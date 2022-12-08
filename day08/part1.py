data = open("input.txt").read().split("\n")

map = {}
count = 0
max_x = 0
max_y = 0

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
        count += 1
        continue
    else:
        check = True
        for counter in range(0,k[0]):
            if map[counter,k[1]] < v:
                if k[0] - counter == 1:
                    count += 1
                    print(k, v, 1)
                    check = False
                    break
            else:
                break
        if check == True:
            for counter in range(k[0]+1,max_x+1):
                if map[counter,k[1]] < v:
                    if counter == max_x:
                        count += 1
                        print(k, v, 2)
                        check = False
                        break
                else:
                    break
        if check == True:
            for counter in range(0,k[1]):
                if map[k[0],counter] < v:
                    if k[1] - counter == 1:
                        count += 1
                        print(k, v, 3)
                        check = False
                        break
                else:
                    break
        if check == True:
            for counter in range(k[1]+1,max_y+1):
                if map[k[0],counter] < v:
                    if counter == max_y:
                        count += 1
                        print(k, v, 4)
                        check = False
                        break
                else:
                    break

print(count)
#Too low