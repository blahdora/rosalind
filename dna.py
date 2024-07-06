# Link: https://rosalind.info/problems/dna/

with open('rosalind_dna.txt', 'r') as f:
    lines = f.readlines()
line = lines[0].strip()
print(line.count('A'))
print(line.count('C'))
print(line.count('G'))
print(line.count('T'))
