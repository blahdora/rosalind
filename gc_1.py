from collections import defaultdict

sequences = defaultdict(str)
with open("rosalind_gc.txt", "r") as f:
    header = None
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            header = line
        else:
            if header:
                sequences[header] += line
#print(sequences)

gc_content = {}
for index, sequence in sequences.items():
    gc_content[index] = ((sequence.count("C") + sequence.count("G"))*100 / len(sequence))
max_gc = max(gc_content.values())
#print(gc_content)
print(index[1:])
print("{:.6f}".format(max_gc))
