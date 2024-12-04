
print("Завдання 1")
# Введення початкового і кінцевого числа
start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

# Перебір чисел у діапазоні від початку до кінця включно
for number in range(start, end + 1):
    # Якщо число кратне 7, виводимо його
    if number % 7 == 0:
        print(number)
    else:
        print("Це число не кратне семи")


print("Завдання 2")
start2 = int(input("Введіть початок діапазону: "))
end2 = int(input("Введіть кінець діапазону: "))

#Виводить всі числа діапазону
for number in range(start2, end2 + 1):
    print(number)

#Виводить числа у зворотньому порядку
for number in range(end2, start2 - 1, -1):
    print(number)

#Виводить числа, якщо кратні 7ми
for number in range(start2, end2 + 1):
    if number % 7 == 0:
        print(number)

#лічильник
count_multiples_of_5 = 0
# Перебір чисел у діапазоні
for number in range(start2, end2 + 1):
    if number % 5 == 0:
        count_multiples_of_5 += 1
        print("Кількість чисел, кратних 5:", count_multiples_of_5)

print("Завдання 3")
start3 = int(input("Введіть початок діапазону: "))
end3 = int(input("Введіть кінець діапазону: "))
#Виводить числа, якщо кратні трьом
for number in range(start3, end3 + 1):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    if number % 3 == 0 and number % 5 ==0:
        print("Fizz Buzz")
    #виводить число, так як інші умови не були задоволені
    else:
        print(number)