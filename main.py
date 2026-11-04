with open("test.log") as f:
    line = f.readlines()

count = 0


for i in line:
    count += 1
print(count)