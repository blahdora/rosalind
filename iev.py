with open("rosalind_iev.txt", "r") as f:
    couples = list(map(int, f.read().strip().split()))

#gen = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']
p_dom = [2, 2, 2, 1.5, 1, 0] #probability of dom phenotype in offspring
p = 0
for i in range(len(couples)):
    p += (couples[i] * p_dom[i]) 
        
print(p)