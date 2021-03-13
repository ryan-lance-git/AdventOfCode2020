import re

f = open('2-2 input.txt')

REGEX = r'(\d+)\-(\d+) (\w)\: (\w*)\n?'

mylist = f.readlines()

pos1  = [re.match(REGEX, item).group(1) for item in mylist]
pos2  = [re.match(REGEX, item).group(2) for item in mylist]
chars = [re.match(REGEX, item).group(3) for item in mylist]
strs  = [re.match(REGEX, item).group(4) for item in mylist]

pos1 = list(map(lambda x: int(x) - 1, pos1))
pos2 = list(map(lambda x: int(x) - 1, pos2))

total = 0
for i in range(len(mylist)):
    if strs[i][pos1[i]] == chars[i] ^ strs[i][pos2[i]] == chars[i]:
        total += 1
        
print(total)
