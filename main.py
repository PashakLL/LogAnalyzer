file_log = input("введите название файла с логами - ")
levels = {}
failed_by_ip = {}
failed = 0
brokenline = 0


try:
    with open(file_log) as f:
        lines = f.readlines()
except FileNotFoundError as error:
    print(f"Файл не найден по причине {error}")
    exit()

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

sorted_failed_by_ip = sorted(failed_by_ip.items(), key=lambda item: item[1], reverse=True)



print(f"Подсчет по записям: {levels}\n")
print("IP с неудачными входами")
for ip_error, count in sorted_failed_by_ip:
    print(f"{ip_error} - {count}")
print(f"\nОшибочная строка: {brokenline}")
print(f"\nНе удачные входы: {failed}")
