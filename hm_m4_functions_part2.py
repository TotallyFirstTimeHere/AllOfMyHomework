from itertools import product

print("\nEx1")
def dobutok_of_list(numbers):
    dobutok = 1
    for number in numbers:
        dobutok *= number
    return dobutok

print(dobutok_of_list([1, 2, 3, 4]))
print(dobutok_of_list([5, 10, -2]))
print(dobutok_of_list([]))
print(dobutok_of_list([345, 124, -214, -2837]))

print("\nEx2")
def minimum(numbers2):
    if not numbers2:
        return None #якщо список порожній

    min = numbers2[0]
    for number in numbers2:
        if number < min:
            min = number
    return min

print("Найменьше число:", minimum([3, 10, 84, -90, -2]))
print("Найменьше число:", minimum([69, 293, 2039]))
print("Найменьше число:", minimum([]))

print("\nEx3")
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    prime_count = 0
    for number in numbers:
        if is_prime(number):
            prime_count += 1
    return prime_count

print(count_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(count_primes([11, 13, 17, 19, 23]))
print(count_primes([1, 4, 6, 8, 10]))
print(count_primes([318, 8273, 92, 69, 2837, 777]))

print("\nEx4")
def remove(numbers, target):
    initial_length = len(numbers) #початкова довжина списку
    numbers[:] = [num for num in numbers if num !=target] # оновив оригінальний список
    removed_count = initial_length - len(numbers) # Кількість видалених елементів
    return removed_count

numbers = [1242, 93, 20, 32, 94, 93, 93, 69]
target = 93
removed_count2 = remove(numbers, target)
print("Кількість видалених елементів:", removed_count2)
print("Оновлений список:", numbers)

print("\nEx5")
def merge_lists(list1, list2):
    return list1 + list2  # об'єднав два списки за допомогою оператора +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print("Об'єднаний список:", merged_list)

print("\nEx6")
def power_element(numbers, exponent):
    return [num ** exponent for num in numbers] #створюю новий списк підносячи кожен елемент ^2

numbers = [11, 21, 12, 13, 15, 16,]
exponent = 2
powered = power_element(numbers, exponent)
print(f"Списк піднесений до ^2:", powered)