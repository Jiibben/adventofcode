with open("input.txt", "r") as f:
    d = f.readlines()
ex_report = list(map(lambda x:int(x.replace("\n", "")), d))
rep = 0
a = ex_report[rep]
found = False
while not found:
    rep += 1
    for i in ex_report:
        d = a + i
        if d == 2020:
            print("The answer is {}".format(a*i))
            found = True
            break
    a = ex_report[rep]
