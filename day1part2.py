with open("input.txt", "r") as f:
    d = f.readlines()
ex_report = list(map(lambda x: int(x.replace("\n", "")), d))


def permute(list, s):
    if list == 1:
        return s
    else:
        return [str(y) + " " + str(x)
                for y in permute(1, s)
                for x in permute(list - 1, s)
                ]


def permuting(list, s):
    if list == 1:
        return s
    else:
        return [x + y for y in permuting(1, s) for x in permuting(list - 1, s)
                ]


a = permute(3, ex_report)
b = permuting(3, ex_report)

for i in b:
    if i == 2020:
        c = a[b.index(i)]
        break

print(c)
