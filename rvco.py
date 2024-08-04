# https://rosalind.info/problems/rvco/ 

from Bio import SeqIO

c = 0
with open("rosalind_rvco.txt", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        sequence = record.seq
        if sequence == sequence.reverse_complement():
            c += 1
print(c)

