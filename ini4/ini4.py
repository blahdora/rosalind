with open("rosalind_ini4.txt", "r") as file:
    lines = file.readlines()
input_range = lines[0].strip().split(" ")
total_sum = 0
if int(input_range[0]) % 2 == 0:
    for i in range(int(input_range[0])+1, int(input_range[1])+1, 2):
        total_sum += i
else:
    for i in range(int(input_range[0]), int(input_range[1])+1, 2):
        total_sum += i
print(total_sum)

