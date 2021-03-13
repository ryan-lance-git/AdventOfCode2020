
f = open('1-1 input.txt')

mylist = [int(line) for line in f.readlines()]

# 1-1
for i in mylist:
    for j in mylist:
        if i + j == 2020:
            print(f'{i} and {j} sum to 2020, multiplying them together yields {i*j}')

# 1-2
for i in mylist:
    for j in mylist:
        for k in mylist:
            if i + j +k == 2020:
                print(f'{i}, {j} and {k} sum to {i+j+k}, multiplying them together yields {i*j*k}')
