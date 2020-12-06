import itertools
import datetime

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
    return list(map(lambda d: [list(i) for i in d], map(lambda x: x.split("\n"), data)))
    
print(part2(groups))
