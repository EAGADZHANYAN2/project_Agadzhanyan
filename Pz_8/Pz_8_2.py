# № 2
#Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать информацию
#из строки в словарь, найти среднее арифметическое оценок, результаты вывести на
#экран.

text = "петров иван покс-29 5 4 3 2 5 4 4 5 4"

parts = text.split()

student_info = {
    "фамилия": parts,
    "имя": parts [1],
    "номер_покс": parts [2],
    "оценки": [int(x) for x in parts[3:]]
}

average_grade = sum(student_info["оценки"]) / len(student_info["оценки"])

print("Информация о студенте:")
print(f"Фамилия: {student_info['фамилия']}")
print(f"Имя: {student_info['имя']}")
print(f"Номер ПОКС: {student_info['номер_покс']}")
print(f"Оценки: {student_info['оценки']}")
print(f"\nСреднее арифметическое оценок: {average_grade:.2f}")

