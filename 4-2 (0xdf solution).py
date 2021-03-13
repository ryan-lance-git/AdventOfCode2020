import re


keys = {
    "byr": r"byr:\s*(19[2-9]\d|200[0-2])\b",  # (Birth Year) - four digits; at least 1920 and at most 2002.
    "iyr": r"iyr:\s*20(1\d|20)\b",  # (Issue Year) - four digits; at least 2010 and at most 2020.
    "eyr": r"eyr:\s*20(2\d|30)\b",  # (Expiration Year) - four digits; at least 2020 and at most 2030.
    "hgt": r"hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",  # (Height) - a number followed by either cm or in:
    # "If cm, the number must be at least 150 and at most 193.
    # "If in, the number must be at least 59 and at most 76.
    "hcl": r"hcl:\s*#[0-9a-f]{6}\b",  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "ecl": r"ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b",  # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "pid": r"pid:\s*\d{9}\b",  # (Passport ID) - a nine-digit number, including leading zeroes.
    # "cid", # (Country ID) - ignored, missing or not.
}

with open('4-1 input.txt') as f:
    passports = f.read().split("\n\n")

num_keys_valid = sum([all([k in p for k in keys]) for p in passports])
print(f"Part 1: {num_keys_valid}")

num_data_valid = sum([all([re.search(keys[k], p) for k in keys]) for p in passports])
print(f"Part 2: {num_data_valid}")
