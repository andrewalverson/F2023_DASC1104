#!/usr/bin/env python3

# this script will read in 2 files: covid_genes.gff3 and covid.fasta
# calculate and report the length of the genome
# read the GFF file, get the start and end coords for each gene, and
	# extract that gene from the genome

# specify the input files
fasta_file = 'covid.fasta'
gff_file   = 'covid_genes.gff3'

# read in the input files

# reading in the genome from covid.fasta
# skip the first header line
# need to remove all the line breaks and save the genome in one big string

# read in the FASTA file
with open(fasta_file, 'r') as FASTA:
	for line in FASTA:
		print(line)