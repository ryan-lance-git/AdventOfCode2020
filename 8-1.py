
with open('8 input.txt') as f:
    data = [(op, int(val)) for op, val in [x.split(' ') for x in f.read().split('\n')]]

##d = '''nop +0
##acc +1
##jmp +4
##acc +3
##jmp -3
##acc -99
##acc +1
##jmp -4
##acc +6'''
##
##data = [(op, int(val)) for op, val in [x.split(' ') for x in d.split('\n')]]

def get_pos_after_jump(pos, jmp_val):
    new_pos = pos + jmp_val
    
    if 0 < new_pos < s:
        return new_pos
    
    if new_pos < 0:
        return new_pos + s

    if new_pos > s:
        return new_pos - s

# Will need this for looping
s = len(data)

# Keep track of the accumulator and current position
acc = 0
pos = 0

# Keep track of the last visited positions
last_pos = []

while True:

    # Check if I've alreay been here
    if pos in last_pos:
        print(f"final acc value: {acc}")
        break
    
    last_pos.append(pos)
    
    opr = data[pos][0]
    val = data[pos][1]

    if opr == 'nop':
        pos += 1

    if opr == 'acc':
        pos += 1
        acc += val
    
    if opr == 'jmp':
        pos = get_pos_after_jump(pos, val)

    

