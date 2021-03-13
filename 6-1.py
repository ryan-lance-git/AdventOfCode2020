
with open('6-1 input.txt') as file:
    data = file.read().split('\n\n')
    data = [x.replace('\n','') for x in data]

def count_unique_letters(string):
    s = ''
    for L in string:
        if L not in s:
            s += L
    return len(s)

counts = [count_unique_letters(x) for x in data]

print('Ans to 6-1:', sum(counts))


