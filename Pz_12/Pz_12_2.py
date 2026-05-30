# Вариант 2.
# 2. В матрице найти сумму отрицательных элементов в первой трети матрицы.
import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

min_val = int(input("Введите минимальное значение элемента: "))
max_val = int(input("Введите максимальное значение элемента: "))

matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

print("\nСгенерированная матрица:")
for row in matrix:
    print(" ".join(f"{x:4d}" for x in row))

third = rows // 3

if third == 0:
    sum_neg = 0
    print(f"\nВ матрице меньше 3 строк (rows={rows})")
    print(f"Первая треть не содержит ни одной строки")
    print(f"Сумма отрицательных элементов = {sum_neg}")
else:
    sum_neg = sum(x for row in matrix[:third] for x in row if x < 0)
    print(f"\nПервая треть матрицы включает первые {third} строк(и)")
    print(f"Сумма отрицательных элементов: {sum_neg}")