with open("input.txt", "r") as f:
    d = f.readlines()
ex_report = list(map(lambda x: int(x.replace("\n", "")), d))


def find_sum(list_):
    found = False
    rep = 0
    while not found:
        a = list_[rep]
        for b in list_:
            if 2020 - (a + b) in ex_report:
                c = 2020 - (a + b)
                found = True
                return a * b * c
        rep += 1


print(find_sum(ex_report))
