#Дан список размера N.Обнулить элементы списка,
# рассположенные между его минимальным и максимальным элементами
# (не включая минимальный и максимальный элементы)

N = int(input("Введите размер списка N: "))

numbers = list(map(int, input(f"Введите {N} чисел : ").split()))

if len(numbers) == N:
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    print(f"Минимальный элемент: {numbers[min_index]} на позиции {min_index + 1}")
    print(f"Максимальный элемент: {numbers[max_index]} на позиции {max_index + 1}")

    left = min(min_index, max_index)
    right = max(min_index, max_index)

    print(f"Обнуляем элементы между позициями {left + 2} и {right} (не включая границы)")

    for i in range(left + 1, right):
        numbers[i] = 0

    print("Результат:")
    print(numbers)