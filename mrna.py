# https://rosalind.info/problems/mrna/ 

from Bio.Data import CodonTable

def reverseTranslate(protein):
    MOD = 1_000_000 # numeric literal w/ underscores = 1000000

    # Get the standard codon table
    codon_table = CodonTable.unambiguous_dna_by_id[1]

    # Create a dictionary to map each AA to possible codons
    aa2codons = {}
    for codon, aa in codon_table.forward_table.items():
        if aa not in aa2codons:
            aa2codons[aa] = []
        aa2codons[aa].append(codon)
    
    # Add the stop codon
    aa2codons['*'] = ['TAA', 'TAG', 'TGA']

    # Initialize a list for dp
    dp = [0] * (len(protein) + 1)
    dp[len(protein)] = 1 # Base case: 1 way to complete an empty seq

    # Compute the no of ways to form the protein seq
    for i in range(len(protein)-1, -1, -1):
        aa = protein[i]
        if aa in aa2codons:
            for codon in aa2codons[aa]:
                dp[i] = (dp[i] + dp[i+1]) % MOD
    
    # Multiply by the no of stop codons
    result = dp[0] * len(aa2codons['*'])
    return result % MOD

if __name__ == "__main__":
    with open("rosalind_mrna.txt", "r") as f:
        protein = f.readline().strip()
    print(reverseTranslate(protein))