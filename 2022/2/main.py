#! /bin/python3

file_input =""
with open("2022/2/input.txt") as f:
    file_input = f.read().splitlines()

# # 
# A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors


SCORE_CARD = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}
def give_score(other,me):
    if (other == 'A' and me =='X') or (other == 'B' and me =='Y') or (other == 'C' and me =='Z') :
        return 3 + SCORE_CARD[me]

    if (other == 'A' and me == 'Y') or (other == 'B' and me == 'Z') or (other == 'C' and me == 'X'):
        return 6 + SCORE_CARD[me]

    if (other == 'A' and me == 'Z' )or (other == 'B' and me == 'X') or (other == 'C' and me == 'Y'):
        return  SCORE_CARD[me]
    

    
score=0
for val in file_input:
    other , me = val.split(" ")
    print((other,me))
    score+=give_score(other,me)

print(score)