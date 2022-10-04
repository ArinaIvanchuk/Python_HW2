#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на 
#указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

new_list = []
n = int(input('input number N: '))
for i in range(-n, n + 1):
    new_list.append(i)
print(new_list)

path = 'file.txt'
data = open(path, 'r')
list_ind = []
for line in data:
    list_ind.append(int(line))
data.close()

prog = 1
for ind in list_ind:
    if ind < len(new_list):
        prog *= new_list[ind]
print(prog)
