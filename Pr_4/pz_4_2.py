#2. Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
#деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
#то вывести TRUE, если нет — вывести FALSE.
a = input("Введите целое число N (>0): ")
while type(a) != int:
    try:
        a = int(a)
        if a <= 0:
            print("Число должно быть больше 0!")
            a = input("Введите целое число N (>0): ")
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое число N (>0): ")
odd = False
temp = a
while temp > 0:
    digit = temp % 10
    if digit % 2 == 1:
        odd = True
        break
    temp = temp // 10
if odd:
    print("TRUE")
else:
    print("FALSE")