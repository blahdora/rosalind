### Link:

https://rosalind.info/problems/ini3/

### **Description:**

**Given:** A string 𝑠 of length at most 200 letters and four integers 𝑎, 𝑏, 𝑐 and 𝑑.

**Return:** The slice of this string from indices 𝑎 through 𝑏 and 𝑐 through 𝑑 (with space in between), *inclusively*. In other words, we should include elements 𝑠[𝑏] and 𝑠[𝑑] in our slice.

### **Explanation:**

It's a straightforward string manipulation problem using string stripping and slicing. The script reads an input string and four indices from a file. It then extracts two substrings from the input string using these indices and prints the result. Here's a step-by-step description:

1. **Open and Read File**: The code opens the file "rosalind_ini3.txt" and reads its contents.
2. **Extract Input Data:** It retrieves the input string and the indices from the first and second line of the file respectively.
3. **Parse Indices**: The indices are split into individual values and converted to integers.
4. **Extract Substrings:**
   - The code extracts two substrings from the input string using the provided indices.
   - The first substring is extracted from index `i1` to `i2` (inclusive).
   - The second substring is extracted from index `i3` to `i4` (inclusive).
5. **Print Result**: The extracted substrings are concatenated with a space between them and printed.
