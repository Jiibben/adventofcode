print([i for i in list(map(lambda x: int(x.replace("\n", "")), open("input.txt", "r").readlines())) if 2020 - i in list(map(lambda x: int(x.replace("\n", "")), open("input.txt", "r").readlines()))][0] * [i for i in list(map(lambda x: int(x.replace("\n", "")), open("input.txt", "r").readlines())) if 2020 - i in list(map(lambda x: int(x.replace("\n", "")), open("input.txt", "r").readlines()))][1])
