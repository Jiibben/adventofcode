from itertools import combinations

data = [i for i in open("input9.txt", "r").read().split("\n")]
preamble_length = 25


def get_preamble_number(index, pb_length, dat):
    number = list()
    d = list()
    for i in range(index, index + pb_length):
        number.append(int(dat[i]))
    number = list(combinations(number, 2))
    for z in number:
        d.append(z[0] + z[1])

    return d


run = True
idx = 0
idx2 = preamble_length
while run:
    result = get_preamble_number(idx, preamble_length, data)
    if int(data[idx2]) in result:
        pass
    else:
        print(data[idx2])
        run = False
        break
    idx += 1
    idx2 += 1
