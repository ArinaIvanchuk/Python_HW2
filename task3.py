#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n_list = []
n = int(input('input size list: '))
sum = 0
for i in range(1, n+1):
    n_list.append(round(float((1+1/i)**i)))
    sum = sum + round(float((1+1/i)**i))
print(n_list, '->', sum)