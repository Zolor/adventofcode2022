data = open("input.txt").read().split("\n")

X = 1
result = 0
counter = 0
for line in data:
    counter += 1
    if counter in [20, 60, 100, 140, 180, 220]:
            result += counter * X
            print(counter, X, result, "first")
    if line.startswith("addx"):
        counter += 1
        if counter in [20, 60, 100, 140, 180, 220]:
            result += counter * X
            print(counter, X, result, "second")
        add = line.split(" ")[1]
        X += int(add)
