#! /bin/python3

file_input =""
with open("2022/1/input.txt") as f:
    file_input = f.read().split("\n")
    
calories =0
max_elf = 0

for idx,val in enumerate(file_input):
    if val == '':
        if calories > max_elf:
            max_elf = calories
        calories = 0
    else:
        calories+=int(val)
        
print(max_elf)
