from itertools import chain

valid = ["byr", "iyr", "eyr", "hgt", " hcl", "ecl", "pid"]

with open("/Users/allanburnier/PycharmProjects/adventofcode/input4.txt", "r") as f:
    a = f.readlines()

m = []
c = 0
d = 0

for i in a:
    if i == "\n":
        m.append(list(map(lambda x: x.replace("\n", "").split(" ") if " " in x else [x.replace("\n", "")], a[d:c])))
        d = c + 1
    c += 1

print(m)