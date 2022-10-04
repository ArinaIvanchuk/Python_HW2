# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = float(input('input number: '))
a= int(num)
b = round(num - int(num), 3)
sum = 0
while a!=0:
    sum+=a%10
    a=a//10
while b!=0:
    sum+=int(b*10)
    b = round(b*10 - int(b*10), 3)
print(sum)