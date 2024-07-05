with open("rosalind_ini5.txt", "r") as file:
    lines = file.readlines()

with open("output_ini5.txt", "w") as out_file:
    for i in range(1, len(lines), 2):
        out_file.write(lines[i])
