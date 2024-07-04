### Link:

https://rosalind.info/problems/ini4/

### **Description:**

**Given:** Two positive integers 𝑎 and 𝑏 (𝑎<𝑏<10000).

**Return:** The sum of all odd integers from 𝑎 through 𝑏, inclusively.

### **Explanation:**

The Python script reads a range of integers from input file "rosalind_ini4.txt" and calculates the sum of all odd integers within that range (inclusive). Here's a step-by-step description:

1. **Open and Read File**: The code opens the file "rosalind_ini4.txt" and reads its contents.
2. **Extract Range**: It retrieves the range of integers from the first line of the file, splitting it into two values.
3. **Initialize Sum**: A variable `total_sum` is initialized to 0 to store the sum of odd numbers.
4. **Sum Odd Numbers:**
   - If the starting number is even, it starts summing from the next odd number.
   - If the starting number is odd, it starts summing from that number.
5. **Print Result**: Finally, the sum of all odd integers in the specified range is printed.
