# https://www.bioinformatics.org/JaMBW/2/3/TranslationTables.html


from Bio.Seq import translate

with open("rosalind_ptra.txt", "r") as f:
    lines = f.read().strip().split('\n')

dna = lines[0]
protein = lines[1]

for i in range(1,16):
    if translate(dna, table=i, to_stop=True) == protein:
        print(i)
        break