import re
from itertools import product
data = open("day14.txt", "r").read().splitlines()

def apply_mask(mask, bit):
    bit_list = [i for i in bit]
    for i in enumerate(mask):
        index, val = i
        if val == "X":
            pass
        else:
            bit_list[index] = val
    return "".join(bit_list)

def calculate_val(bit):
    return int(bit, 2)

def find_memadress(address):
    pattern = re.compile(r"\d")
    result = pattern.findall(address)
    return int("".join(result))

def to_binary(num):
    return ('{0:036b}'.format(num))

def find_indexes(string, char):
    indexes = list()
    for i in range(0, len(string)):
        if string[i] == char:
            indexes.append(i)
    return indexes

def apply_mask2(mask, bit):
    eny = list(bit)
    indexes = find_indexes(mask, "X")
    a = list(product("10", repeat=len(indexes)))
    final = list()
    for i in range(0,len(eny)):
        if mask[i] == "1":
            eny[i] = "1"
        elif mask[i] == "0":
            pass
    for x in a:
        for i in range(0,len(indexes)):
            eny[indexes[i]] = x[i]
            final.append("".join(eny))
    return [calculate_val(i) for i in set(final)]

def solve1(data):
    curr_mask = ""
    memory = {}
    for i in data:
        x,y = i.split(" = ")
        if x == "mask":
            curr_mask = y
        else:
            memory[find_memadress(x)] = int(apply_mask(curr_mask, to_binary(int(y))), 2)

    return sum(list(memory.values()))

def solve2(data):
    curr_mask = ""
    memory = {}
    for i in data:
        x,y = i.split(" = ")
        if x == "mask":
            curr_mask = y
        else:
            for z in apply_mask2(curr_mask, to_binary(find_memadress(x))):
                memory[z] = int(y)

    return sum(list(memory.values()))

print(solve1(data))
print(solve2(data))