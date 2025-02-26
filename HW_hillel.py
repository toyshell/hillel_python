# Завдання              5.1               5.2               5.3

# HW Завдання 5.1

import keyword
import string

text = ["_var", "var_", "var1", "Var", "var iable", "var!able", "for", "_", "__", "1var"]


for name in text:
    if name[0].isdigit():
        print(False)
    elif any(el.isupper() for el in name):
        print(False)
    elif any(el in string.punctuation.replace("_", "") for el in name):
        print(False)
    elif name in keyword.kwlist:
        print(False)
    elif name.count("_") > 1:
        print(False)
    else:
        print(True)


# HW Завдання 5.2

while True:

    while True:
        a = input("Введіть число (A): ")
        b = input("Введіть друге число (B): ")
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            break
        else:
            print("Помилка: введіть правильні числа.")


    while True:
        calculator = input("Введіть операцію (+, -, *, /): ")
        if calculator == "+":
            print(f"Результат: {a + b}")
            break
        elif calculator == "-":
            print(f"Результат: {a - b}")
            break
        elif calculator == "*":
            print(f"Результат: {a * b}")
            break
        elif calculator == "/":
            if b != 0:
                print(f"Результат: {a / b}")
            else:
                print("Помилка: ділення на нуль.")
            break
        else:
            print("Помилка: невірна операція. Спробуйте ще раз.")


    answer = input("Do you want to continue? yes/no: ")
    if answer not in ["yes", "y"]:
        print("Калькулятор завершено.")
        break


# HW Завдання 5.3

import  string

text = input("Введіть текст: ")

for el in string.punctuation:
    text = text.replace(el, "")

hashtag = "#" + "".join(word.capitalize() for word in text.split()) [:140]

print(hashtag)















"""

# Завдання  4.1    4.2     4.3

# HW Завдання 4.1
lst = [0, 1, 0, 12, 3]
new_lst = []

for num in lst:
    if num != 0:
        new_lst.append(num)

for i in range(lst.count(0)):
    new_lst.append(0)

print(new_lst)

# HW Завдання 4.2

lst = [0, 1, 7, 2, 4, 8]
num_index = 0

for i in range(0,len(lst),2):
    num_index += lst[i]

result = num_index * lst[-1]

print(result)


# HW Завдання 4.3


import random
lst = [1, 2, 3, 4, 5, 6, 7, 9]

new_random_lst = [random.randint(0, 10) for i in range(len(lst))]

new_lst = [lst[0],lst[2],lst[-2]]

print(new_lst)

"""

















