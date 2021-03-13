import re

with open('7-1 input.txt') as file:
    data = file.read().split('\n')
    data = [re.split(', | contain ',x) for x in data]

REGEX0 = '(\w+ \w+)'
REGEXN = '(\d+) (\w+ \w+)'

class bag:
    def __init__(self, bag_type):
        # Every bag should know it's own type, and have a list of bag types it contains
        self.bag_type  = bag_type
        self.sub_bags  = []

    def add_sub_bag(self, sub_bag):
        self.sub_bags.append(sub_bag)

    def check_for_bag_type(self, bag_type, p=False):
        for sb in self.sub_bags:
            if sb.bag_type == bag_type:
                if p: print(f'\tFound that {self.bag_type} contains {bag_type}\n')
                return True
            else:
                if p: print(f'Checking if {self.bag_type}\'s sub-bag {sb.bag_type} contains {bag_type}')
                if sb.check_for_bag_type(bag_type):
                    if p: print(f'\tFound that {self.bag_type}\'s sub-bag {sb.bag_type} contains {bag_type}')
                    return True
            
        if p: print(f'\tDidn\'t find bag type {bag_type} in {self.bag_type}')
        return False

    def show_deets(self):
        print(f'{self.bag_type} contains: {[x.bag_type for x in self.sub_bags]}')
        

main_bags = [] # list of bags
sub_bags  = {} # dictionary of sub-bags for the main bag types

for item in data:
    # Get the main bag type
    main_bag_type = re.match(REGEX0, item[0]).group(0)
    main_bags.append(bag(main_bag_type))
    
    # Get the sub-bags
    sb_types = []
    try:
        sb_types = [re.match(REGEXN, x).groups()[1] for x in item[1:]]
    except: pass

    # Add the sub-bag types to the sbs dictionary
    sub_bags[main_bag_type] = sb_types


# Add all the sub bags to each main bag
for main_bag in main_bags:

    # For every sub-bag type for that main bag type (look into the dict)
    for sb_type in sub_bags[main_bag.bag_type]:
        
        # Get the bag object for that sub-bag type
        sb = None # need to fill in the sb bag obj

        # Look in the main_bags, get the bag object that matches the sub-bag type!
        for mb in main_bags:
            if mb.bag_type == sb_type:
                sb = mb

        # Add it to the current main bag's list
        main_bag.add_sub_bag(sb)


# CHECK: print the main bag and it's sub-bags for the first N bags
[mb.show_deets() for mb in main_bags[:10]]
print('\n')
        
# Check if the first bag has shiny gold
bt = 'shiny gold'
main_bags[0].check_for_bag_type(bt, p=True)
print('\n')

# Count all the bags that eventually have type bt
print(f"Total bags that contain {bt}: {sum([x.check_for_bag_type('shiny gold') for x in main_bags])}")


