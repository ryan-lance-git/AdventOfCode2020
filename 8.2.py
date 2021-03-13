import copy 
d = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

data = [(op, int(val)) for op, val in [x.split(' ') for x in d.split('\n')]]

with open('8 input.txt') as f:
    data = [[op, int(val)] for op, val in [x.split(' ') for x in f.read().split('\n')]]

def get_pos_after_jump(pos, jmp_val, s):
    new_pos = pos + jmp_val
    if 0 < new_pos < s:
        return new_pos
    if new_pos < 0:
        return new_pos + s
    if new_pos > s:
        return new_pos - s

def check_ends(data):
    # Will need this for looping
    s = len(data)
    final = s - 1 # the final position

    # Keep track of the accumulator and current position
    acc = 0
    pos = 0

    # Keep track of the last visited positions
    last_pos = []

    while True:
        # Check if I've alreay been here (Termination Condition)
        if pos in last_pos and pos != final:
            print(f"Final acc value: {acc}")
            return False
        # Check if I'm at the final position (Termination Condition)
        if pos == final:
            print(f"Part2 Solution! Final acc value: {acc}")
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
            pos = get_pos_after_jump(pos, val, s)

# Part 1
check_ends(data)

# Part 2
for i, item in enumerate(data):
    new_data = copy.deepcopy(data)
    
    if item[0] == 'nop':
        new_data[i][0] = 'jmp'
        check_ends(new_data)

    if item[0] == 'jmp':
        new_data[i][0] = 'nop'
        check_ends(new_data)




