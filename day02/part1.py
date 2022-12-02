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
    if ord(me) - ord(op) == 23:
        score += 3
    elif ord(me) - ord(op) == 21 or ord(me) - ord(op) == 24:
        score += 6
    score += resultCounter(ord(me))

print(score)

#13682