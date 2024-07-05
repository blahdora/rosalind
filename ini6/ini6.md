### Link:

https://rosalind.info/problems/ini6/

### **Description:**

**Given:** A string 𝑠 of length at most 10000 letters.

**Return:** The number of occurrences of each word in 𝑠, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

### **Explanation:**

1. Open the file 'rosalind_ini6.txt' for reading as f
2. Read all lines from f into a list called lines
3. Initialize an empty dictionary dic
4. Remove leading and trailing whitespace from the first line of lines and store it in string
5. Split string into a list of words using space as the delimiter and store it in words
6. For each word in words:
     - If word is already a key in dic:
         - Increment the corresponding value in dic by 1
     - Else:
         - Add word as a key to dic with a value of 1
7. For each key-value pair (index, value) in dic.items():
     - Print index
     - Print value
