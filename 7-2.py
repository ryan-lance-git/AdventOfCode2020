import re

with open('7-1 input.txt') as file:
    data = file.read().split('\n')
    data = [re.split(', | contain ',x) for x in data]

REGEX0 = '(\w+ \w+)'
REGEXN = '(\d+) (\w+ \w+)'

class bag:
    def __init__(self, bag_type):
        self.bag_type = bag_type
        self.sub_bags = {}

    def add_sub_bag(self, sb, sb_val):
        self.sub_bags[sb] = sb_val

    def check_for_bag_type(self, bag_type):
        for sb in self.sub_bags:
            if sb.bag_type == bag_type:
                return True
            elif sb.check_for_bag_type(bag_type):
                return True
        return False
    
    def check_num_sbs(self):

        if len(self.sub_bags) == 0:
            #print(f'No more sub-bags in {self.bag_type} returning 1')
            return 1

        else:
            count = 0
            for i, sb in enumerate(self.sub_bags):
                
                sbt = sb.bag_type
                num_sbt = self.sub_bags[sb]
                count += num_sbt * sb.check_num_sbs()
                
            return count + 1
        

    def show_deets(self):
        print(f'{self.bag_type} contains: {[(self.sub_bags[x], x.bag_type) for x in self.sub_bags]}')        


main_bags = [] # list of bags
sub_bags  = {} # dictionary of sub-bags for the main bag types
sub_vals  = {} # dictionary of the sub-bag values for the main_bags types

for item in data:
    # Get the main bag type
    main_bag_type = re.match(REGEX0, item[0]).group(0)
    main_bags.append(bag(main_bag_type))
    
    # Get the sub-bags (types) and the number of them (values)
    sb_types  = []
    sb_values = []
    try:
        sb_types  = [re.match(REGEXN, x).groups()[1] for x in item[1:]]
        sb_values = [re.match(REGEXN, x).groups()[0] for x in item[1:]]
    except: pass

    sub_bags[main_bag_type] = sb_types
    sub_vals[main_bag_type] = sb_values

# Add all the sub bags (and number of sub-bags) to each main bag
for i, main_bag in enumerate(main_bags):
    mbt = main_bag.bag_type
    
    for j, sb_type in enumerate(sub_bags[mbt]):

        # Get the sub-bag value. ith main bag, jth sub_bag
        sb_val = int(sub_vals[mbt][j])

        # Find the bag object which has the sb_type
        sb = None
        for mb in main_bags:
            if mb.bag_type == sb_type:
                sb = mb

        # Add the sub-bag and value to the current main bag
        main_bag.add_sub_bag(sb, sb_val)


# Part 1

# ~~~~~~~~~~~~~~~~
# CHECK: print the main bag and it's sub-bags for the first N bags
[mb.show_deets() for mb in main_bags[:10]]
print('\n')
        
# Check if the first bag has shiny gold
bt = 'shiny gold'
main_bags[0].check_for_bag_type(bt)
print('\n')

# Count all the bags that eventually have type bt
print(f"Total bags that contain {bt}: {sum([x.check_for_bag_type('shiny gold') for x in main_bags])}")
# ~~~~~~~~~~~~~~~~


# Part 2

# Find the object that is the shiny gold bag
for mb in main_bags:
    if mb.bag_type == bt:
        mybag = mb

print(f"Total bags that {bt} contains: {mybag.check_num_sbs() - 1}")









