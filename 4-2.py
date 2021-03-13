import re

all_fields  = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
fields      = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors  = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

with open('4-1 input.txt') as file:
    data = []
    groups = file.read().split('\n\n')
    for item in groups:
        x = [i.split(':') for i in re.split('\n| ', item)]
        d = {}
        for i in x:
            d[i[0]] = i[1]
        data.append(d)


count_valid = 0
count_invalid = 0

for passport in data:
    
    is_good = True
    for field in fields:
        
        if field not in passport:
            is_good = False
            #print('passport does not contain',field, passport)
        
        if field in passport:
            val = passport[field]

            if field=='byr' and not (1920 <= int(val) <= 2002):
                is_good = False
                #print('byr not in range',field, val)


            if field=='iyr' and not (2010 <= int(val) <= 2020):
                is_good = False
                #print('iyr is not in range',field,val)


            if field=='eyr' and not (2020 <= int(val) <= 2030):
                is_good = False
                #print('eyr is not in range', field, val)
                

            if field == 'hcl':
                REGEX = '#([0-9a-f]{6})'
                match = re.match(REGEX, val)
                try:
                    color = match.group(1)
                except:
                    is_good = False
                    #print('hcl not right:',val)


            if field == 'ecl':
                if not val in eye_colors:
                    is_good = False
                    #print('ecl not in eye colors:',field,val)

                    
            if field == 'pid':
                try:
                    int(val)
                except:
                    is_good = False
                    print('pid is not int', field, val)
                    
                if len(val) != 9:
                    is_good = False
                    #print('pid is not len 9:',field, val)


            if field=='hgt':
                REGEX = '(\d+)(in|cm)'
                match = re.match(REGEX, val)
                try:
                    height  = int(match.group(1))
                    unit    = match.group(2)

                    if unit not in ('in', 'cm'):
                        is_good = False
                        #print('unit not in in or cm', field,val)
                    
                    if unit == 'cm':
                        if not (150 <= height <= 193):
                            is_good = False
                            #print('hgt in cm not in range:',field,val)
                        
                    if unit == 'in':
                        if not (59 <= height <= 76):
                            is_good = False
                            #print('hgt in in not in range:',field,val)
                    
                except:
                    is_good = False
                    #print('hgt not matching regex:',field,val)
            
    if is_good:
        #print('GOOD passport:\n', passport.keys(), '\n')
        count_valid += 1

    if not is_good:
        #print('BAD passport:\n', passport.keys(), '\n')
        count_invalid += 1


print('VALID:', count_valid)
print('INVALID:',count_invalid)
print('TOTAL:', count_valid + count_invalid)
