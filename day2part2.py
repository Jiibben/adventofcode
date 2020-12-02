with open("input2.txt", "r") as f:
    d = f.readlines()
ex_report = list(map(lambda x: x.replace("\n", ""), d))

c = []
final = 0
for i in ex_report:
    count, psw = i.split(":")
    range_, letter = count.split(" ")
    min, max = range_.split("-")
    b = {"min": int(min),
         "max": int(max),
         "letter": letter,
         "psw": psw
         }
    c.append(b)

for i in c:
    if i["letter"] == i["psw"][(i["min"])] and not i["letter"] == i["psw"][(i["max"])] or (i["letter"] == i["psw"][(i["max"])] and not i["letter"] == i["psw"][(i["min"])]):
        final += 1

print(final)
