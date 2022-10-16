# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

List = [2,3,5,9,3]

print(List)
list_length=len(List)
sum = 0
for i in range(list_length):
    if i%2 != 0:
        sum = sum + List[i]

print(f'На нечётных позициях элементы {List[1]} и {List[3]}. Ответ:', sum)