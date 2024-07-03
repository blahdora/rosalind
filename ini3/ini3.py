with open('rosalind_ini3.txt', 'r') as file:
    lines = file.readlines()
input_string = lines[0].strip()
input_indices = lines[1].strip()
indices = input_indices.split(" ")
print(indices)
i1, i2, i3, i4 = int(indices[0]), int(indices[1]), int(indices[2]), int(indices[3])
print(input_string[i1:i2+1]+ " " + input_string[i3:i4+1])