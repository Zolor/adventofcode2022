data = open("input.txt").readlines()

tmp = 0
biggest = 0

for line in data:
    if line == "\n":
        if tmp > biggest:
            biggest = tmp
        tmp = 0
    else:
        tmp += int(line)

print(biggest)
