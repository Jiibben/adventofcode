def getlist(file):
    d = open(file, "r").readlines()
    map_line = list(map(lambda x: x.replace("\n", ""), d))
    return map_line


a = getlist("input3.txt")
search = {
    "right": [1, 3, 5, 7, 1],
    "down": [1, 1, 1, 1, 2]
}


def move(x, y, mape):
    b = 0
    c = 0

    if y == 1:
        for i in mape:
            if b + x > len(i):
                b = b - len(i)
            if i[b] == "#":
                c += 1
            b += x
        return c
    elif y > 1:
        eny = list(filter(lambda e: mape.index(e) % 2 == 0, mape))
        for i in eny:
            if b + x > len(i):
                b = b - len(i)
            if i[b] == "#":
                c += 1
            b += x
        return c


result = 1
for z, w in zip(search["right"], search["down"]):
    result *= (move(z, w, a))
print(result)
