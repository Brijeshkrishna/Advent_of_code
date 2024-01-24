#! /bin/python3

file_input = ""
with open("2023/1/input.txt") as f:
    file_input = f.read().splitlines()


VALID_DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def replacer_r(s: str):
    idx=len(s)-1
    while idx >= 0:        
        if s[idx].isdigit() :
            return s  
        t = s[idx -5: idx ]
        for val in VALID_DIGIT:
            t = t.replace(val, str(VALID_DIGIT[val]))
        s = s[:idx] + t + s[idx + 5 :]
        idx -= 1
    return s



def replacer(s: str):
    idx=0
    while idx < len(s):        
        if s[idx].isdigit() :
            return replacer_r(s)    
        t = s[idx : idx + 5]
        for val in VALID_DIGIT:
            t = t.replace(val, str(VALID_DIGIT[val]))
        s = s[:idx] + t + s[idx + 5 :]
        idx += 1
    return s


def is_int(i):
    return (ord(i) - ord("0")) <= 9


def find_digit(v: str):
    digit = []
    for val in v:
        if is_int(val):
            digit.append(val)

    if len(digit) == 0:
        return 0

    return int(digit[0] + digit[-1])


sums = 0
for val in file_input:
    print(find_digit(replacer(val)))
    # sums += find_digit(replacer(val))
# print(sums)
# 54627 - 55773

# print(replacer("9eightszgdhftggrktkzbsmnhtwonekh"))