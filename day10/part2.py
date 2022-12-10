data = open("input.txt").read().split("\n")

X = 1
counter = 0
crt = ""

def pixel_drawer():
    #print(X)
    pixels = []
    for y in range(X-1, X+2):
        pixels.append(y % 40)
    #print(pixels)
    if (counter-1) % 40 in pixels:
        return("#")
    else:
        return(".")

for line in data:
    counter += 1
   # print(counter)
    if counter in [41, 81, 121, 161, 201, 241]:            
        print(crt)
        crt = ""
    if line.startswith("noop"):
        crt += pixel_drawer()
        #print(crt, counter)
    elif line.startswith("addx"):      
        crt += pixel_drawer()
        counter += 1
        if counter in [41, 81, 121, 161, 201, 241]:
            print(crt)
            #print(crt, counter)
            crt = ""
        crt += pixel_drawer()
        #print(crt, counter)
        add = int(line.split(" ")[1])
        X += add
print(crt)

