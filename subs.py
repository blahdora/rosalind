with open("rosalind_subs.txt", "r") as f:
    lines = f.readlines()

s = lines[0].strip()
t = lines[1].strip()

for i in range(len(s)):
    if s[i:].startswith(t):
        print(i+1)

