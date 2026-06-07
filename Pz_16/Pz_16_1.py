#Вариант 2.
#Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент отличником.

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        average = sum(self.grades) / len(self.grades)
        print(f"Средний балл студента {self.first_name} {self.last_name}: {average:.2f}")
        return average

    def is_excellent(self):
        average = self.calculate_average()
        if average >= 4.5:
            print(f"Студент {self.first_name} {self.last_name} является отличником.")
            return True
        else:
            print(f"Студент {self.first_name} {self.last_name} не является отличником.")
            return False

try:
    first_name = input("Введите имя студента: ")
    last_name = input("Введите фамилию студента: ")
    grades_input = input("Введите оценки через пробел (например: 5 4 5 5 3): ")

    grades_list = []
    for grade in grades_input.split():
        grades_list.append(float(grade))

    my_student = Student(first_name, last_name, grades_list)
    my_student.is_excellent()

except ValueError:
    print("Ошибка: оценки должны быть числами.")
    exit()