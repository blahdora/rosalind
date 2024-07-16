# https://rosalind.info/problems/lcsm/

from Bio import SeqIO

def find_lcs(sequences):
    if not sequences:
        return ""

    def lcs2(s1, s2):
        n1 = len(s1)
        n2 = len(s2) 
        # 2d array with n2+1 no of cols and n1+1 rows
        # will hold length of longest common suffix of ss s1[0:i] and s2[0:j]
        dp = [[0]*(n2+1) for _ in range (n1+1)]
        max_len = 0
        end_index = 0
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i
                else:
                    dp[i][j] = 0
        return s1[end_index - max_len : end_index]


    lcs = sequences[0]
    for i in range(1, len(sequences)):
        lcs =  lcs2(lcs, sequences[i])
        if not lcs:
            break
    return lcs

sequences = []
with open("rosalind_lcsm.txt", "r") as f:
    for line in SeqIO.parse(f, "fasta"):
        sequences.append(line.seq)

print(find_lcs(sequences))
