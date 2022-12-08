data = open("testinput.txt").read().split("\n")

map = {}
count = 0

for y, l in enumerate(data):
    for x, r in enumerate(l):
        map[x,y] = int(r)
print(map.get((1,1)))

for k, v in map.items():
    if k[0] == 0 or k[0] == 4 or k[1] == 0 or k[1] == 4:
        count += 1
        continue
    #[1,1]
    elif map.get((k[0]-1,k[1])) > 


print(map)