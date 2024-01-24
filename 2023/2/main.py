#! /bin/python3
import re 

file_input =""
with open("2023/2/input.txt") as f:
    file_input = f.read().splitlines()

t = 0
for val  in file_input:
    val  = val.split(": ")
    c= 1
    g= int(re.match("Game (\d*)",val[0]).groups()[0])

    val = val[1]
    for sub in val.split(";"):

        for i in sub.split(","):
            r =re.match("(\d*) (\w)",i.strip()).groups()
            if r[1] == 'r':
                if int(r[0]) > 12 :
                    c =0
        
            elif r[1] == 'b':
                if int(r[0])  > 13 :
                    c= 0
            else:
                if int(r[0]) > 14 :
                    c=0
    if c:
        print(g)
        t+=g

print(t)
