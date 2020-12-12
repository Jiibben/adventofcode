def adjacent(dat, x, y):
    total = 0
    square = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for b in square:
        xa = y + b[0]
        ya = x + b[1]
        if ya >= 0 and ya < len(dat) and xa >= 0 and xa < len(dat[ya]):
            total += (dat[ya][xa] == "#")
    return total

def taken(v):
    total = 0
    for x in v:
        total += x.count("#")
    return total

with open("input11.txt") as file:
    data = file.read().split("\n")

for t in range(500):
    next = []
    for d in range(len(data)):
        string = ""
        for z in range(len(data[d])):
            character = data[d][z]
            if character != '.':
                occupants = adjacent(data, d, z)
                if character == "L" and occupants == 0:
                    character = "#"
                elif character == "#" and occupants >= 4:
                    character = "L"
            string += character
        next.append(string)
    data = next
print(taken(data))