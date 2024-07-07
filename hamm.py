with open("rosalind_hamm.txt", "r") as f:
    lines = f.readlines()
b1 = lines[0].strip()
b2 = lines[1].strip()

dh = 0
for i in range(len(b1)):
    if b1[i] != b2[i]:
        dh += 1
print(dh)