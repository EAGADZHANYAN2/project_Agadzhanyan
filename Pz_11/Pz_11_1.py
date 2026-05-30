#Вариант 2.
#1. Организовать и вывести последовательность А из n чисел (n - четное). Из
#последовательности А получить две последовательности В и С: в последовательности В –
#первая половина элементов А, в С – вторая половина элементов А. Найти произведение
#соответствующих элементов последовательностей В и С. Найти среднее арифметической
#полученной последовательности.

import random

n = int(input("Введите четное количество элементов n: "))
while n % 2 != 0:
    n = int(input("Ошибка! n должно быть четным."))

A = list(map(lambda _: random.randint(1, 20), range(n)))

print("A =", A)
mid = n // 2
B = A[:mid]
C = A[mid:]

print("B =", B)
print("C =", C)

products = list(map(lambda x, y: x * y, B, C))
print("Произведения =", products)

total = sum(products)
average = total / len(products) if products else 0
print(f"Среднее = {average:.2f}")