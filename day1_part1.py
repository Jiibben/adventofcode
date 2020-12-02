def lfromfile(file):
    return list(map(lambda x: int(x.replace("\n", "")), open(file,"r").readlines()))

def find_sum(list_):
    for i in list_:
        if 2020 - i in list_:
            return i * (2020-i)

print(find_sum(lfromfile("input.txt")))

