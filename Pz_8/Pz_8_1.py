#Вариант 2
# №1 Из словаря my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#удалить 'profession', вывести все пары ключ-значение и проверить наличие 'age'.

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

del my_dict['profession']

print("Все пары ключ-значение после удаления:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

if 'age' in my_dict:
    print("\nКлюч 'age' существует в словаре")
else:
    print("\nКлюча 'age' нет в словаре")
