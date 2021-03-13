
with open('5-1 input.txt') as file:
    data = [x.strip() for x in file.readlines()]

def calc_uid(string):
    row = 0
    col = 0

    for i, L in enumerate(string):
        
        if i < 6:
            addr = 2 ** (6 - i)
            if L == 'B':
                row += addr
                
        else:
            addr = 2 ** (9 - i)
            if L == 'R':
                col += addr

    return row * 8 + col


print('Ans to 5-1:',max([calc_uid(x) for x in data]))


'''
rows
i, addr
0, 64
1, 32
2, 16
3, 8
4, 4
5, 2
6, 1

cols
i, addr
7, 4
8, 2
9, 1
'''

