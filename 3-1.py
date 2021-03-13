f = open('3-1 input.txt').readlines()
f = list(map(lambda s: s.strip(), f))

width = len(f[0])

i = 0
total = 0

def check_tree(row, pos):
    if row[pos] == '#': return 1
    return 0

def increment(i, amount):
    if i + 3 < width:
        return i + 3
    else:
        return i + 3 - width

for j, row in enumerate(f):
    if j % 1 == 0:
        total += check_tree(row, i)
        i = increment(i, 3)

print(total)


