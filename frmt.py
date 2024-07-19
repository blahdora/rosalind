# https://rosalind.info/problems/frmt/

from Bio import Entrez, SeqIO

def shortest_seq(ids):
    Entrez.email = "shalinisinha602@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=[", ".join(ids)], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    print(min(records, key=lambda s: len(s.seq)).format("fasta"))

if __name__ == "__main__":
    with open("rosalind_frmt.txt", "r") as f:
        ids = f.readline().strip().split()
    shortest_seq(ids)