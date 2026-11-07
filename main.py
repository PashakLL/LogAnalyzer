with open("test.log") as f:
    lines = f.readlines()


counts = {}
failed = 0
brokenline = 0

for i in range(len(lines)):
    parts = lines[i].split()
    if len(parts) < 5:
        brokenline += 1
        continue
    level = parts[2]
    if parts[3] == "login_failed":
        failed += 1
    if level in counts:
        counts[level] += 1
    else:
        counts[level] = 1
print(counts)
print(f"Ошибочная строка: {brokenline}")
print(f"Не удачные входы: {failed}")
