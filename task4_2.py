'''
Вывести на экран ромб из звездочек
'''

d = int(input("Введите диагональ ромба: "))
c = d // 2

for y in range(d):
    for x in range(d):
        if y <= c:
            if c - y <= x <= c + y:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if c + y - d + 1 <= x <= c - y + d - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

    