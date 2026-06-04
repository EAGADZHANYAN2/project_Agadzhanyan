#Вариант 2
#https://professorweb.ru/my/html/html5/level2/files/img46023.jpg

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    qualities = text_qualities.get("1.0", END).strip()
    phone = entry_phone.get()

    if not (name and email and age):
        messagebox.showerror("Ошибка", "Заполните обязательные поля (*)")
        return

    selected = [animal for animal in animals if animal_vars[animal].get()]
    animals_str = ", ".join(selected) if selected else "не выбраны"

    messagebox.showinfo("Результат",
        f"Заявка отправлена!\n\nИмя: {name}\nEmail: {email}\nТелефон: {phone}\n"
        f"Возраст: {age}\nПол: {gender}\nЛичные качества: {qualities}\n"
        f"Любимые животные: {animals_str}")

def close_app():
    root.quit()
    root.destroy()

root = Tk()
root.title("Заявка на работу в зоопарке")
root.geometry("520x700")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Заголовки
Label(root, text="Форма заявки на работу в зоопарке",
      font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(15, 5))

Label(root, text="Пожалуйста, заполните форму. Обязательные поля помечены *",
      font=("Arial", 9)).grid(row=1, column=0, columnspan=2, pady=(0, 15))

# Контактная информация
frame_contact = LabelFrame(root, text="Контактная информация", font=("Arial", 10, "bold"))
frame_contact.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

Label(frame_contact, text="Имя *", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_name = Entry(frame_contact, width=40)
entry_name.grid(row=0, column=1, pady=5, padx=(10, 0))

Label(frame_contact, text="Телефон", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_phone = Entry(frame_contact, width=40)
entry_phone.grid(row=1, column=1, pady=5, padx=(10, 0))

Label(frame_contact, text="Email *", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
entry_email = Entry(frame_contact, width=40)
entry_email.grid(row=2, column=1, pady=5, padx=(10, 0))

# Персональная информация
frame_personal = LabelFrame(root, text="Персональная информация", font=("Arial", 10, "bold"))
frame_personal.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

Label(frame_personal, text="Возраст *", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_age = Entry(frame_personal, width=20)
entry_age.grid(row=0, column=1, sticky="w", pady=5, padx=(10, 0))

# Пол (выпадающий список Combobox)
Label(frame_personal, text="Пол", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
gender_var = StringVar(value="Женщина")
gender_combo = ttk.Combobox(frame_personal, textvariable=gender_var,
                            values=["Мужчина", "Женщина"], width=18, state="readonly")
gender_combo.grid(row=1, column=1, sticky="w", pady=5, padx=(10, 0))

# Перечислите личные качества (ВЕРНУЛИ)
Label(frame_personal, text="Перечислите личные качества", font=("Arial", 10)).grid(row=2, column=0, sticky="nw", pady=5)
text_qualities = Text(frame_personal, width=40, height=4)
text_qualities.grid(row=2, column=1, pady=5, padx=(10, 0))

# Любимые животные
frame_animals = LabelFrame(root, text="Выберите ваших любимых животных", font=("Arial", 10, "bold"))
frame_animals.grid(row=4, column=0, columnspan=2, sticky="ew", padx=20, pady=5)

animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
animal_vars = {}

for i, animal in enumerate(animals):
    animal_vars[animal] = BooleanVar()
    row = 0 if i < 4 else 1
    col = i % 4
    Checkbutton(frame_animals, text=animal, variable=animal_vars[animal]).grid(row=row, column=col, sticky="w", pady=5, padx=15)

# Кнопка отправки
Button(root, text="Отправить информацию", bg="#4CAF50", fg="white",
       font=("Arial", 11, "bold"), command=submit_form).grid(row=5, column=0, columnspan=2, pady=20)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()