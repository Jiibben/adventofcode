import itertools
import string
def part1(file):
    total = 0
    d = []
    g = []
    c = [i.replace("\n", "") for i in open(file,"r")]
    for i in c:
        if i != "":
            d.append(list(i))
        if i == "":
            g.append(list(set(itertools.chain.from_iterable(d))))
            d = []
    for i in g:
        total += len(i)
    return total


def part2(file):
    total = 0
    d = []
    g = []
    c = [i.replace("\n", "") for i in open(file,"r")]
    for i in c:
        if i != "":
            d.append(list(i))
        if i == "":
            g.append(d)
            d = []
    return g


def check_group_dec(liste_of_list):
    d = list(string.ascii_lowercase)
    for x in string.ascii_lowercase:
        for i in liste_of_list:
            if x in i:
                pass
            elif x not in i:
                d.pop(d.index(x))
                break
    return len(d)

tot = 0
for i in part2("input6.txt"):
    tot += check_group_dec(i)

print(tot)