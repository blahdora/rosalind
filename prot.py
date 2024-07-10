from Bio.Seq import Seq
with open("rosalind_prot.txt", "r") as file:
    rna = Seq(file.readline().strip())
prot = rna.translate(to_stop=True)
print(prot)
