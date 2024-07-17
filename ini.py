with open("rosalind_ini.txt", "r") as f:
    seq = f.read().strip()
print(seq.count('A'))
print(seq.count('C'))
print(seq.count('G'))
print(seq.count('T'))