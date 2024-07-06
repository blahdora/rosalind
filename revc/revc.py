# Link: https://rosalind.info/problems/revc/

with open("rosalind_revc.txt", "r") as f:
    lines = f.readlines()
dna_string = lines[0].strip()
reversed_string = dna_string[::-1]
replacements = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
complement = ''.join(replacements[base] for base in reversed_string)
print(complement)
