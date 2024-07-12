import numpy as np
from Bio import SeqIO # Using multiple sequences so preferred over Seq

sequences = []
with open("rosalind_cons.txt", "r") as f:
    for line in SeqIO.parse(f, "fasta"):
        sequences.append(line.seq) # .seq is an attribute of SeqRecord's objs
        x = len(line)
        profile_matrix = np.zeros((4, x), dtype=int)
for i in range(len(sequences)):
    s = sequences[i]
    for j in range(len(s)):
        if s[j] == "A":
            profile_matrix[0][j] += 1
        elif s[j] == "C":
            profile_matrix[1][j] += 1 
        elif s[j] == "G":
            profile_matrix[2][j] += 1 
        else:
            profile_matrix[3][j] += 1
res =  np.argmax(profile_matrix, axis=0)
res_string = [0] * x
for i in range(len(res)):
    if res[i] == 0:
        res_string[i] = "A"
    elif res[i] == 1:
        res_string[i] = "C"
    elif res[i] == 2:
        res_string[i] = "G"
    else:
        res_string[i] = "T"
print("".join(res_string))
print("A: " + " ".join(map(str, profile_matrix[0])))
print("C: " + " ".join(map(str, profile_matrix[1])))
print("G: " + " ".join(map(str, profile_matrix[2])))
print("T: " + " ".join(map(str, profile_matrix[3])))
    



