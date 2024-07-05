### Link:

https://rosalind.info/problems/ini5/

### **Description:**

**Given:** A file containing at most 1000 lines.

**Return:** A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

### **Explanation:**

This code reads lines from the file "rosalind_ini5.txt" and writes every second line (starting from the second line) to a new file called "output_ini5.txt".  Here's a short explanation of the given code:

1. **Reading the input file:**
   - `with open("rosalind_ini5.txt", "r") as file:` opens the file named "rosalind_ini5.txt" in read mode.
   - `lines = file.readlines()` reads all lines from the file and stores them in the list `lines`.
2. **Writing to the output file:**
   - `with open("output_ini5.txt", "w") as out_file:` opens the file named "output_ini5.txt" in write mode. If the file doesn't exist, it will be created; if it does exist, its contents will be overwritten.
   - `for i in range(1, len(lines), 2):` iterates over the indices of `lines`, starting from 1 and skipping every other line (i.e., it processes every second line, starting with the second one).
   - `out_file.write(lines[i])` writes the lines at the selected indices to the output file.
