#! /bin/python3

file_input =""
with open("2022/1/input.txt") as f:
    file_input = f.read().split("\n")
    
calories =0
max_elf = []

for idx,val in enumerate(file_input):
    if val == '':
        max_elf.append(calories)
        calories = 0
    else:
        calories+=int(val)
max_elf.append(calories)

max_elf.sort()
print(max(max_elf))
print(sum(max_elf[-3:]))

# 72070