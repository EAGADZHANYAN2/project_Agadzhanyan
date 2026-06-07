#Вариант 2.
#Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
#Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
#"Человек". Каждый класс должен иметь метод, который выводит информацию о поле объекта.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_gender_info(self):
        print(f"Пол: {self.gender}")
        return self.gender

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Мужской")

    def get_gender_info(self):
        print(f"Пол: Мужской")
        return "Мужской"

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Женский")

    def get_gender_info(self):
        print(f"Пол: Женский")
        return "Женский"

try:
    person_type = input("Кого вы хотите создать (мужчина/женщина/человек): ").strip().lower()
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))

    if person_type == "мужчина":
        person = Man(name, age)
    elif person_type == "женщина":
        person = Woman(name, age)
    else:
        gender = input("Введите пол: ")
        person = Human(name, age, gender)

    print(f"\nИмя: {person.name}, Возраст: {person.age}")
    person.get_gender_info()

except ValueError:
    print("Ошибка: возраст должен быть числом.")
    exit()