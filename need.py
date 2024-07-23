# https://rosalind.info/problems/need/
# Get match and mismatch score from EDNAfull 
# https://rosalind.info/glossary/dnafull/

from Bio import Entrez, SeqIO, Align

with open("rosalind_need.txt", "r") as f:
    genbank_ids = ", ".join(f.readline().strip().split())
Entrez.email = "shalinisinha602@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=[genbank_ids], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
aligner = Align.PairwiseAligner()

aligner.mode = 'global'
aligner.open_gap_score = -10
aligner.extend_gap_score = -1
aligner.match_score = 5
aligner.mismatch_score = -4

alignments = aligner.align(records[0].seq, records[1].seq)
print(alignments[0].score)


