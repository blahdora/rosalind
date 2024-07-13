# Link: https://rosalind.info/problems/fib/

with open("rosalind_fib.txt", "r") as f:
    n, k = map(int, f.read().strip().split())

f = [0] * (n+1)
f[0], f[1] = 1, 1
for i in range(2, n):
    f[i] = (k * f[i-2]) + f[i-1]
print(f[n-1])


