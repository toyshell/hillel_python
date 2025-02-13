user_number = input("Введіть число тільки чотиризначне: ")

number = int(user_number)
if 1000 <= number <= 9999:

print(number % 10, number // 10 % 10, number // 100 % 10, number // 1000 % 10, number // 10000)
