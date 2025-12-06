#Дан список размера N.Найти номера элементов тех список,
# которые больше своего левого соседа, и количество таких элеметов.
#Найденные номера выводить в порядке их убывания.

import random

N = 10
numbers = [random.randint(1, 10) for _ in range(N)]

print(f"Сгенерированный список из {N} элементов:")
print(numbers)

indices = []

for i in range(1, N):
    if numbers[i] > numbers[i - 1]:
        indices.append(i + 1)

print(f"Количество элементов, больших левого соседа: {len(indices)}")

if indices:
    indices.sort(reverse=True)
    print("Номера элементов (в порядке убывания):", end=" ")
    print(*indices)
else:
    print("Нет элементов, больше своего левого соседа.")