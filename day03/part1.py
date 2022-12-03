data = open("input.txt").read().split("\n")
items = []
result = 0
for line in data:
    first, second = line[:len(line)//2], line[len(line)//2:]
    for letter in first:
        if letter in second:
            items.append(letter)
            break
for item in items:
    if item.isupper():
        result += ord(item) - 38
    else:
        result += ord(item) - 96
print(result)