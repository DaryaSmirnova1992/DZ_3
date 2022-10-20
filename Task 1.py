# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
List=[ random.randint(-100,100) for _ in range(10)]
print(List)

sum = 0
elements = 'На нечётных позициях элементы '
num = str(' ')
list_length=len(List)
for i in range(list_length):
    if i%2 != 0 and i> list_length - 2:
        sum = sum + List[i]
        num = str(List[i])
        elements = elements + num + '. '
    elif i%2 != 0:
        sum = sum + List[i]
        num = str(List[i])
        elements = elements + num + ', '
    

print(elements + 'Сумма элементов:', sum)