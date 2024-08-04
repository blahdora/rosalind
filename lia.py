from scipy.stats import binom

def prob(k, N):
    # Total no. of orgs in kth gen
    norgs = 2 ** k

    # Probability of AaBb genotype
    p = 1/4

    # Prob of >= N AaBb
    pN = 1 - binom.cdf(N -1, norgs, p)

    return round(pN, 3)

if __name__ == "__main__":
    with open("rosalind_lia.txt", "r") as f:
        k, N = map(int, f.readline().strip().split())
    print(prob(k, N))

