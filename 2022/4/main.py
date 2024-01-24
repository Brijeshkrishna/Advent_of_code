#! /bin/python3

file_input =""
with open("2022/4/input.txt") as f:
    file_input = f.read().splitlines()

def is_in_range(a,b,c):
    if c >= a and c<=b : return 1
    return 0

def is_in_bwt(a,b,c):
    if c<=b and c>=a: return 1
    return 0


def is_contained(a):
    a , b  = a[0] , a[1]
    a1,a2 =a.split("-")
    a1,a2 = int(a1),int(a2)
    
    b1,b2 =b.split("-")
    b1,b2 = int(b1),int(b2)

    return ((is_in_range(a1,a2,b1) and is_in_range(a1,a2,b2)) or is_in_range(b1,b2,a1) and is_in_range(b1,b2,a2)) or   is_in_bwt(a1,a2,b1) or is_in_bwt(b1,b2,a1)

count =  0
for val in file_input:
    count+=is_contained(val.split(","))
    print(val,count)
    
print(count)


# def part2(a):
#     a , b  = a[0] , a[1]
#     a1,a2 =a.split("-")
#     a1,a2 = int(a1),int(a2)
    
#     b1,b2 =b.split("-")
#     b1,b2 = int(b1),int(b2)

#     if a2 > b2 
#     return is_in_bwt(7,9,7) or is_in_bwt(7,9,7) 