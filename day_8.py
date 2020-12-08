data = [i.split(" ") for i in open("input8test.txt", "r").read().split("\n")]

print(data)

repeat = True
add = 0
o = 0


def check_range(add, sign, current, range):
    if sign == "+":
        if current + add > range:
            return current - range + add
        else:
            return add
    elif sign == "-":
        return add


while repeat:
    print(o, add)
    try:
        operation, number = data[o]
    except:
        print(data)
        break
    if operation == "acc":
        print("acc")
        data[o] = ""
        o += check_range(1,"+", o, len(data))
        if number[0] == "-":
            add -= int(number[1:])
        elif number[0] == "+":
            add += int(number[1:])
    elif operation == "jmp":
        data[o] = ""
        print("jmp")
        if number[0] == "-":
            o -= check_range(int(number[1:]),"+", o, len(data))
        elif number[0] == "+":
            o += check_range(int(number[1:]), "-", o, len(data))
    elif operation == "nop":
        data[o] = ""
        print("nop")
        o += check_range(1, "+", o, len(data))
