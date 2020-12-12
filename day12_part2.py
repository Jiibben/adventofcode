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
waypoint = {
    "N":1,
    "E":10,
    "S":0,
    "W":0
}
def move_waypoint(face, number, way):
    way[face] = way[face] + number

def rotate_waypoint(side, degree, way):
    if side =="R":
        for i in range(0, int(degree /90)):
            waypt = way.copy()
            way["N"] = waypt["W"]
            way["E"] = waypt["N"]
            way["S"] = waypt["E"]
            way["W"] = waypt["S"]
    if side =="L":
        for i in range(0, int((abs(360 - degree)) /90)):
            waypt = way.copy()
            way["N"] = waypt["W"]
            way["E"] = waypt["N"]
            way["S"] = waypt["E"]
            way["W"] = waypt["S"]

def forward(number, pos, way):
    pos["W"] = pos["W"] + int(way["W"] * number)
    pos["E"] = pos["E"] + int(way["E"] * number)
    pos["S"] = pos["S"] + int(way["S"] * number)
    pos["N"] = pos["N"] + int(way["N"] * number)


for i in data:
    m = i[0]
    n = i[1]
    if m in ["N", "S", "W", "E"]:
        move_waypoint(m, n, waypoint)
    elif m in ["L", "R"]:
        curr = rotate_waypoint(m, n, waypoint)
    elif m == "F":
        forward(n, position, waypoint)

print((abs(position["E"]- position["W"])) + (abs(position["N"] - position["S"])))
