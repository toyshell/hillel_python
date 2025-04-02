

"""
# Завдання 14.1

from HW_hillel import Student, Group, GroupOverflowError


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
print('OK')

try:
    for i in range(11):
        gr.add_student(st1)
except GroupOverflowError as e:
    print(e)
"""












"""
# Завдання 14.2

from HW_hillel import Student, Group


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
print('OK')

gr.delete_student('Taylor')
print(gr) # Only one student

gr.delete_student('Taylor')



first_list = [[1, 2, 3], [4, 5, 6]]
for lst in first_list:
    #for j in lst:
        print(lst, end ="")

import random
my_list = []
# Не найоптимальніший варіант рішення
for i in range(random.randint(6, 15)):
my_list.append(random.randint(1, 1000))
print(my_list)

# Виконання 3 -х задач 3,1   3,2  3,3
# HW 3.1

x = int(input("введіть число перщої змінної "))
y = int(input("введіть число другої змінної "))
operators = input("виберіть оператора +.-,/,* ")

if operators == "+":
    print(x+y)
elif operators == "-":
    print(x-y)
elif operators == "*":
    print(x*y)
elif operators == "/":
  if y == 0:
    print("ви ввели 0, введіть не 0 ")
  else:
    print(x / y)
else:

    print("невірне число")




# HW 3.2

lst = [1]

if len(lst) > 0:
    last_number = lst.pop()
    lst.insert(0,last_number)
print(lst)


 # HW 3.3

lst = [1]

if len(lst) == 0:
    print([[], []])
elif len(lst) % 2 == 0:
    number = len(lst) // 2
    print([lst[:number], lst[number:]])
else:
    number = len(lst) // 2 + 1
    print([lst[:number], lst[number:]])




x = input("введіть число перщої змінної ")
y = input("введіть число другої змінної ")

if not x.isnumeric() or not y.isnumeric():
    print("введи цифру")
else:
    x = int(x)
    y = int(y)

operators = input("виберіть оператора +.-,/,* ")

if operators == "+":
    print(x+y)
elif operators == "-":
    print(x-y)
elif operators == "*":
    print(x*y)
elif operators == "/":
  if y == 0:
    print("ви ввели 0, введіть не 0 ")
  else:
    print(x / y)
else:

    print("невірне число")


a = True
if  a:
    a = True
    print(True)
else:
    if not a:
     print(False)

number = int(input("Введи число "))

if number == 3:
    print("Almost Fizz")
elif number == 5:
    print("Майже гул")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else :
    print("Не вірно ввели")

# count() - повертає кількість входжень елемента до списку.
first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
print(first_list.count(5))  # 3
first_list.count(9) # 0

# Перевірка того, що число є простим, за допомогою циклу
# виведе на екран прямокутник із символів «*».
a = int(input("Input a "))
b = int(input("Input b "))
i = 0
while i < a: # Висота
    j = 0
    while j < b: # ширина
        print("*") # рядок не буде переведено
        j += 1
    print()
    i += 1

first_list = [[1, 2, 3], [4, 5, 6]]
i = 0
while i < len(first_list):
        j = 0
        lst = first_list[i]
        while j < len(lst):
            print(lst[j])
            j += 1
        i += 1


import random
my_list = [random.randint(1, 100) for i in range(random.randint(6, 15))]
print(my_list)


import random
lst = [3, 4, 6, 1, 2, 5, 3, 4, 1, 6]
# Генеруємо список із 10 випадкових чисел від 0 до 10
numbers = [random.randint(0, 10) for _ in lst]



# Виводимо згенерований список
print("Generated list:", numbers)









# Перевірка суми суміжних чисел
found_pair = False
for i in range(len(numbers) - 1):
    if numbers[i] + numbers[i + 1] == 7:
        print(f"Found a pair that sums to 7: ({numbers[i]}, {numbers[i + 1]})")
        found_pair = True

if not found_pair:
    print("No pairs found that sum to 7.")



# Завдання на рік високосний рік чи ні

year = int(input("Введи рік: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Цей рік високосний")
else:
    print("Цей рік невисокосний")


answers = []

# Перелік запитань
questions = [
    "Чи ти відважний?",
    "Чи любиш маніпулювати іншими?",
    "Чи любиш ти пригоди?",
    "Чи є в тебе терпіння?",
    "Чи важлива для тебе справедливість?"
]

# Цикл для питань
for question in questions:
    answer = input(question + " (так/ні): ").lower()

    # Перевірка правильності відповіді
    if answer not in ['так', 'ні']:
        print("Будь ласка, введіть 'так' або 'ні'.")
        answer = input(question + " (так/ні): ").lower()  # Дозволяє ввести відповідь ще раз

    answers.append(answer)

# Логіка для визначення будинку
if answers.count("так") >= 3:
    print("Вітаємо! Ви потрапили в Ґріфіндор!")
elif answers.count("так") == 2:
    print("Вітаємо! Ви потрапили в Хаффлпафф!")
elif answers.count("так") == 1:
    print("Вітаємо! Ви потрапили в Рейвенкло!")
else:
    print("Вітаємо! Ви потрапили в Слізерин!")



def find_gcd(a, b):
    # Ваш код тут
    while b != 0:
        a, b = b,a % b
    return a
print(find_gcd(98, 56))

"""