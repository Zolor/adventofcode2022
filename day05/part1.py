import re
data = open("input.txt").read().split("\n")
tmpcrates = []
instructions = []
breaker = 0
for line in data:
    if line == "":
        breaker = 1
    elif breaker == 1:
        instructions.append(line)
    else:
        tmpcrates.append(line)

counter = 0
crates = {}
for line in tmpcrates:
    cargospace = 1
    counter = 0
    for space in line:
        counter += 1
        if ord(space) <= 90 and ord(space) >=65:
            if cargospace in crates:
                crates[cargospace].append(space)
            else:
                crates[cargospace] = []
                crates[cargospace].append(space)
        if counter == 4:
            cargospace += 1
            counter = 0

for k, v in crates.items():
    v = v.reverse()

for line in instructions:
    numbers = re.findall(r'\d+', line)
    ints = [eval(x) for x in numbers]
    for _ in range(ints[0]):
        crates[ints[2]].append(crates[ints[1]].pop())

result = ""
for x in range(len(crates)):
    result += crates[x+1].pop()

print(result)