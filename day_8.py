data = [i.split(" ") for i in open("input8.txt", "r").read().split("\n")]

def check_operator(index_add, current_index, list_):
    if (current_index + index_add) in list_:
        raise ValueError("repeated index:", current_index + index_add)
    else:
        list_.append(current_index+ index_add)
        return current_index + index_add
    

def accumulate(data):
    already_checked = list()
    accumulator, index = (0, 0)
    while True:
        try:
            operation = data[index][0]
            number = int(data[index][1])
            if operation == "nop":
                index = check_operator(1, index, already_checked)
                continue
            elif operation == "jmp":
                index = check_operator(number, index, already_checked)
                continue
            elif operation == "acc":
                index = check_operator(1, index,  already_checked)
                accumulator += number
                continue
            else:
                raise IndexError("something wrong happend")
        
        except ValueError as e:
            return accumulator

print(accumulate(data))