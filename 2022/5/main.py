#! /bin/python3

file_input = ""
with open("2022/5/input.txt") as f:
    file_input = f.read().splitlines()


def parse_stack(s: str, line_no: int):
    data = {}
    for i in s[line_no].split("  "):
        data[i.strip()] = []

    i = line_no - 1
    while i >= 0:
        staks = list(s[i])
        idx = 1
        for j in range(1, len(staks), 4):
            if s[i][j] != " ":
                data[str(idx)].append(s[i][j])
            idx += 1
        i -= 1
    return data


def get_line(file):
    init_idx = 0
    for i in file_input:
        if i == "":
            break
        init_idx += 1
    return init_idx

def parse_move(file_data):
    data = []
    for val in file_data[1:]:
        t = val.split(" ")
        data.append([int(t[1]), int(t[3]), int(t[5])])
    return data


def move(inti, data):
    for i in data:
        for _ in range(i[0]):
            t = inti[str(i[1])].pop()
            inti[str(i[2])].append(t)

def get_code(init):
    r = ""
    for val in init.values():
        r += val.pop()
    return r


file_no = get_line(file_input)
init = parse_stack(file_input, file_no - 1)
data = parse_move(file_input[file_no:])

move(init, data)
print(get_code(init))

# BZLVHBWQF