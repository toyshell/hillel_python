user_number = input("Введіть число тільки чотиризначне: ")

number = int(user_number)
if 1000 <= number <= 9999:
 print(number // 1000)
 print(number // 100 % 10)
 print(number //10 % 10 )
 print(number % 10)