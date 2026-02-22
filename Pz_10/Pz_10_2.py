# 2
# Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме выведя строки в обратном порядке.

t = open('text18-2.txt', 'w', encoding='UTF-8')
t.write('- Да, были люди в наше время,\n')
t.write('Не то, что нынешнее племя:\n')
t.write('Богатыри — не вы!\n')
t.write('Плохая им досталась доля:\n')
t.write('Немногие вернулись с поля…\n')
t.write('Не будь на то господня воля,\n')
t.write('Не отдали б Москвы')
t.close()

p = 0
z = 0
znaki = '.,!?;:-—…()"«»'

print('Содержимое файла text18-2.txt:')
print()

for i in open('text18-2.txt', encoding='UTF-8'):
    print(i, end='')
    for j in i:
        if j in znaki:
            p += 1

print(end='\n')
print('Количество знаков препинания: ', p, end='\n')

f1 = open('text18-2.txt', encoding='UTF-8')
l = f1.readlines()
f1.close()

l = l[::-1]

f2 = open('text18-2-reversed.txt', 'w', encoding='UTF-8')
f2.writelines(l)
f2.close()

print('Создан файл text18-2-reversed.txt со строками в обратном порядке')