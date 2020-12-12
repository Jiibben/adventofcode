def adjacent(v, x, y):
    total = 0
    offsets = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ]
    for d in offsets:
        dx = x + d[0]
        dy = y + d[1]
        while dy >= 0 and dy < len(v) and dx >= 0 and dx < len(v[dy]) and v[dy][dx] == '.':
            dx += d[0]
            dy += d[1]
        if dy >= 0 and dy < len(v) and dx >= 0 and dx < len(v[dy]):
            total += (v[dy][dx] == "#")
    return total

def taken(v):
    total = 0
    for x in v:
        total += x.count("#")
    return total

with open("input11.txt") as file:
    data = file.read().split("\n")

for t in range(199):
    next = []
    a = 0
    for y in range(len(data)):
        string = ""
        for x in range(len(data[y])):
            a += 1 
            character = data[y][x]
            if character != '.':
                occupants = adjacent(data, x, y)
                if character == "L" and occupants == 0:
                    character = "#"
                elif character == "#" and occupants >= 5:
                    character = "L"
            string += character
        next.append(string)
    data = next
print(taken(data))