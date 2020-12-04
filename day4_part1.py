from itertools import chain

valid = ["byr", "iyr", "eyr", "hgt", " hcl", "ecl", "pid"]

with open("input4.txt", "r") as f:
    a = f.readlines()

m = []
c = 0
d = 0
for i in a:
    if i == "\n":
        m.append(list(chain.from_iterable(list(map(lambda x: x.replace("\n", "").split(" ") if " " in x else [x.replace("\n", "")], a[d:c])))))
        d = c + 1
    c += 1


last = []
for x in m:
    abc = {
    "byr": None,
    "iyr": None,
    "eyr": None,
    "hgt": None,
    "hcl": None,
    "ecl": None,
    "pid": None,
    "cid": "eny"

}
    for n in x:
        
        if "byr" in n:
            abc["byr"] = n
        elif "iyr" in n:
            abc["iyr"] = n
        elif "eyr" in n:
            abc["eyr"] = n
        elif "hgt" in n:
            abc["hgt"] = n
        elif "hcl" in n:
            abc["hcl"] = n
        elif "ecl" in n:
            abc["ecl"] = n
        else:
            abc["cid"] = n
        last.append(abc)

print(len(last))


for f in last:
    if None in f.values():
        last.pop(last.index(f))

print(len(last))