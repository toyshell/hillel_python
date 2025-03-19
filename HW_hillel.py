#Завдання  10,1             10,2             10,3

#Завдання 10.1

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    value = begin
    for el in range(end):
        yield  value
        value = func(value)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

# Завдання 10.2

import re

def first_word(text: str) -> str:

    new_text = re.search(r"[a-zA-Zа-яА-ЯёЇїІіЄєҐґ']+", text)
    return new_text.group() if new_text else ""


assert first_word("Hello world!") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

# Завдання 10.3

def is_even(digit):

    if digit % 2 == 0:
        return True
    else:
        return False



assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')



"""

# Завдання        9.1            9.2

# Завдання 9.1

def popular_words (text, words):
    new_text = text.lower()
    new_text = "".join(char if char.isalpha() or char == " " else "" for char in new_text)
    new_list = new_text.split()
    return {word:new_list.count(word) for word in words}

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'

print('OK')

# Завдання 9.2

def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args),2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')


# Завдання              8.1      8.2      8.3

# Завдання 8.1

def add_one(some_list):

   number = int("".join(map(str, some_list)))

   number += 1

   return [int(digit) for digit in str(number)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")

# Завдання 8.2

def is_palindrome(text):

    text_cleaned = "".join(el.lower() for el in text if el.isalnum())

    return text_cleaned == text_cleaned[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")

# Завдання 8.3

def find_unique_value(some_list):
   for number in some_list:
      if some_list.count(number) == 1:
           return number

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")


# Завдання                   7.1          7.2          7.3         7.4

# Завдання  7.1

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

# Заавдання 7.2

def correct_sentence(text):
    if not text:
        return ""

    text = text[0].upper() + text[1:]

    if not text.endswith("."):
        text += "."

    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')


# Завдання 7.3

def second_index(text, some_str):

    first_text = text.find(some_str)
    if first_text == -1:
        return None

    second_index = text.find(some_str, first_text + 1)

    if second_index == -1:
        return None

    return second_index

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')


# Завдання 7.4

def common_elements():
    multiples_of_3 = set(range(0, 100, 3))
    multiples_of_5 = set(range(0, 100, 5))

    return multiples_of_3.intersection(multiples_of_5)  # Перетин множин

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")




#HW Завдання                  6.1         6.2          6.3

# Завдання 6,1

import string

lst = string.ascii_letters

user_letters = input("Введіть дві літери через дефіс: ")

start, end = user_letters.split("-")

start_index = lst.index(start)
end_index = lst.index(end)

result = lst[start_index : end_index + 1]
print(result)


from math import remainder

# Завдання 6,2

seconds = int(input("введіть секунди від 0 до 8640000 - "))

if 0 <= seconds < 8640000:
    days = seconds // 86400
    hours = (seconds % 86400)// 3600
    minutes = (seconds % 3600) // 60
    _seconds = seconds % 60

    time_sec = f"{hours:02}:{minutes:02}:{_seconds:02}"
    day_sec = "день" if days == 1 else "дні"

    print(f"{days} {day_sec}, {time_sec}")
else:
    print("Введіть секунди від 0 до 8640000 правельно ")



# Завдання 6.3

numbers = int(input("Ведіть число: "))

while numbers >= 9:
 digit = list(str(numbers))
 new_digit =[int(el) for el in digit]

 new_number = 1

 for el in new_digit:
     new_number *= el

 numbers = new_number
print(numbers)


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

















