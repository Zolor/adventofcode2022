data = open("input.txt").read().split("\n")
data = str(data[0])
start = 0
stop = 4
solution = True
while solution == True:
    tmp_str = ""
    for i in range(start,stop):
        tmp_str += data[i]
        print(tmp_str)
    counter = 0
    for x, y in enumerate(tmp_str):
        if tmp_str.count(y) >= 2:
            break
        elif counter == 3:
            print(tmp_str)
            print(stop)
            solution = False
            break
        else:
            counter += 1
    start += 1
    stop += 1
    if start + 1 == len(data):
        solution = False

#16,17 is wrong