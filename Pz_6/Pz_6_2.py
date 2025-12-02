#Дан список размера N.Найти номера элементов тех список,
# которые больше своего левого соседа, и количество таких элеметов.
#Найденные номера выводить в порядке их убывания.

N = int(input("Введите размер списка N: "))

print(f"Введите {N} чисел :")
numbers = list(map(int, input().split()))

if len(numbers) != N:
    print(f"Ошибка! Вы ввели {len(numbers)} чисел вместо {N}")
else:
    indices = []

    for i in range(1, N):
        if numbers[i] > numbers[i - 1]:
            indices.append(i + 1)

    count = len(indices)
    print(f"Количество элементов, больших левого соседа: {count}")

    if count > 0:
        indices.sort(reverse=True)

        print("Номера таких элементов (в порядке убывания):")
        print(' '.join(map(str, indices)))
    else:
        print("Таких элементов нет")