import argparse
from pybedtools import BedTool
import pyBigWig 
import pandas as pd
import numpy as np 
import pdb
import csv
import sys
from .classification_label_protocols import *
from .regression_label_protocols import * 
from multiprocessing.pool import ThreadPool
import gzip 

#Approaches to determining classification labels
#Others can be added here (imported from classification_label_protocols) 
labeling_approaches={
    "peak_summit_in_bin_classification":peak_summit_in_bin_classification,
    "peak_percent_overlap_with_bin_classification":peak_percent_overlap_with_bin_classification,
    "peak_summit_in_bin_regression":peak_summit_in_bin_regression,
    "peak_percent_overlap_with_bin_regression":peak_percent_overlap_with_bin_regression,
    "all_genome_bins_regression":all_genome_bins_regression
    }

def parse_args():
    parser=argparse.ArgumentParser(description="Generate genome-wide labeled bins for a set of narrowPeak task files ")
    parser.add_argument("--task_list",help="this is a tab-separated file with the name of the task in the first column, the path to the corresponding narrowPeak(.gz) file in the second column (optionally), and the path to the corresponding bigWig file in the third column (optionally, for regression)")
    parser.add_argument("--outf",help="output filename that labeled bed file will be saved to.")
    parser.add_argument("--output_type",choices=['gzip','hdf5','pkl','bz2'],default='gzip',help="format to save output, one of gzip, hdf5, pkl, bz2")
    parser.add_argument("--split_output_by_chrom",action="store_true",default=False) 
    parser.add_argument("--chrom_sizes",help="chromsizes file for the reference genome. First column is chrom name; second column is chrom size")
    parser.add_argument("--chroms_to_keep",nargs="+",default=None,help="list of chromosomes, as defined in the --chrom_sizes file, to include in label generation. All chromosomes will be used if this argument is not provided. This is most useful if generating a train/test/validate split for deep learning models")
    parser.add_argument("--chroms_to_exclude",nargs="+",default=None,help="list of chromosomes, as defined in the --chrom_sizes file, to exclude in label generation. No chromosomes will be excluded if this argument is not provided. This is most useful if generating a train/test/validate split for deep learning models")
    parser.add_argument("--bin_stride",type=int,default=50,help="bin_stride to shift adjacent bins by")
    parser.add_argument("--left_flank",type=int,default=400,help="left flank")
    parser.add_argument("--right_flank",type=int,default=400,help="right flank")
    parser.add_argument("--bin_size",type=int,default=200,help="flank around bin center where peak summit falls in a positive bin")
    parser.add_argument("--threads",type=int,default=1)
    parser.add_argument("--subthreads",type=int,default=4,help="This is only useful for regression labels for each bin in the genome. Each task-thread will generate n subthreads to allow for parallel processing of chromosomes. Reduce number to use fewer threads")
    parser.add_argument("--overlap_thresh",type=float,default=0.5,help="minimum percent of bin that must overlap a peak for a positive label")
    parser.add_argument("--allow_ambiguous",default=False,action="store_true")
    parser.add_argument("--labeling_approach",choices=["peak_summit_in_bin_classification",
                                                       "peak_percent_overlap_with_bin_classification",
                                                       "peak_summit_in_bin_regression",
                                                       "peak_percent_overlap_with_bin_regression",
                                                       "all_genome_bins_regression"])
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)       
    return parser.parse_args()

def get_labels_one_task(inputs):
    #unravel the inputs 
    task_name=inputs[0]
    task_bed=inputs[1]
    task_bigwig=inputs[2]
    chrom=inputs[3]
    first_coord=inputs[4]
    final_coord=inputs[5]
    args=inputs[6]
    #determine the appropriate labeling approach
    return labeling_approaches[args.labeling_approach](task_name,task_bed,task_bigwig,chrom,first_coord,final_coord,args)    
    
def get_chrom_labels(inputs):
    #unravel inputs 
    chrom=inputs[0]
    chrom_size=inputs[1]
    bed_and_bigwig_dict=inputs[2]
    tasks=inputs[3]
    args=inputs[4] 

    #pre-allocate a pandas data frame to store bin labels for the current chromosome. Fill with zeros    
    #determine the index tuple values
    index_tuples,first_bin_start,final_bin_start=get_indices(chrom,chrom_size,args) 
    chrom_df = pd.DataFrame(0, index=index_tuples, columns=tasks[0])
    print("pre-allocated df for chrom:"+str(chrom)+"with dimensions:"+str(chrom_df.shape))

    #create a thread pool to label bins, each task gets assigned a thread 
    pool_inputs=[] 
    pool=ThreadPool(args.threads)
    for task_name in bed_and_bigwig_dict: 
        task_bed=bed_and_bigwig_dict[task_name]['bed']
        task_bigwig=bed_and_bigwig_dict[task_name]['bigwig']
        pool_inputs.append((task_name,task_bed,task_bigwig,chrom,first_bin_start,final_bin_start,args))
    bin_values=pool.map(get_labels_one_task,pool_inputs)
    pool.close()
    pool.join()
    
    for task_name,task_labels in bin_values: 
        chrom_df[task_name]=task_labels
    if args.split_output_by_chrom==True:
        assert args.output_type in ["gzip","bz2"]
        index_label=['Chrom','Start','End']
        chrom_df.to_csv(args.outf+"."+chrom,sep='\t',float_format="%.2f",header=True,index=True,index_label=index_label,mode='wb',compression=args.output_type,chunksize=1000000) 
    return (chrom, chrom_df)

