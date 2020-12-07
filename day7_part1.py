a = list(map(lambda x: x.split(", "), open("input7.txt", "r").read().replace("\n", "").replace("bags", "bag").split(".")))[:-1]
data = {}
for i in a:
    d = list()
    d.append(i[0].split("bag contain")[1][3:-4])
    for z in i[1:]:
        d.append(z[2:-4])
    data[i[0].split("bag contain")[0][:-1]] = d


def contains(dict, key, value):
    if value in dict[key]:
        return key
    else:
        return None
# for u in b:
#     print(u, b.get(u))

def check_possibilites(dict_):
    k = set()
    f_list = ["shiny gold"]
    while len(f_list) != 0:
        for i in f_list:
            f_list.pop(f_list.index(i))
            for z in dict_:
                n = contains(dict_, z ,i)
                if n:
                    f_list.append(n)
                    k.add(n)

    return len(k)



print(check_possibilites(data), end="")

