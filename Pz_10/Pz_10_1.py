# 1
# Средствами языка Python сформировать текстовый файл (.txt) содержащий
# последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Произведение элементов меньших 0 в первой половине:

l = ['-15 23 -7 34 -42 18 -5 29 -11 8 -3 16 -9 12 -6 25 -14 31 -2 19']

f3 = open('data_2.txt', 'w', encoding='utf-8')
f3.writelines(l)
f3.close()

f4 = open('data_2-1.txt', 'w', encoding='utf-8')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

f3 = open('data_2.txt', encoding='utf-8')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

max_element, p, t = 0, 1, 0
half = len(k) // 2

for i in range(len(k)):
    if k[i] > max_element:
        max_element = k[i]

for i in range(half):
    if k[i] < 0:
        p *= k[i]
        t += 1

if t == 0:
    p = 0

f4 = open('data_2-1.txt', 'a', encoding='utf-8')
f4.write('\n')
print('Количество элементов: ', len(k), file=f4)
print('Максимальный элемент: ', max_element, file=f4)
print('Произведение элементов меньших 0 в первой половине: ', p, file=f4)
f4.close()

print('Исходные данные:', ' '.join(map(str, k)))
print('Количество элементов:', len(k))
print('Максимальный элемент:', max_element)
print('Произведение элементов меньших 0 в первой половине:', p)