print(f"Завдання 1")
a = int(input("Введіть 1ше число: "))
b = int(input("Введіть 2ге число: "))
c = int(input("Введіть 3тє число: "))
d = input("Вибір дії множення/сума?")

for i in range(a, b, c):
    if d == "множення":
        print(a*b*c)
    elif d == "сума":
        print(a + b + c)
    else:
        print("Вказана дія не підходить\n")


print(f"Завдання 2")

a1 = int(input("Введіть 1ше число: "))
b1 = int(input("Введіть 2ге число: "))
c1 = int(input("Введіть 3тє число: "))
d1 = input("Максимум? Мінімум? Середньоарифметичне?")

if d1.lower() == "максимум":
    print("Максимум:", max(a1, b1, c1))
elif d1.lower() == "мінімум":
     print("Мінімум:", min(a1, b1, c1))
elif d1.lower() == "cередньоарифметичне":
    print("Середньоарифметичне:", (a + b + c) / 3)
else:
    print("Вказана дія не підходить\n")

print(f"Завдання 3")

while True:
    m = int(input("Введіть метри: "))
    distance = input(f"В яку одиницю вимірювання хочете перевести милі/дюйми/ярди: ")
    if distance.lower().startswith("милі"):
        miles = m * 1.6
        print(f"{miles} миль")
    elif distance.lower().startswith("дюйми"):
        inches = m * 39.3701
        print(f"{inches} дюймів")
    elif distance.lower().startswith("ярди"):
        yards = m * 1.09361
        print(f"{yards} ярдів")
    else:
        print("error 69 wait for update")

    if distance.lower().startswith("exit") or distance.lower().startswith("qq"):
        break