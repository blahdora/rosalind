# Link: https://rosalind.info/problems/fib/

with open("rosalind_fib.txt", "r") as f:
    lines = f.readlines()
n_k = lines[0].split(" ")
n = int(n_k[0])
k = int(n_k[1])
f = [0] * (n+1)
f[0], f[1] = 1, 1
for i in range(2, n):
    f[i] = (k * f[i-2]) + f[i-1]
print(f[n-1])


