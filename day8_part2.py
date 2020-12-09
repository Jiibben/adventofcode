from datetime import datetime

data = [i.split(" ") for i in open("input8.txt", "r").read().split("\n")]

t0 = datetime.now().microsecond
already_checked = list()
accumulator, index = (0, 0)
found = True
d = data.copy()
round = 0

def find_index(list_, item):
    indexes = list()
    for i in range(0, len(list_)):
        if list_[i][0] == item:
            indexes.append(i)
    return indexes

c = find_index(data, "jmp")
while found:
    data[c[round]] = ["nop", data[c[round]][1]]
    while True:
        try:
            operation = data[index][0]
            number = int(data[index][1])
            if operation == "nop":
                if (index + 1) not in already_checked:
                    index +=1
                    already_checked.append(index)
                else:
                    break
            elif operation == "jmp":
                if (index + number) not in already_checked:
                    index += number
                    already_checked.append(index)
                else:
                    break
            elif operation == "acc":
                if (index + 1) not in already_checked:
                    index +=1
                    already_checked.append(index)
                    accumulator += number
                else:
                    break
        except IndexError:
            print(accumulator)
            t1 = datetime.now().microsecond
            found = False
            break
    index = 0
    accumulator = 0
    already_checked = []
    round += 1
    data = d.copy()

    
print(t1-t0)
