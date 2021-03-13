
with open('9 input.txt') as f:
    data = [int(x) for x in f.read().split('\n')]

pre = 25 # There are 25 number in the preamble
pos = pre 

def look_solution(pos, p=False):
    found = False
    for i in data[pos-pre:pos]:
        for j in data[pos-pre:pos]:
            if i==j: continue            
            if i+j == data[pos]:
                if p: print(f"{i} plus {j} equals {data[pos]}")
                found = True
    if not found: return data[pos]

# Part 1 solution
def find_part1():
    for num in range(pre, len(data)):
        s1 = look_solution(num)
        if s1: return s1

s1 = find_part1()

# Part 2 solution
for i, number1 in enumerate(data):
    for j, number2 in enumerate(data[i:]):

        if sum(data[i:j]) == s1:
            s2 = min(data[i:j]) + max(data[i:j])
            print(f"The range {i} to {j} in data adds up to {s1}")
            print(f"The lowest and highest in that range add to {s2}")
