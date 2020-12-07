a = list(map(lambda x: x.split(", "), open("input7.txt", "r").read().replace("\n", "").replace("bags", "bag").split(".")))[:-1]
data = {}
for i in a:
    d = list()
    d.append(i[0].split("bag contain")[1][1:-4])
    for z in i[1:]:
        d.append(z[:-4])
    data[i[0].split("bag contain")[0][:-1]] = d

def num_count(number ,bag, data_):
    final = 0
    for i in bag:
        if i == "no other":
            break
        else:
            a = int(i[0:1]) * number
            final += a
            final += num_count(a, data_[i[2:]], data_)
    return final
print(num_count(1 ,data["shiny gold"], data))