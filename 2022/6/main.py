#! /bin/python3

file_input =""
with open("2022/6/input.txt") as f:
    file_input = f.read()


for idx in range(len(file_input)-4):
    if len(set(file_input[idx:idx+4])) == 4 :
        print(idx+4)
        break

for idx in range(len(file_input)-14):
    if len(set(file_input[idx:idx+14])) == 14 :
        print(idx+14)
        break