data = open("testinput.txt").readlines()

tmp = 0
biggest = []

for line in data:
    if line == "\n":
        biggest.append(tmp)
        tmp = 0
    else:
        tmp += int(line)
biggest.sort()
print(biggest[-1] + biggest[-2] + biggest[-3])