def getlist(file):
    d = open(file, "r").readlines()
    map_line = list(map(lambda x: x.replace("\n", ""), d))
    return map_line


a = getlist("input3.txt")


def move(x, y, map):
    b = 0
    c = 0
    lol = y
    for i in map:
        if b + x >= len(i):
            b = b - len(i)
        b += x
        if i[b] == "#":
            c += 1

    return c

print(move(3, 1, a))