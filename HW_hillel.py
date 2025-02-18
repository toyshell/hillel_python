
# Виконання 3 -х задач 3,1   3,2   3,3
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

