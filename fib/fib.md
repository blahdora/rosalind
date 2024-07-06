### Link:

https://rosalind.info/problems/fib/

### **Description:**

**Given:** Positive integers 𝑛≤40 and 𝑘≤5.

**Return:** The total number of rabbit pairs that will be present after 𝑛 months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of 𝑘 rabbit pairs (instead of only 1 pair).

### **Explanation:**

In this variation of the Fibonacci sequence problem, the key difference is that each pair of reproduction-age rabbits produces k pairs of rabbits instead of just one. To solve this, let's clarify the assumptions and develop a modified recurrence relation:

#### Assumptions:

1. Each rabbit pair reaches reproductive age at the end of their first month.
2. Every month, each pair of reproduction-age rabbits produces k new rabbit pairs.

#### Modified Recurrence Relation:

- Let Fn represent the number of rabbit pairs alive after the n-th month.
- Initially, F1=1 (we start with one pair of rabbits).
- The number of rabbit pairs alive in any month is the sum of:
  - The number of rabbit pairs that were alive the previous month (Fn−1), and
  - The number of new rabbit pairs produced by reproduction-age rabbits, which is k×Fn−2 (the rabbits that were alive two months prior, because they will have reached reproductive age).

### Recurrence Relation:

Fn = Fn−1 + k × Fn−2

#### Steps:

- We initialize a list F to store the number of rabbit pairs for each month.
- Since python uses 0-based index numbering, we set the base cases F[0]=1and F[1]=1
- We use a loop to fill in the values for F[2] to F[n-1] using the recurrence relation
- Finally, we return F[n-1].
