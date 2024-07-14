# Link: https://rosalind.info/problems/grph/

from Bio import SeqIO

sequences_with_ids = []

with open("rosalind_grph.txt") as f:
    for record in SeqIO.parse(f, "fasta"):
        sequences_with_ids.append((record.id, record.seq))

for id1, seq1 in sequences_with_ids:
    for id2, seq2 in sequences_with_ids:
        if id1 != id2 and seq1[-3:] == seq2[:3]:
            print(id1 + " " + id2)