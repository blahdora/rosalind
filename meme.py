# https://rosalind.info/problems/meme/ 

'''
meme rosalind_meme.txt -text -minw 20 2>/dev/null | grep -A 2 "MEME-1 regular expression"
'''

# Script to get regular expression from list of motifs

from collections import Counter

def generate_consensus_and_regex(sequences):
    # Transpose the list of sequences to get columns
    transposed = list(zip(*sequences))
    consensus = ""
    regex = ""

    for col in transposed:
        count = Counter(col)
        most_common_base, most_common_count = count.most_common(1)[0]
        consensus += most_common_base

        # Create regex part
        if len(count) > 1:
            bases = ''.join(sorted(count.keys()))
            regex += f"[{bases}]"
        else:
            regex += most_common_base

    return consensus, regex

# Read the input sequences from a file
with open('rosalind_meme.txt', 'r') as file:
    sequences = [line.strip() for line in file.readlines() if line.strip()]

# Generate consensus and regex
consensus, regex = generate_consensus_and_regex(sequences)

# Output the results
print(f"Consensus Sequence: {consensus}")
print(f"Regular Expression: {regex}")
