data = open("input.txt").read().split("\n")

ls = False
storage = {}
curr_dir = "/"
folder = ""
folders = []
for line in data:
    if "ls" in line:
        ls = True
    elif line.startswith("$ cd"):
        if line.endswith("..") and curr_dir != "/":
            folder = curr_dir.rfind("/",0,-1)
            curr_dir = curr_dir[:folder+1]
        elif line.endswith("/"):
            continue
        elif line.endswith("..") and curr_dir == "/":
            continue
        else:
            folder = line.split(" ")[2] + "/"
            curr_dir = curr_dir + folder
            folders.append(curr_dir)
        ls = False
    if ls == True and line[0].isdigit():
        fs = [int(i) for i in line.split() if i.isdigit()]
        fs = int(fs[0])
        if curr_dir not in storage:
            storage[curr_dir] = fs
        else:
            storage[curr_dir] = storage.get(curr_dir) + fs
    elif curr_dir not in storage:
        storage[curr_dir] = 0

tmp = sorted(storage.keys(), key=len, reverse=True)
for key in tmp:
    for key2 in tmp:
        if key == key2:
            continue
        elif key2.startswith(key) and key.count("/") + 1 == key2.count("/"):
            storage[key] = storage[key] + storage[key2]
            #print(key, key2, storage[key], storage[key2])

print(storage)
resultat = 0
for val in storage.values():
    if val <= 100000:
        resultat += val

print(resultat)