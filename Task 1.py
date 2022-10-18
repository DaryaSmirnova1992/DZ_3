# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

List = [2,3,5,9,3]

print(List)
list_length=len(List)
sum = 0
elements = 'На нечётных позициях элементы '
num = str(' ')
for i in range(list_length):
    if i%2 != 0 and (List[-1] or List[-2]):
        sum = sum + List[i]
        num = str(List[i])
        elements = elements + num + '. '
    elif i%2 != 0:
        sum = sum + List[i]
        num = str(List[i])
        elements = elements + num + ', '
    

print(elements + 'Сумма элементов:', sum)