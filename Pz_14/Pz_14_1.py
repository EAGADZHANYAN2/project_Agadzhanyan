#Вариант 2
#https://professorweb.ru/my/html/html5/level2/files/img46023.jpg

from tkinter import *
from tkinter import messagebox

def submit_form():

    get_name = lambda: entry_name.get()
    get_email = lambda: entry_email.get()
    get_age = lambda: entry_age.get()
    get_gender = lambda: gender_var.get()
    get_qualities = lambda: text_qualities.get("1.0", END).strip()
    get_phone = lambda: entry_phone.get()

    name = get_name()
    email = get_email()
    age = get_age()
    gender = get_gender()
    qualities = get_qualities()
    phone = get_phone()

    is_valid = lambda: bool(name and email and age)
    if not is_valid():
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля (помечены *)")
        return

    get_selected = lambda: [animal for animal in animals if animal_vars[animal].get()]
    selected = get_selected()
    format_animals = lambda lst: ", ".join(lst) if lst else "не выбраны"

    format_result = lambda: (f"Заявка отправлена!\n\n"
                             f"Имя: {name}\n"
                             f"Email: {email}\n"
                             f"Телефон: {phone}\n"
                             f"Возраст: {age}\n"
                             f"Пол: {gender}\n"
                             f"Личные качества: {qualities}\n"
                             f"Любимые животные: {format_animals(selected)}")
    messagebox.showinfo("Результат", format_result())

def close_app():
    root.quit()
    root.destroy()

root = Tk()
root.title("Заявка на работу в зоопарке")
root.geometry("520x700")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Заголовки
title = Label(root, text="Форма заявки на работу в зоопарке",
              font=("Arial", 16, "bold"), fg="black", bg="#f0f0f0")
title.grid(row=0, column=0, columnspan=2, pady=(15, 5))

subtitle = Label(root, text="Пожалуйста, заполните форму. Обязательные поля помечены *",
                 font=("Arial", 9), fg="black", bg="#f0f0f0")
subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 15))

# Контактная информация
frame_contact = LabelFrame(root, text="Контактная информация",
                           font=("Arial", 10, "bold"), bg="white", fg="black",
                           padx=10, pady=10, relief="groove", bd=2)
frame_contact.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

Label(frame_contact, text="Имя *", font=("Arial", 10), bg="white", fg="black").grid(row=0, column=0, sticky="w", pady=5)
entry_name = Entry(frame_contact, width=40, relief="sunken", bd=1)
entry_name.grid(row=0, column=1, pady=5, padx=(10, 0))

Label(frame_contact, text="Телефон", font=("Arial", 10), bg="white", fg="black").grid(row=1, column=0, sticky="w", pady=5)
entry_phone = Entry(frame_contact, width=40, relief="sunken", bd=1)
entry_phone.grid(row=1, column=1, pady=5, padx=(10, 0))

Label(frame_contact, text="Email *", font=("Arial", 10), bg="white", fg="black").grid(row=2, column=0, sticky="w", pady=5)
entry_email = Entry(frame_contact, width=40, relief="sunken", bd=1)
entry_email.grid(row=2, column=1, pady=5, padx=(10, 0))

# Персональная информация
frame_personal = LabelFrame(root, text="Персональная информация",
                            font=("Arial", 10, "bold"), bg="white", fg="black",
                            padx=10, pady=10, relief="groove", bd=2)
frame_personal.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

Label(frame_personal, text="Возраст *", font=("Arial", 10), bg="white", fg="black").grid(row=0, column=0, sticky="w", pady=5)
entry_age = Entry(frame_personal, width=20, relief="sunken", bd=1)
entry_age.grid(row=0, column=1, sticky="w", pady=5, padx=(10, 0))

Label(frame_personal, text="Пол", font=("Arial", 10), bg="white", fg="black").grid(row=1, column=0, sticky="w", pady=5)
gender_var = StringVar(value="Женщина")
frame_gender = Frame(frame_personal, bg="white")
frame_gender.grid(row=1, column=1, sticky="w", padx=(10, 0))
Radiobutton(frame_gender, text="Мужчина", variable=gender_var, value="Мужчина",
            bg="white", activebackground="white", fg="black").pack(side="left")
Radiobutton(frame_gender, text="Женщина", variable=gender_var, value="Женщина",
            bg="white", activebackground="white", fg="black").pack(side="left", padx=(15, 0))

Label(frame_personal, text="Перечислите личные качества", font=("Arial", 10), bg="white", fg="black").grid(row=2, column=0, sticky="nw", pady=5)
text_qualities = Text(frame_personal, width=40, height=4, relief="sunken", bd=1, wrap=WORD)
text_qualities.grid(row=2, column=1, pady=5, padx=(10, 0))

# Любимые животные
frame_animals = LabelFrame(root, text="Выберите ваших любимых животных",
                           font=("Arial", 10, "bold"), bg="white", fg="black",
                           padx=10, pady=10, relief="groove", bd=2)
frame_animals.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
animal_vars = {}

for i, animal in enumerate(animals):
    animal_vars[animal] = BooleanVar()
    row = 0 if i < 4 else 1
    col = i % 4
    Checkbutton(frame_animals, text=animal, variable=animal_vars[animal],
                bg="white", activebackground="white", fg="black").grid(row=row, column=col, sticky="w", pady=5, padx=15)

# Кнопка отправки
btn_submit = Button(root, text="Отправить информацию",
                    bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                    relief="raised", bd=2, padx=20, pady=5, command=submit_form)
btn_submit.grid(row=5, column=0, columnspan=2, pady=20)

# Настройка растягивания колонок
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()