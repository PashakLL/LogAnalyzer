with open("test.log") as f:
    lines = f.readlines()


levels = {}
failed_by_ip = {}
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
        ip=parts[5].split('ip=')[1]
        if ip in failed_by_ip:
            failed_by_ip[ip] += 1
        else:
            failed_by_ip[ip] = 1
    if level in levels:
        levels[level] += 1
    else:
        levels[level] = 1
print(levels)
print(failed_by_ip)
print(f"Ошибочная строка: {brokenline}")
print(f"Не удачные входы: {failed}")
