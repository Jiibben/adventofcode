data = [[i[0], int(i[1:])] for i in open("input12.txt", "r").read().splitlines()]

#data
curr = "E"
facing = {
    "E": 0,
    "S": 1,
    "W": 2,
    "N": 3
}
face = {
    0: "E",
    1: "S",
    2: "W",
    3: "N"
}

position = {
    "N":0,
    "E":0,
    "S":0,
    "W":0
}


def turn(current_face, lr, degree):
    if lr == "L":
        return face[int((facing[current_face] + (abs(360 - degree)/90))%4)]
    if lr == "R":
        return face[int((facing[current_face]+ (degree/90))%4)]

def forward(current_face, number, pos):
    pos[current_face] = pos[current_face] + number

def move(face, number, pos):
    pos[face] = pos[face] + number


for i in data:
    m = i[0]
    n = i[1]
    if m in ["N", "S", "W", "E"]:
        move(m, n, position)
    elif m in ["L", "R"]:
        curr = turn(curr, m, n)
    elif m == "F":
        forward(curr, n, position)

print((abs(position["E"]- position["W"])) + (abs(position["N"] - position["S"])))
