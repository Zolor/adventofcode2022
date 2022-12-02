data = open("testinput.txt").read().split("\n")

Y = 1
X = 2
Z = 3
score = 0

for line in data:
    op, me = line.split(" ")
    if ord(me) - ord(op) == 23:
        score += 3
        if ord(me) == 88:
            score += 1
        elif ord(me) == 89:
            score += 2
        else:
            score += 3
    elif ord(me) - ord(op) > 23 or ord(me) - ord(op) < 22:
        score += 6
        if ord(me) == 88:
            score += 1
        elif ord(me) == 89:
            score += 2
        else:
            score += 3
    else:
        if ord(me) == 88:
            score += 1
        elif ord(me) == 89:
            score += 2
        else:
            score += 3
    print(score)

print(score)

#14858 is too high