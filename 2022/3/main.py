#! /bin/python3

file_input =""
with open("2022/3/input.txt") as f:
    file_input = f.read().splitlines()


def get_code(alp:str):
    if alp.isupper() :
        return ord(alp) - 38
    return ord(alp) - 96

def find_common(s:str):
    com1 = set(s[:int(len(s)/2)])
    com2 = set(s[int(len(s)/2) : ])
    print(com1,com2)
    return get_code(list(com2.intersection(com1))[0])
  

score = 0
for val in file_input:
    score+=find_common(val)

print(score)

# 7990