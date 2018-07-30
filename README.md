# QC Plots

This repository contains a python script to create a simple diagnostic plot of read quality from input `.fastq` files. The `data/` folder includes two example data files, with 1000 reads for forward and reverse, respectively (source: <https://www.ncbi.nlm.nih.gov/sra/SRR622461>).
 
## Requirements

To run the script you'll need **python** installed. An installation of **Anaconda 3.x** is recommended:

https://www.anaconda.com/download/

The code requires the `biopython` and `matplotlib` modules:

`pip install biopython matplotlib` 

## Usage

From the terminal use the following command to generate the read quality diagnostic plot:

`python qcheck.py data/SRR622461_2.fastq data/SRR622461_2.fastq`
