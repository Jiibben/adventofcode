#! /usr/bin/python3
from math import floor, ceil
def getlist(file):
    arranged_data = []
    lines = list(map(lambda x: x.replace("\n", ""), open(file, "r").readlines()))
    for i in lines:
        arranged_data.append(
            {
                "row":i[0:-3],
                "column":i[-3:]
            }
        )
    return arranged_data

def get_seat_id(rows, column):
    y = [0, 127]
    x = [0, 7]
    for letter in rows:
        
        if letter =="F":
            y[1] = y[1] - ceil((y[1] - y[0]) / 2)
        elif letter =="B":
            y[0] = y[0] + ceil((y[1] - y[0]) /2)
    
    for l in column:
        if l =="L":
            x[1] = x[1] - ceil((x[1] - x[0]) / 2)
        elif l =="R":
            x[0] = x[0] + ceil((x[1] - x[0]) /2)

    return y[0] * 8 + x[0]

# create list of seats id from boarding passes
a = []
for i in getlist("input5.txt"):
    a.append(get_seat_id(i["row"], i["column"]))

# part 1 

print("answer 1 is: ", max(a))

# part 2
def find_bdpass(bdpass_list):
    for i in range(0, max(bdpass_list)):
        if i not in bdpass_list and i + 1 in bdpass_list and i - 1 in bdpass_list:
            return i

print("answer 2 is: ", find_bdpass(a))