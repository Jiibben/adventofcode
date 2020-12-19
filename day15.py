starting = [0, 3, 6]
spoken = []
run = 0
while run < 2020:
    last = starting[-1]
    if last not in starting:
        starting.append(0)
    elif last in spoken():
        