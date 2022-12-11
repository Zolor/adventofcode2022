data = open("input.txt").read()#.split("\n")
datamod = [i for i in data.split("\n\n")]
monkey_items = []
instructions = []
test_divs = 1

for i in datamod:
    tmp_line = i.split("\n")
    tmp = tmp_line[1].strip("  Starting items: ")
    test_divs *= int(tmp_line[3].strip("  Test: divisible by "))
    tmp_lista = []
    for x in tmp.split(", "):
        tmp_lista.append(int(x))
    monkey_items.append(tmp_lista)
    op = tmp_line[2]
    test = int(tmp_line[3].split(" ")[-1])
    if_true = int(tmp_line[4].split(" ")[-1])
    if_false = int(tmp_line[5].split(" ")[-1])
    instructions.append([op, test, if_true, if_false])
print(test_divs)
inspects = [0] * len(monkey_items)

for _ in range(10000):
    for x, line in enumerate(instructions, start=0):
        op = instructions[x][0]
        test = instructions[x][1]
        if_true = instructions[x][2]
        if_false = instructions[x][3]
        #print(op)
        for item in monkey_items[x]:
            inspects[x] += 1
            #operation
            tmp_item = 0
            intr = op.split(" ")[-1]
            if "+" in op:
                if intr == "old":
                    tmp_item += item + item
                    tmp_item = tmp_item % test_divs
                else:
                    tmp_item += item + int(intr)
                    tmp_item = tmp_item % test_divs
            elif "*" in op:
                if intr == "old":
                    tmp_item += item * item
                    tmp_item = tmp_item % test_divs
                else:
                    tmp_item += item * int(intr)
                    tmp_item = tmp_item % test_divs
            #test
            if tmp_item % test == 0:
                monkey_items[if_true].append(tmp_item)
            else:
                monkey_items[if_false].append(tmp_item)
        monkey_items[x] = []

inspects = sorted(inspects)
print(inspects)
print(inspects[-1] * inspects[-2])