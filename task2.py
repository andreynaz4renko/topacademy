'''
Пользователь вводит с клавитуры ширину и высоту прямоугольника.
Требуется отобразить на экран заполненный прямоугольник c
указанными высотой и шириной. Например, если пользователь ввёл 
высоту 3, а ширину 5 на экране будет выведено:
   *****
   *****
   *****
'''

a = int(input("Введите высоту: "))
b = int(input("Введите ширину: "))

for y in range(a):
    for x in range(b):
        print("*", end=" ")
    print()