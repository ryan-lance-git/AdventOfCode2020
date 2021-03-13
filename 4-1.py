import yaml

all_fields  = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields      = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('4-1 input.txt') as file:
    data = []
    groups = file.read().split('\n\n')
    print('Number of groups:', len(groups))
    for item in groups:
        temp = yaml.load(item.replace(' ', '\n').replace(":", ": "))
        data.append(temp)

count_valid = 0
count_invalid = 0

for passport in data:
    
    is_good = True
    for field in fields:
        if field not in passport.keys():
            is_good = False
            
    if is_good:
        #print('GOOD passport:\n', passport.keys(), '\n')
        count_valid += 1

    if not is_good:
        #print('BAD passport:\n', passport.keys(), '\n')
        count_invalid += 1

print(count_valid)
print(count_invalid)
