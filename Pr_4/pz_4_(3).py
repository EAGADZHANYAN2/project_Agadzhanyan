#1. Сумма и количество отрицательных чисел
count_negative = 0
sum_negative = 0
i = 1
while i <= 4:
    a = int(input(f"Введите число {i}: "))
    if a < 0:
        count_negative += 1
        sum_negative += a
    i += 1
print("Количество отрицательных чисел:", count_negative)
print("Сумма отрицательных чисел:", sum_negative)

#2. Количество четных чисел
count_even = 0
i = 1
while i <= 4:
    a = int(input(f"Введите число {i}: "))
    if a % 2 == 0:
        count_even += 1
    i += 1
print("Количество четных чисел:", count_even)

#3. Квадраты и кубы чисел от 2 до 5
print("Число\tКвадрат\tКуб")
a = 2
while a <= 5:
    print(f"{a}\t{a**2}\t{a**3}")
    a += 1

#4. Сумма факториалов
n = int(input("Введите n (n>1): "))
total_sum = 0
factorial = 1
i = 1
while i <= n:
    factorial *= i
    total_sum += factorial
    i += 1
print("S =", total_sum)

#5. Среднее арифметическое N чисел
n = int(input("Введите количество чисел N: "))
total_sum = 0
i = 1
while i <= n:
    a = int(input(f"Введите число {i}: "))
    total_sum += a
    i += 1
average = total_sum / n
print("Среднее арифметическое:", average)

#6. Количество чисел равных нулю
a = int(input("Введите количество чисел N: "))
count_zero = 0
i = 1
while i <= a:
    b = int(input(f"Введите число {i}: "))
    if b == 0:
        count_zero += 1
    i += 1
print("Количество чисел равных нулю:", count_zero)

#7. Числа между A и B в порядке убывания (включая A и B)
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
count = 0
current = b
print("Числа в порядке убывания:")
while current >= a:
    print(current)
    count += 1
    current -= 1
print("Количество чисел:", count)

#8. Сумма чисел от A до B включительно
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
total_sum = 0
current = a
while current <= b:
    total_sum += current
    current += 1
print("Сумма чисел от A до B:", total_sum)

#9. Элементы арифметической прогрессии 10<ai<30
count = 0
a1 = 1
d = 3
n = 5
i = 1
current = a1
print("Элементы прогрессии удовлетворяющие условию 10<ai<30:")
while i <= n:
    if 10 < current < 30:
        print(current)
        count += 1
    current += d
    i += 1
print("Количество элементов:", count)

#10. Числа Фибоначчи и количество четных
a = int(input("Введите N (N≥3): "))
fib1, fib2 = 1, 1
count_even = 0
i = 1
print("Первые", a, "чисел Фибоначчи:")
while i <= a:
    if i == 1:
        print(fib1, end=" ")
        if fib1 % 2 == 0:
            count_even += 1
    elif i == 2:
        print(fib2, end=" ")
        if fib2 % 2 == 0:
            count_even += 1
    else:
        fib_next = fib1 + fib2
        print(fib_next, end=" ")
        if fib_next % 2 == 0:
            count_even += 1
        fib1, fib2 = fib2, fib_next
    i += 1
print("\nКоличество четных чисел:", count_even)

#11. Арифметическая прогрессия с делением на 2
print("Элементы прогрессии после деления на 2 и округления:")
current = 1
d = 3
n = 4
i = 1
while i <= n:
    result = current / 2
    rounded = round(result)
    print(f"a{i} = {current} -> {current}/2 = {result:.1f} -> округлено: {rounded}")
    current += d
    i += 1