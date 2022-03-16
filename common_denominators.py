

lst = [[1, 2], [1, 3], [1, 4]]

'''

# 1st solution -> Gives a large number

    1 (4*3)    1(4*2)     1(2*3)
    -   +      -  +       -  +
    2 (4*3)    3(4*2)     4(2*3)

    ----> 12/24 + 8/24 + 6/24

# 2nd solution -> LCM
    using the least common multiple (LCM)

# 3rd approach -> LCM
    using math library

'''


def LCM(fracs: list): # returns multiplyers = index + 1 and lcm
    if lst == []:
        return [None, None]

    denominators = [fracs[elem][-1] for elem in range(len(fracs))]
    valids = [0]*(len(denominators))
    list_multiplyer = [1]*(len(denominators))

    table = []
    multiplyer = 1
    while True:
        table.append([])
        # create multiplication table
        for i in range(len(denominators)):
            table[multiplyer-1].append(denominators[i] * multiplyer)
        
        # Backtrack finds current minimum in each row of table
        to_find_idx = table[-1].index(min(table[-1]))
        lcm = table[-1][to_find_idx]
        list_multiplyer[to_find_idx] = multiplyer
        valids[to_find_idx] = 1

        for i in range(len(table)-1, 0, -1):
            if lcm in table[i-1]:
                index = table[i-1].index(lcm)
                list_multiplyer[index] = i
                valids[index] = 1
        
        if valids == [1]*(len(denominators)):
            return [list_multiplyer, lcm]
        else:
            list_multiplyer = [1]*(len(denominators))
            valids = [0]*(len(denominators))

        multiplyer += 1

def convert_fracts_ap2(lst): # using the 2nd approach
    multiplyer, lcm = LCM(lst)
    for i in range(len(lst)):
        lst[i][0] *= multiplyer[i]
        lst[i][1] = lcm
    return lst


import math
# Works only in version 3.9 and above
def convert_fracts_ap3(lst): # using the 3rd approach
    denominators = [lst[elem][-1] for elem in range(len(lst))]
    lcm = math.lcm(*denominators)
    for i in range(len(lst)):
        lst[i][0] *= lcm//lst[i][1]
        lst[i][1] = lcm
    return lst


import numpy as np
# for version 3.8 and below
def convert_fracts_ap3_1(lst): # using the 3rd approach
    if lst == []: return lst
    denominators = [lst[elem][-1] for elem in range(len(lst))]
    lcm = np.lcm.reduce(denominators)
    for i in range(len(lst)):
        lst[i][0] *= lcm//lst[i][1]
        lst[i][1] = lcm
    return lst


print(convert_fracts_ap3_1(lst))
