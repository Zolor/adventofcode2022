line = "dir a"
print(line.split(" ")[1])

curr_dir = "/a/b/"
folder = curr_dir.rfind("/",0,-1)
curr_dir = curr_dir[:folder+1]

print(curr_dir)
print(folder)