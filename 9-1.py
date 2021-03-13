
with open('9 input.txt') as f:
    data = [int(x) for x in f.read().split('\n')]

pre = 25 # There are 25 number in the preamble
pos = pre 

def look_solution(pos, p=False):

    found = False
    for i in data[pos-pre:pos]:
        for j in data[pos-pre:pos]:

            # Skip the i=j case
            if i==j: continue
            
            if i+j == data[pos]:
                if p: print(f"{i} plus {j} equals {data[pos]}")
                found = True

    if not found:
        print(f"No solution for position {pos}, {data[pos]}")

for num in range(pre, len(data)):
    look_solution(num)
