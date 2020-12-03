def getlist(file):
    d = open(file, "r").readlines()
    map_line = list(map(lambda x: x.replace("\n", ""), d))
    a = [[i * 1000] for i in map_line]
    return a


mape = getlist("input3.txt")
eny = 0
add = 0
run = 0
donnee = [1, 3, 5, 7]

try:
    for i in range(1, 400):
        if i % 2 == 0:
        eny += 1
            run += 1
        if mape[i][0][eny] == "#":
            add += 1
except IndexError:
    print("ran %s times " % run)
    print(add)
