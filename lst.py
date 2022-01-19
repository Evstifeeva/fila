
#Пользователь вводит список из 5 элементов. необходимо нйти наибольший элемент списка и вывести его на экран.
lst_1 = []
i = 0
while i < 5:
    lst_1.append(int(input('Введите число: ')))
    i += 1
print('список - ' + str(lst_1))
max_num = lst_1[0]
for l in lst_1: 
    if l > max_num:
        max_num = l
print('максимальное число: {}'.format(max_num))





