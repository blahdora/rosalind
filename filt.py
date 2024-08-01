# https://rosalind.info/problems/filt/ 
# https://biopython.org/docs/1.75/api/Bio.SeqIO.QualityIO.html 

from Bio import SeqIO

with open("rosalind_filt.txt", "r") as f:
    q, p = map(int, f.readline().strip().split())
    valid_reads = 0
    for record in SeqIO.parse(f, "fastq"):
        phred = record.letter_annotations["phred_quality"]

        total_bases = len(phred)
        high_quality = sum(score >= q for score in phred)
        percentage = (high_quality / total_bases) * 100

        if percentage >= p:
            valid_reads += 1

print(valid_reads)


