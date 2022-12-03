data = open("input.txt").read().split("\n")
items = []
result = 0
group = []

while True:
    group.append(data.pop(0))
    group.append(data.pop(0))
    group.append(data.pop(0))
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            items.append(letter)
            break
    group = []
    if len(data) == 0:
        break
for item in items:
    if item.isupper():
        result += ord(item) - 38
    else:
        result += ord(item) - 96
print(result)