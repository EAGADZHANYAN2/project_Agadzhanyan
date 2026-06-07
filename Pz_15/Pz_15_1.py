#Вариант 2
#Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
#которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
#содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
#Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
#выбранная Специальность.

import sqlite3 as sq
from databases import abiturients_data

with sq.connect('abiturient.db') as con:
    abiturient = con.cursor()

    abiturient.execute("DROP TABLE IF EXISTS Анкета")
    abiturient.execute("""CREATE TABLE IF NOT EXISTS Анкета (
        reg_number INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        patronymic TEXT,
        birth_date TEXT NOT NULL,
        awards TEXT CHECK(awards IN ('да', 'нет')) NOT NULL,
        address TEXT NOT NULL,
        specialty TEXT NOT NULL
    )""")

    abiturient.executemany("INSERT INTO Анкета VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", abiturients_data)

    def print_table(title_text):
        print('\n', title_text)
        print(f"{'N':<4} {'Фамилия':<15} {'Имя':<12} {'Отчество':<15} {'Дата рожд.':<12} {'Награды':<7} {'Адрес':<20} {'Специальность':<20}")
        abiturient.execute("SELECT * FROM Анкета")
        for row in abiturient.fetchall():
            reg, last, first, patron, birth, awards, addr, spec = row
            print(f"{reg:<4} {last:<15} {first:<12} {patron:<15} {birth:<12} {awards:<7} {addr:<20} {spec:<20}")

    print_table("Исходное содержимое таблицы Анкета")

    print("\n 1. Абитуриенты со специальностью Информатика:")
    abiturient.execute("SELECT last_name, first_name, specialty FROM Анкета WHERE specialty = 'Информатика'")
    for row in abiturient.fetchall():
        print(f" - {row[0]} {row[1]} ({row[2]})")

    print("\n 2. Абитуриенты с наградами:")
    abiturient.execute("SELECT last_name, first_name, awards FROM Анкета WHERE awards = 'да'")
    for row in abiturient.fetchall():
        print(f" - {row[0]} {row[1]} (Награды: {row[2]})")

    print("\n 3. Абитуриенты 2000 года рождения:")
    abiturient.execute("SELECT last_name, first_name, birth_date FROM Анкета WHERE birth_date LIKE '2000%'")
    for row in abiturient.fetchall():
        print(f" - {row[0]} {row[1]} (Дата: {row[2]})")

    abiturient.execute("UPDATE Анкета SET awards = 'да' WHERE specialty = 'Математика'")

    abiturient.execute("UPDATE Анкета SET specialty = 'Программирование' WHERE specialty = 'Информатика'")

    abiturient.execute("UPDATE Анкета SET address = 'ул. Центральная, 1' WHERE last_name = 'Петрова'")

    print_table("Таблица после проведения 3-х операций редактирования")

    abiturient.execute("DELETE FROM Анкета WHERE last_name = 'Морозов'")

    abiturient.execute("DELETE FROM Анкета WHERE reg_number = 8")

    abiturient.execute("DELETE FROM Анкета WHERE awards = 'нет' AND specialty = 'Экономика'")

    print_table("Итоговая таблица после проведения 3-х операций удаления")