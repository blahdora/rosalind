# https://rosalind.info/problems/phre/
# https://biopython.org/docs/1.75/api/Bio.SeqRecord.html

from Bio import SeqIO

c = 0
with open("rosalind_phre.txt", "r") as f:
    t = int(f.readline())
    for record in SeqIO.parse(f, "fastq"):
        q = record.letter_annotations["phred_quality"]
        avg = sum(q)/len(q)
        if avg < t:
            c += 1
print(c)