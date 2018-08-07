#!/usr/bin/env python

import sys
from Bio import SeqIO
import matplotlib.pyplot as plt

# Accept command line argument
if len(sys.argv) < 3:
	print("USAGE: python %s <r1-FASTQ> <r2-FASTQ>" % sys.argv[0])
	sys.exit()

# input fastq file
r1Fastq = sys.argv[1]
r2Fastq = sys.argv[2]

# define plot function
def myPlotFunc(fastq):
	for i,rec in enumerate(SeqIO.parse(fastq,"fastq")):
		if i >= 60:
			break
		plt.plot(rec.letter_annotations["phred_quality"])
	plt.ylim(0,45)
	plt.ylabel("PHRED quality score")
	plt.xlabel("Position")

# plot quality of forward reads
plt.subplot(1,2,1)
myPlotFunc(r1Fastq)

# plot quality of reverse reads
plt.subplot(1,2,2)
myPlotFunc(r2Fastq)

# save plot
plt.savefig("plots/plot.png")

print("Done")
sys.exit()
