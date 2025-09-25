import math
from collections import Counter

def calc_perms(name):
    name = name.lower()
    name_len = len(name)
    if name_len <= 1:
        return {name}
    
    perms = set()

    for i in range(name_len):
        curr_char = name[i]
        remaining = name[:i] + name[i+1:]

        for perm in calc_perms(remaining):
            perms.add(curr_char + perm)

    return perms

user_input = input("Enter a name: ")
unique_perms = calc_perms(user_input)

print(f"Number of unique permutations of '{user_input}': {len(unique_perms)}")