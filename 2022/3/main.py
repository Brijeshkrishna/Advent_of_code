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
    return get_code(list(com2.intersection(com1))[0])
  

score = 0
for val in file_input:
    score+=find_common(val)

print(score)

# 7990

sum_score =0 
for idx in range(0,len(file_input),3):
    sum_score +=get_code(list(set(file_input[idx]).intersection(set(file_input[idx+1])).intersection(set(file_input[idx+2])))[0])
print(sum_score)