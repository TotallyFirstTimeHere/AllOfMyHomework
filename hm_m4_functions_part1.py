print("Ex1")
def formatText():
    x = input("""“Don’t compare yourself with anyone in this world…
    if you do so, you are insulting yourself.”
                                        Bill Gates""")
formatText()

print("\nEx2")
def number(n1, n2):
    for i in range(n1 + 1, n2):
        if i % 2 != 1:
            print(i)

number(2, 12)

print("\nEx3")
def square(length, symbol, filled):
    for i in range(length):
        if filled or i == 0 or i == length - 1:
            # Якщо квадрат заповнений, або якщо це перший чи останній рядок
            print(symbol * length)
        else:
            # Виводимо порожній рядок з символами по краях
            print(symbol + " " * (length - 2) + symbol)
#вивожу функцію
square(6, '@', True)
print()
square(6, '*', False)

print("\nEx4")
def minimum(a,b,c,d,e):
    min_num = a #припускаю, що а найбільше
    if b < min_num: #якщо б більше за макснум, то б присвоюється макснум
        min_num = b
    if c < min_num:
        min_num = c
    if d < min_num:
        min_num = d
    if e < min_num:
        min_num = e
    return min_num
result = minimum(10, 25, 169, 18, 2)
print("Найменьше число:", result)

print("\nEx5")
def dobutok_in_range(start, end):
    # Перевірка та обмін значень, якщо межі переплутані
    if start > end:
        start, end = end, start

    dobutok = 1
    for number in range(start, end +1):
        dobutok *= number
    return dobutok
print()

print(dobutok_in_range(5, 10))   # Добуток чисел від 5 до 10
print(dobutok_in_range(10, 5))   # Добуток чисел від 5 до 10 (переплутані межі)

print("\nEx6")
def quantity(number):

    number = abs(number) #abs - модуль, його взяв щоб знак не впливав
    return len(str(number))

# Приклад виклику функції
print(quantity(3456))    # Виведе 4
print(quantity(-12345))  # Виведе 5 (негативне число)
print(quantity(0))       # Виведе 1

print("\nEx7")
def if_palindrom(number2):
    number2_str = str(abs(number2))
    #порівняв рядок з його перевернутою версією
    return  number2_str == number2_str[::-1]

print(if_palindrom(123321))
print(if_palindrom(546645))
print(if_palindrom(421987))
print(if_palindrom(-12321))
