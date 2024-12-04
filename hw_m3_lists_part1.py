from typing import final

print("Ex1")
user = input("Введіть слово для перевірки на паліндром: ")
#перевожу рядок до нижнього регістру та видаляю пробіли
"""user.replace(" ", "") видаляє всі пробіли в рядку.
.lower() приводить рядок до нижнього регістру, щоб порівняння було коректним
"""
user = user.replace(" ", "").lower()
#Перевіряю чи рядок юзер рівний його перевернутій версії
if user == user[::-1]: #user[::-1] створює перевернутий рядок.
    print("Це паліндром\n")
else:
    print("Це не паліндром\n")

print("Ex2")
user2 = input("Введіть текст: ")
# метод .split перетворює рядок на рядок на окремі слова з пробілами
reserved_words = input(f"Введіть список зарезервованих слів: ").split()
# в цьому випадку розбиваю текст на слова, щоб можна було перевірити кожне слово
words = user2.split()
new_text = []

for word in words:
    #перевіряю чи слово є в списку зарезервованих слів, та змінюю його регістр
    if word in reserved_words:
        new_text.append(word.upper())
    else:
        new_text.append(word)

final_text = ' '.join(new_text) #об'єднує слова назад в рядок

print(f"Замінений текст: {final_text}\n")

print("Ex3")
text = input("Введіть текст:")
#це стандартний модуль у Python для роботи з регулярними виразами (regex),
#які допомагають шукати, замінювати та перевіряти складні шаблони тексту.
import re
import time
#розділяю текст на речення де є .!?
sentences = re.split(r'[.!?]', text)

sentences = [s for s in sentences if s.strip()]
# s на початку вказує що потрібно додати в новий список
# далі в циклі for s in sentences виконується перебір кожного елемента в списку sentences
#замінюючи на s
# на останок умова if s.strip() робить так, щоб у новий список потрапили тільки ті елементи, які не є порожніми рядками
#іншими словвами містить текст
"""new_sentences = []
for s in sentences:
    if s.strip():
        new_sentences.append(s)"""
#так би виглядав генератор списків як би його робив тіки через цикл
sum_sentences = len(sentences)
print(f"Кількість речень у тексті:  {sum_sentences}")
time.sleep(3)