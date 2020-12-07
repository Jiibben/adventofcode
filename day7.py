a = list(map(lambda x: x.split(", "), open("input7.txt", "r").read().replace("\n", "").split(".")))[:-1]
b = {}
for i in a:
    d = list()
    d.append(i[0].split("bags contain")[1][3:-5])
    for z in i[1:]:
        d.append(z[2:-5])
    b[i[0].split("bags contain")[0][:-1]] = d

"""mirrored plum
muted violet
dotted violet
dark green
dull gray
shiny fuchsia
dark aqua"""


not_found = True
while not_found:
    for z in b:
        if a in b.get(z):




