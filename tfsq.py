# https://rosalind.info/problems/tfsq/
# https://biopython.org/docs/1.75/api/Bio.SeqIO.html 

from Bio import SeqIO

in_file = "rosalind_tfsq.txt"
out_file = "tfsq.out"

SeqIO.convert(in_file, 'fastq', out_file, 'fasta')

