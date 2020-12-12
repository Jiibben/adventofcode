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
answer = ""
while run:
    result = get_preamble_number(idx, preamble_length, data)
    if int(data[idx2]) in result:
        pass
    else:
        print(data[idx2])
        answer = int(data[idx2])
        run = False
        break
    idx += 1
    idx2 += 1

inde = 0
start_inde = 0
ui = 0
search = answer

while True:
    try:
        ui += int(data[inde])
        inde += 1
        if ui == search:
            break
        elif ui > search:
            raise IndexError("ERROR")
    except IndexError:
        ui = 0
        start_inde += 1
        inde = start_inde

ux = []
for n in range(start_inde, inde):
    ux.append(int(data[n]))

print(max(ux) + min(ux))