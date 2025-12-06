#Дан список размера N.Обнулить элементы списка,
# рассположенные между его минимальным и максимальным элементами
# (не включая минимальный и максимальный элементы)

import random

N = 10
numbers = [random.randint(1, 15) for _ in range(N)]

print(f"Случайный список: {numbers}")

min_idx = 0
max_idx = 0

for i in range(1, N):
    if numbers[i] < numbers[min_idx]:
        min_idx = i
    if numbers[i] > numbers[max_idx]:
        max_idx = i

print(f"Минимальный элемент: {numbers[min_idx]} (индекс {min_idx})")
print(f"Максимальный элемент: {numbers[max_idx]} (индекс {max_idx})")

start = min(min_idx, max_idx) + 1
end = max(min_idx, max_idx)

for i in range(start, end):
    numbers[i] = 0

print(f"После обнуления: {numbers}")