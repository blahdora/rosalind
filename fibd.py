
import numpy as np

with open("rosalind_fibd.txt", "r") as f:
    n, m = map(int, f.read().strip().split())

pop = np.zeros([n+1, m], dtype=np.int64)
pop[1][0] = 1

for month in range(2, n+1):
    for age in range(m):
        if age > 0:
            pop[month][age] = pop[month-1][age-1]
        else:
            pop[month][age] = np.sum(pop[month-1, 1:])
print(np.sum(pop[month]))

