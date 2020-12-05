from itertools import chain
import re
with open("input4.txt", "r") as f:
    a = f.readlines()

passeport_list = []
c = 0
d = 0
for i in a:
    if i == "\n":
        passeport_list.append(list(chain.from_iterable(list(map(lambda x: x.replace("\n", "").split(" ") if " " in x else [x.replace("\n", "")], a[d:c])))))
        d = c + 1
    c += 1

def remove_invalid(psp_list):
    for psp in psp_list:
        for element in psp:
            if re.match('^cid\D', element):
                psp.pop(psp.index(element))


    return list(filter(lambda x: len(x) ==7, psp_list))


passeport_check = remove_invalid(passeport_list)


def is_psp_valid(psp):
    for i in psp:
        if re.match('^hcl\D', i):
            if not re.fullmatch('hcl\D#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', i):
                return False
        elif re.match('^pid\D', i):
            if not re.fullmatch('pid\D\d\d\d\d\d\d\d\d\d', i):
                return False
        elif re.match('^iyr\D', i):
            t = int(i.split(":")[1])
            if t < 2010 or t > 2020:
                return False
        elif re.match('^eyr\D', i):
            z = int(i.split(":")[1])
            if z < 2020 or z > 2030:
                return False
        elif re.match('^ecl\D', i):
            k = i.split(":")[1]
            if k not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                return False
        elif re.match('^byr\D', i):
            q = int(i.split(":")[1])
            if q < 1920 or q > 2002:
                return False
        elif re.match('^hgt\D', i):
            z = i.split(":")[1]
            ki = z.strip("0123456789")
            if ki == "in":
                b = int(z.strip("in"))
                if b < 59 or b > 76:
                    return False
            elif ki == "cm":
                u = int(z.strip("cm"))
                if u < 150 or u > 193:
                    return False
            elif ki == "":
                return False
    return True

print(len(list(filter(is_psp_valid, passeport_check))))

