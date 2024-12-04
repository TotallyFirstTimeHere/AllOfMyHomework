from random import randint
#ex1
print("\nEx1")
#список рандомних цілих чисел
list1 = [randint(-100, 100) for _ in range(6)]
list2 = [randint(-100, 100) for _ in range(6)]

print("Список 1:", list1)
print("Список 2:", list2)

# 1. Об'єднані елементи обох списків
combined = list1 + list2
print("\nОб'єднані елементи обох списків:", combined)

# 2. Елементи обох списків без повторень
combined_no_duplicates = list(set(list1 + list2))
print("Елементи обох списків без повторень:", combined_no_duplicates)

# 3. Елементи, спільні для двох списків
common_elements = list(set(list1) & set(list2))
print("Елементи, спільні для двох списків:", common_elements)

# 4. Унікальні елементи кожного зі списків
unique_in_list1 = list(set(list1) - set(list2))
unique_in_list2 = list(set(list2) - set(list1))
unique_elements = unique_in_list1 + unique_in_list2
print("Тільки унікальні елементи кожного зі списків:", unique_elements)

# 5. Мінімальне та максимальне значення кожного зі списків
min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
print("Мінімальне та максимальне значення списку 1:", min_max_list1)
print("Мінімальне та максимальне значення списку 2:", min_max_list2)
