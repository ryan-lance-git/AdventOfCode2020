
with open('6-1 input.txt') as file:
    data = file.read().split('\n\n')

def unique_letters(string):
    s = ''
    for L in string:
        if L not in s:
            s += L
    return s

uniques = [unique_letters(x) for x in [x.replace('\n', '') for x in data]]

print('Ans to 6-1:', sum([len(x) for x in uniques]))
print('Ans to 6-2:', sum(sum([all([L in x for x in g]) for L in uniques[i]])
                         for i, g in enumerate([x.split('\n') for x in data])))

