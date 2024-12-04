print("Завдання 1")
a = int(input("Введіть 1ше число: "))
b = int(input("Введіть 2ге число: "))

# Ініціалізація змінних для сум та лічильників
sum_even = 0  # Сума парних чисел
count_even = 0  # Кількість парних чисел

sum_odd = 0  # Сума непарних чисел
count_odd = 0  # Кількість непарних чисел

sum_multiples_of_9 = 0  # Сума чисел, кратних 9
count_multiples_of_9 = 0  # Кількість чисел, кратних 9

# Перебір чисел у діапазоні
for number in range(a, b + 1):
    if number % 2 == 0:
        sum_even += number
        count_even += 1
    else:
        sum_odd += number
        count_odd += 1

    if number % 9 == 0:
        sum_multiples_of_9 += number
        count_multiples_of_9 += 1

# Обчислення середніх арифметичних
if count_even > 0:
    avg_even = sum_even / count_even
else:
    avg_even = 0  # Якщо немає парних чисел

if count_odd > 0:
    avg_odd = sum_odd / count_odd
else:
    avg_odd = 0  # Якщо немає непарних чисел

if count_multiples_of_9 > 0:
    avg_multiples_of_9 = sum_multiples_of_9 / count_multiples_of_9
else:
    avg_multiples_of_9 = 0  # Якщо немає чисел, кратних 9

# Виведення результатів
print("Сума парних чисел:", sum_even)
print("Середнє арифметичне парних чисел:", avg_even)

print("Сума непарних чисел:", sum_odd)
print("Середнє арифметичне непарних чисел:", avg_odd)

print("Сума чисел, кратних 9:", sum_multiples_of_9)
print("Середнє арифметичне чисел, кратних 9:", avg_multiples_of_9)

print("Завдання 2")
length = int(input("Введіть довжину лінії: "))
symbol = input("Введіть символ для лінії: ")
# Виведення вертикальної лінії
for i in range(length):
    print(symbol)

print("Завдання 3")
while True: #нескінченний цикл
    n = int(input("Введіть число "))
    if n == 7:
        print("Good bye!")    #закінчує
        break #виходить з циклу
    if n > 0:
        print("Number is positive")
    elif n < 0:
        print("Number is negative")
    elif n  == 0:
        print("Number is equal to zero")


print("Завдання 4")

overall_sum = 0 #змінна що буде оновлюватися
min_number = float('inf') #-нескінченність, щоб знайти реальний мінімум
max_number = float('-inf') #+нескінченність, щоб знайти реальний максимум

#нескінченний цикл, який буде виконуватися поки користувач не введе 7
while True:
    num = int(input("Введіть число: "))

    if num == 7:
        print("Good bye!")
        break

    overall_sum += num #оновлення всіх введених чисел
    min_number = min(min_number, num) #оновлення найменьщого чисела серед введених
    max_number = max(max_number, num) #оновлення найбільшого чисела серед введених

    print(f"Поточна сума: {overall_sum}")
    print(f"Мінімум: {min_number}")
    print(f"Максимум: {max_number}")