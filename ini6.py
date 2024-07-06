with open('rosalind_ini6.txt', 'r') as f:
    lines = f.readlines()
dic = {}
string = lines[0].strip() 
words = string.split(" ") 
for word in words: 
    if word in dic:
        dic[word] += 1 
    else:
        dic[word] = 1
for index, value in dic.items():
    print(index)
    print(value)