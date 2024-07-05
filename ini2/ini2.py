with open("rosalind_ini2.txt", "r") as file:
    lines = file.readlines()
legs = lines[0].strip()
legs_array = legs.split(" ")
print(int(legs_array[0])**2 + int(legs_array[1])**2)
