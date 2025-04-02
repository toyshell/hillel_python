#Завдання 15.1           15.2

#Завдання 15.1
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        new_width = (total_area / self.height)
        return Rectangle(new_width, self.height)

    def __mul__(self, n):
        total_area = self.get_square() * n
        new_width = (total_area / self.height)
        return Rectangle(new_width, self.height)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'
print('ok')
r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print('ok')
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print('Ok')
print('All tests passed!')


# Завдання 14.2
import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.a, self.b)
        self.a = self.a // gcd
        self.b = self.b // gcd

    def __mul__(self, other):
        result = Fraction(self.a * other.a, self.b * other.b)
        result.simplify()
        return result

    def __add__(self, other):
        new_b = self.b * other.b
        new_a = self.a * other.b + other.a * self.b
        result = Fraction(new_a, new_b)
        result.simplify()
        return result

    def __sub__(self, other):
        new_b = self.b * other.b
        new_a = self.a * other.b - other.a * self.b
        result = Fraction(new_a, new_b)
        result.simplify()
        return result

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')

"""
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.age}років,{self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()},{self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))

class GroupOverflowError(Exception):
    pass

class Group:
    MAX_STUDENTS = 10
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupOverflowError("Не можна додавати більше 10 студентів у групу.")
        self.group.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)

        return f'Number:{self.number}\\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
print('ok')
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!


# Завдання 14.2

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.age}років,{self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()},{self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))

class Group:

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if student not in self.group:
            self.group.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)

        return f'Number:{self.number}\\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
print('ok')
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!


# Завдання 13.1     13.2

# Завдання 13.1

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.age}років,{self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()},{self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        if student not in self.group:
            self.group.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
            return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)

        return f'Number:{self.number}\\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
print('ok')
gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!


# Завдання 13.2


class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       self.current = start

   def set_max(self, max_max):
        self.max_value = max_max

   def set_min(self, min_min):
       self.min_value = min_min

   def step_up(self):
       if self.current >= self.max_value:
           raise ValueError("Досягнуто максимум")
       self.current += 1


   def step_down(self):
       if self.current <= self.min_value:
           raise ValueError("Досягнуто мінімальне")
       self.current -= 1

   def get_current(self):
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
print('OK')


# Завдання  12.1            12.2

# Завдання 12.1

import codecs
import re

def delete_html_tags(html_file='draft.html', result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()


    clean_html = re.sub(r'<[^>]+>', '', html)


    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(clean_html)

delete_html_tags('draft.html', 'cleaned.txt')


# Завдання 12.2

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"Price:{self.price},Description:{self.description},Dimensions:{self.dimensions},Name:{self.name}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"User:{self.name} {self.surname},Numberphone:{self.numberphone}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.products:
          self.products[item] = +cnt
        else:
          self.products[item] = cnt

    def __str__(self):
        # Створення рядка items_str, що містить інформацію про кожен товар
        items_str = " ".join([f"{item.name}: {cnt} pcs., price: {item.price}" for item, cnt in self.products.items()])

        # Повертається форматований рядок з інформацією про користувача та товари
        return f"User: {self.user.name} {self.user.surname} Items: {items_str}"

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

#User: Ivan Ivanov
#Items:
#lemon: 4 pcs.
#apple: 20 pcs.

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)

#User: Ivan Ivanov
#tems:
#lemon: 4 pcs.
#apple: 10 pcs.


assert cart.get_total() == 40
print('ok')


# Завдання         11.1            11.2               11.3

# Завдання 11.1

import math

def prime_generator(end):
    for num in range(2, end):
        if all(num % i != 0 for i in range(2,int(math.sqrt(num))+1)):
            yield num

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')

# Завдання 11.2

def generate_cube_numbers(end):
    for el in range(2, end + 1):
        if el ** 3 <= end:
            yield el ** 3


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

print("OK")

# Завдання  10.3

def is_even(number):
    if (number & 1) == 0:
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print("Ok")




#Завдання  10,1             10,2             10,3

#Завдання 10.1

def pow(x):
    return x ** 2

def some_gen(begin, end, func):

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

















