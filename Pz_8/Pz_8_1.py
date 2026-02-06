#Вариант 2
# №1 Из словаря my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#удалить 'profession', вывести все пары ключ-значение и проверить наличие 'age'.

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

if 'age' in my_dict:
    print("Ключ 'age' существует в словаре")
else:
    print("Ключа 'age' нет в словаре")
try:
    my_dict.pop('profession')
    print("Ключ 'profession' успешно удален")
except KeyError:
    print("Ключ 'profession' не найден в словаре, удаление не выполнено")

print("Все пары ключ-значение после удаления:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

