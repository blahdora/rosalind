with open('rosalind_iprb.txt', 'r') as f:
    lines = f.readlines()

line = lines[0].split(" ")
k, m, n = int(line[0]), int(line[1]), int(line[2])

org = k+m+n
Pk = (k/org) *((k-1) / (org-1)) 
Pm = (m/org) *((m-1) / (org-1)) * (3/4)
Pkm = 2 * (k/org) * (m/(org-1)) 
Pmn = 2 * (m/org) * (n/(org-1)) * (1/2)
Pkn = 2 * (k/org) * (n/(org-1))

print(f"{Pk+Pm+Pkm+Pkn+Pmn:.5f}")