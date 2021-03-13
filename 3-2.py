import math
f = open('3-1 input.txt').readlines()
f = list(map(lambda s: s.strip(), f))

width = len(f[0])

def check_tree(row, pos):
    if row[pos] == '#': return 1
    return 0

def increment(i, amount):
    if i + amount < width:
        return i + amount
    else:
        return i + amount - width

incs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
totals = []

for inc in incs:
    right = inc[0]
    down  = inc[1]
    total = 0
    i = 0
    
    for j, row in enumerate(f):
        if j % down == 0:
            total += check_tree(row, i)
            i = increment(i, right)
    
    totals.append(total)

r = 1
for item in totals:
    r *= item

print(totals)
print(r)
