# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('input number N: '))
prog = 1
a = n-(n-1)
print(a)
while a<n:
    a=a+1
    prog *=a
    print(prog)