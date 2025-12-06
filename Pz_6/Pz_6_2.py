#Дан список размера N.Найти номера элементов тех список,
# которые больше своего левого соседа, и количество таких элеметов.
#Найденные номера выводить в порядке их убывания.

N = 10
numbers = list(range(1, N + 1))

print(f"Список из {N} последовательных элементов:")
print(numbers)

indices = []

for i in range(1, N):
    if numbers[i] > numbers[i - 1]:
        indices.append(i + 1)

print(f"Количество элементов, больших левого соседа: {len(indices)}")

if indices:
    indices.sort(reverse=True)
    print("Номера элементов (в порядке убывания):", *indices)
else:
    print("Нет элементов, больших своего левого соседа.")
