#Вариант 2.
#1. Организовать и вывести последовательность А из n чисел (n - четное). Из
#последовательности А получить две последовательности В и С: в последовательности В –
#первая половина элементов А, в С – вторая половина элементов А. Найти произведение
#соответствующих элементов последовательностей В и С. Найти среднее арифметической
#полученной последовательности.

import random
from functools import reduce

n = 8
A = list(map(lambda _: random.randint(1, 20), range(n)))

print("A =", A)

mid = n // 2
B = A[:mid]
C = A[mid:]

print("B =", B)
print("C =", C)

products = list(map(lambda x, y: x * y, B, C))
print("Произведения =", products)

total = reduce(lambda acc, x: acc + x, products, 0)
average = total / len(products) if products else 0
print(f"Среднее = {average:.2f}")