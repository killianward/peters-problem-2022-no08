# Peter's Problem 2022 No.8

from itertools import product

possible_nums = list(range(1, 195))

def check(prod):
    num_of_tables = prod[0]
    num_of_chairs = prod[1]
    if num_of_chairs == num_of_tables * 3:
        if (570 - (((num_of_chairs / 3) * 2) * 2)) - (num_of_tables * 3) - (num_of_chairs * 4) == 0:
            return True
        else:
            return False
    else:
        return False

for prod in list(product(possible_nums, repeat=2)):
    if check(prod):
        print(f"Number of chairs: {prod[1]}")
