data = open("input.txt").read().split("\n")

map = {}
max_x = 0
max_y = 0
result = {}

for y, l in enumerate(data):
    for x, r in enumerate(l):
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
        map[x,y] = int(r)
print(max_y)
print(max_x)
for k, v in map.items():
    if k[0] == 0 or k[0] == max_x or k[1] == 0 or k[1] == max_y:
        continue
    else:
        result.update({k:1})
        count = 0
        for counter in range(k[0]-1,-1,-1):
            if map[counter,k[1]] < v:
                count += 1
            else:
                count += 1
                break
        result[k] *= count
        count = 0
        for counter in range(k[0]+1,max_x+1):
            if map[counter,k[1]] < v:
                count += 1
            else:
                count += 1
                break
        result[k] *= count
        count = 0
        for counter in range(k[1]-1,-1,-1):
            if map[k[0],counter] < v:
                count += 1
            else:
                count += 1
                break
        result[k] *= count
        count = 0
        for counter in range(k[1]+1,max_y+1):
            if map[k[0],counter] < v:
                count += 1
            else:
                count += 1
                break
        result[k] *= count
print(result)
print(max(result.values()))

#1404 Too low