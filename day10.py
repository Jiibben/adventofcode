import collections
data = [int(i) for i in open("input10test.txt").read().splitlines()]
data.append(max(data)+3)
data.sort()
def check_data(data_):
    start, one, three = 0, 0, 0
    while True:
        if start >= max(data_):
            break
        else:
            if start + 1 in data_:
                start +=1
                one +=1
            elif start + 3 in data_:
                three +=1
                start+=3
    return one * three


print(check_data(data))

def path(dat):
    cnt = collections.Counter()
    cnt[0] = last = 1
    for n in dat:
        cnt[n] = last = cnt[n - 1] + cnt[n - 2] + cnt[n - 3]
    return last

print(path(data))