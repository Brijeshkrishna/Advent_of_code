#! /bin/python3

import time


file_input =""
with open("2022/7/input.txt") as f:
    file_input = f.read().splitlines()

def parse_line(s:str):
    size , file = s.split(' ')
    if (size == "dir"):
        size = 0
    return (file,int(size))

def clear_path(s:str):
    s = s.split('/')[1:]
    idx = 0
    while idx<len(s)-1:
        if s[idx+1] != '..':
            idx+=1
            continue
        s = s[:idx] + s[idx+2:]
        idx = 1
    return s



def set_to_path(main,current:str):
    current  = current.split('/')
    for i in current:
        if i == '':
            main = main['/']
        else:
            main = main[str(i)]
    return main

# current = "/"
# directory = {}
# file_input = file_input[1:]
# line_no = 1

# while (line_no<len(file_input)):
#     if file_input[line_no] == "$ ls":
#         files = {}
#         while file_input[line_no].startswith("$ cd"):
#             f,s = parse_line(file_input[line_no])
#             files[f] = s
#             line_no+=1
#         directory[current] =files
#         line_no-=1

#         path = file_input[line_no].split(" ")[-1]
#         current+=path
