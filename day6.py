import itertools
import datetime
from string import ascii_lowercase
groups = [line for line in open("input6.txt", "r").read().split("\n\n")]

def timer(f):
    def wrapper(*kwargs):
        t1 = datetime.datetime.now().microsecond
        x = f(*kwargs)
        t2 = datetime.datetime.now().microsecond
        print("Function named %s took %s microsecond to run" % (f.__name__, t2-t1))
        return x
    return wrapper

@timer
def part1(data):
    return list(itertools.accumulate(list(map(lambda x: len(set(itertools.chain.from_iterable(x.split("\n")))), data))))[-1]

@timer
def part2(data): 
    tot = 0
    def check_group_dec(liste_of_list):
        d = list(ascii_lowercase)
        for x in ascii_lowercase:
            for i in liste_of_list:
                if x in i:
                    pass
                elif x not in i:
                    d.pop(d.index(x))
                    break
        return len(d)
    for i in map(lambda x: x.split("\n"), data):
        tot += check_group_dec(i)
    return tot

print(part1(groups))
print(part2(groups))
