# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_length = int(input('Введите длину списка: '))
list = []
for i in range(list_length):
    list.append(int(input(f'Введите число {i+1}: ')))
print(list)

list1 = []
list1_length = int(len(list)/2+len(list)%2)

for i in range(list1_length):
    product = list[i]*list[len(list)-1-i]
    list1.append(product)
print(list1)