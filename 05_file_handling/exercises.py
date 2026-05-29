with open("example.txt", "r") as file:
    lines = file.readlines()

print("Number of lines:", len(lines))


with open("example.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as target:
    target.write(content)