data = open("input.txt").read().split("\n")
result = 0

for line in data:
    first, second = line.split(",")
    onestart, onestop = first.split("-")
    twostart, twostop = second.split("-")
    sectionone = [x for x in range(int(onestart),int(onestop)+1)]
    sectiontwo = [x for x in range(int(twostart),int(twostop)+1)]
    for n in sectionone:
        if n in sectiontwo:
            result += 1
            break

print(result)