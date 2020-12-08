data = [i.split(" ") for i in open("input8.txt", "r").read().split("\n")]

def check_operator(index_add, sign, current_index, list_):
    if sign == "+":
        if (current_index + index_add) in list_:
            raise ValueError("repeated index:", current_index + index_add)
        else:
            list_.append(current_index+ index_add)
            return current_index + index_add
    elif sign == "-":
        if (current_index - index_add) in list_:
            list_.append(current_index - index_add)
            raise ValueError("repeated index:", current_index - index_add)
        else:
            return current_index - index_add

already_checked = list()
accumulator = 0
index = 0
while True:
    try:
        operation = data[index][0]
        number = int(data[index][1][1:])
        sign = data[index][1][0]
        if operation == "nop":
            index = check_operator(1, "+", index, already_checked)
            continue
        elif operation == "jmp":
            index = check_operator(number, sign, index, already_checked)
            continue
        elif operation == "acc":
            index = check_operator(1, "+", index,  already_checked)
            if sign == "-":
                accumulator -= int(number)
            elif sign == "+":
                accumulator += number
            continue
        else:
            raise IndexError("something wrong happend")
    
    except ValueError as e:
        print(e)
        print(accumulator)
        break
