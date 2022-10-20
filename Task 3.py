# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

array = []
n = int(input('Сколько в массиве будет элементов: '))

for i in range(n):
    k = float(input((f'{i+1}-е число: ')))
    array.append(k)
    
print(array)

min= float((array[0]))%1
max= float((array[0]))%1

for i in array:
    i=(float(i)%1)
    if i==0:
        continue
    if i>max:
        max=i
    elif i<min:
        min=i

print(f'Mинимальное значение дробной части элементов: {round(min, 3)}')
print(f'Mаксимальное значение дробной части элементов: {round(max, 3)}')
print(f'Разницa между максимальным и минимальным значением дробной части элементов: {round((max-min), 3)}')