def get_bed_and_bigwig_dict(tasks):
    print("creating dictionary of bed files and bigwig files for each task:")
    bed_and_bigwig_dict=dict()
    for index,row in tasks.iterrows():
        task_name=row[0]
        print(task_name) 
        bed_and_bigwig_dict[task_name]=dict() 
        #get the peak file associated with the task (if provided) 
        try:
            task_bed=BedTool(row[1])
        except:
            print("No Peak file was provided for task:"+task_name+"; Make sure this is intentional")
            task_bed==None
        bed_and_bigwig_dict[task_name]['bed']=task_bed 
        #get the BigWig file associated with the task (if provided)
        try:
            task_bigwig=pyBigWig.open(row[2])
        except:
            print("No BigWig file was provided for task:"+task_name+"; Make sure this is intentional")
            task_bigwig=None
        bed_and_bigwig_dict[task_name]['bigwig']=task_bigwig
    return bed_and_bigwig_dict

def get_indices(chrom,chrom_size,args):
    final_bin_start=((chrom_size-args.right_flank-args.bin_size)//args.bin_stride)*args.bin_stride
    #final_coord=(chrom_size//args.bin_stride)*args.bin_stride
    first_bin_start=args.left_flank 
    indices=[tuple([chrom,i-args.left_flank,i+args.bin_size+args.right_flank]) for i in range(first_bin_start,final_bin_start+1,args.bin_stride)]
    return indices,first_bin_start,final_bin_start


def write_output(task_names,full_df,args):
    '''
    Save genome-wide labels to disk in gzip, hdf5, or pkl format 
    '''
    if args.output_type=="gzip":
        index_label=['Chrom','Start','End']
        full_df.to_csv(args.outf,sep='\t',header=True,index=True,index_label=index_label,mode='wb',compression='gzip',chunksize=1000000)
    elif args.output_type=="bz2":
        index_label=['Chrom','Start','End']
        full_df.to_csv(args.outf,sep='\t',header=True,index=True,index_label=index_label,mode='wb',compression='bz2',chunksize=1000000)
    elif args.output_type=="hdf5":
        store=pd.HDFStore(args.outf)
        store['df']=full_df
        store.close()
        
    elif args.output_type=="pkl":
        full_df.to_pickle(args.outf,compression="gzip")

def genomewide_labels(args):
    if type(args)==type({}):
        #create an argparse.Namespace from the dictionary of inputs
        args_object=argparse.Namespace()
        for key in args:
            vars(args_object)[key]=args[key]
        args=args_object 

    #read in the metadata file with:
    #task names in column 1,
    #path to peak file in column 2,
    #path to bigWig file in column 3
    tasks=pd.read_csv(args.task_list,sep='\t',header=None)
    bed_and_bigwig_dict=get_bed_and_bigwig_dict(tasks) 

    #col1: chrom name
    #col2: chrom size 
    chrom_sizes=pd.read_csv(args.chrom_sizes,sep='\t',header=None)

    processed_first_chrom=False
    #create a ThreadThreadPool to process chromosomes in parallel
    print("creating chromosome thread pool")
    pool=ThreadPool(args.threads)
    pool_args=[]
    chrom_order=[] 
    for index,row in chrom_sizes.iterrows():
        chrom=row[0]
        
        #determine whether this chromosome should be included in the label file
        if args.chroms_to_keep!=None:
            if chrom not in args.chroms_to_keep:
                continue
        if args.chroms_to_exclude!=None:
            if chrom in args.chroms_to_exclude:
                continue 
        chrom_order.append(chrom) 
        chrom_size=row[1]
        pool_args.append((chrom,chrom_size,bed_and_bigwig_dict,tasks,args))
    print("launching thread pool")
    processed_chrom_outputs=pool.map(get_chrom_labels,pool_args)
    pool.close()
    pool.join()

    #if the user is happy with separate files for each chromosome, these have already been written to disk. We are done 
    if args.split_output_by_chrom==True:
        exit()
        
    print("expanding chromosome pool outputs") 
    processed_chrom_outputs_dict=dict() 
    for chrom,chrom_df in processed_chrom_outputs:
        processed_chrom_outputs_dict[chrom]=chrom_df
        
    print("concatenating data frames for chromosomes")
    for chrom in chrom_order: 
        if processed_first_chrom==False:
            full_df=processed_chrom_outputs_dict[chrom]
            processed_first_chrom=True 
        else:
            #concatenate
            full_df=pd.concat([full_df,processed_chrom_outputs_dict[chrom]],axis=0)
    full_df=full_df.astype('float64',copy=False)
    print("writing output dataframe to disk")
    write_output(tasks[0],full_df,args)
    print("done!") 

def main():
    args=parse_args()     
    genomewide_labels(args)
    
if __name__=="__main__":
    main()
