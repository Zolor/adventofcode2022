data = open("input.txt").read().split("\n")

score = 0

def resultCounter(intin):
    if intin == 88:
        return(1)
    elif intin == 89:
        return(2)
    else:
        return(3)

for line in data:
    op, me = line.split(" ")
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    if me == "X":
        if op == "A":
            me = "Z"
        elif op == "B":
            me = "X"
        elif op == "C":
            me = "Y"
    elif me == "Y":
        if op == "A":
            me = "X"
        elif op == "B":
            me = "Y"
        elif op == "C":
            me = "Z"
    elif me == "Z":
        if op == "A":
            me = "Y"
        elif op == "B":
            me = "Z"
        elif op == "C":
            me = "X"
    if ord(me) - ord(op) == 23:
        score += 3
    elif ord(me) - ord(op) == 21 or ord(me) - ord(op) == 24:
        score += 6
    score += resultCounter(ord(me))

print(score)