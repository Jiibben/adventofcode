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
    cnt = 0
    for c in i["psw"]:
        if c == i["letter"]:
            cnt += 1
    if cnt >= i["min"] and cnt <= i["max"]:
        final += 1
print(final)
