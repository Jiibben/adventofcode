def getlist(file):
    d = open(file, "r").readlines()
    map_line = list(map(lambda x: x.replace("\n", ""), d))
    return map_line


a = getlist("input3.txt")
search = {
    "right": [1, 3, 5, 7, 1],
    "down": [1, 1, 1, 1, 2]
}


def move(x, y, map):
    b = 0
    c = 0

    for i in map:
        if b + x > len(i):
            b = b - len(i)
        if map.index(i) % y == 0 and map.index(i) != 0:

            if i[b] == "#":
                c += 1
        b += x
    return c


result = []
for z, w in zip(search["right"], search["down"]):
    result.append(move(z, w, a))

print(result)
mac = 1
for t in result:
    mac = t * mac
print(mac)
