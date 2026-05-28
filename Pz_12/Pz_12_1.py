#Вариант 2.
#1. В матрице найти минимальный и максимальные элементы
import random

rows, cols = 4, 5
matrix = [[random.randint(-10, 20) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for row in matrix:
    print(" ".join(f"{x:4d}" for x in row))

min_elem = min(x for row in matrix for x in row)
max_elem = max(x for row in matrix for x in row)

print(f"\nМинимальный элемент: {min_elem}")
print(f"Максимальный элемент: {max_elem}")