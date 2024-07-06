# Link: https://rosalind.info/problems/rna/

with open('rosalind_rna.txt', 'r') as f:
    lines = f.readlines()
line = lines[0].strip()
print(line.replace('T', 'U'))
