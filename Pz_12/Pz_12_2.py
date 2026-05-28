#2. В матрице найти сумму отрицательных элементов в первой трети матрицы.
import random

rows, cols = 6, 4
matrix = [[random.randint(-10, 20) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for row in matrix:
    print(" ".join(f"{x:4d}" for x in row))

third = rows // 3
if third == 0:
    sum_neg = 0
    print(f"\nВ матрице меньше 3 строк (rows={rows}), сумма отрицательных = {sum_neg}")
else:
    sum_neg = sum(x for row in matrix[:third] for x in row if x < 0)
    print(f"\nСумма отрицательных элементов в первой трети (первые {third} строк): {sum_neg}")
