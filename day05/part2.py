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
    #move 1[0] from 2[1] to 1[2]
    ints = [eval(x) for x in numbers]
    if ints[0] == 1:
        for _ in range(ints[0]):
            crates[ints[2]].append(crates[ints[1]].pop())
    else:
        tmp_lista = []
        for _ in range(ints[0]):
            tmp_lista.insert(0, crates[ints[1]].pop())
        for c in tmp_lista:
            crates[ints[2]].append(c)

result = ""
for x in range(len(crates)):
    result += crates[x+1].pop()

print(result)