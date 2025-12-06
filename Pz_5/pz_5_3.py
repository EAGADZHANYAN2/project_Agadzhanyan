#1. Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
#результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.
def sum_digits(n):
    s = 0
    n = abs(n)
    while n > 0:
        s += n % 10
        n //= 10
    return s

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

sum1 = sum_digits(num1)
sum2 = sum_digits(num2)
sum3 = sum_digits(num3)

if sum1 > sum2 and sum1 > sum3:
    print("У первого числа больше сумма цифр")
elif sum2 > sum1 and sum2 > sum3:
    print("У второго числа больше сумма цифр")
elif sum3 > sum1 and sum3 > sum2:
    print("У третьего числа больше сумма цифр")
else:
    print("У нескольких чисел одинаковая сумма цифр")

#2.Рассчитать и вывести периметр и площадь прямоугольника.Расчеты оформить в функции.
# Функции для расчета периметра и площади прямоугольника
def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_area(length, width):
    return length * width

a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))

perimeter = calculate_perimeter(a, b)
area = calculate_area(a, b)

print(f"Периметр прямоугольника: {perimeter}")
print(f"Площадь прямоугольника: {area}")

#3. Написать программу, подсчитывающую количество цифр числа, используя для
#этого функцию
def count_digits(number):
    count = 0
    number = abs(number)
    while number > 0:
        count += 1
        number //= 10
    return count

a = int(input("Введите число: "))
result = count_digits(a)
print(f"Количество цифр в числе: {result}")