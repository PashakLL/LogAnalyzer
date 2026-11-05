with open("test.log") as f:
    lines = f.readlines()


for i in range(len(lines)):
    parts = lines[i].split()
    if len(parts) < 5:
        print(f"Ошибочная строка")
        continue
    print(f"{parts[2]}")