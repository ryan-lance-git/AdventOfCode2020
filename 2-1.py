import re

f = open('2-2 input.txt')

REGEX = r'(\d+)\-(\d+) (\w)\: (\w*)\n?'

mylist = f.readlines()

mins  = [re.match(REGEX, item).group(1) for item in mylist]
maxs  = [re.match(REGEX, item).group(2) for item in mylist]
chars = [re.match(REGEX, item).group(3) for item in mylist]
strs  = [re.match(REGEX, item).group(4) for item in mylist]



total = 0
for i, item in enumerate(mylist):
    cnt_chars = strs[i].count(chars[i])

    if int(maxs[i]) >= cnt_chars >= int(mins[i]):
        total += 1
