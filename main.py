with open("test.log") as f:
    lines = f.readlines()


print(len(lines))
parts = lines[0].split()
print(parts)