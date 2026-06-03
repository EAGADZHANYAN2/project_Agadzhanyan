#Сравнение туров
#Вариант 2.
#Туристические агентства предлагают следующие туры. Вояж – Мексика, Канада, Израиль,
#Италия. РейнаТур – Англия, Япония, Канада, ЮАР. Определить:
#1. какие туры из Вояж, отсутствуют в РейнаТур.
#2. какие товары из РейнаТур, отсутствуют в Вояж
#3. перечень одинаковых туров.
#4. равны ли перечни туров

#voyage = {"Мексика", "Канада", "Израиль", "Италия"}
#reina_tur = {"Англия", "Япония", "Канада", "ЮАР"}

#print("1. Туры из Вояж, отсутствующие в РейнаТур:", voyage - reina_tur)

#print("2. Туры из РейнаТур, отсутствующие в Вояж:", reina_tur - voyage)

#print("3. Одинаковые туры:", voyage & reina_tur)

#print("4. Перечни туров равны?", voyage == reina_tur)

from tkinter import *
from tkinter import messagebox

def compare_tours():

    voyage_text = text_voyage.get("1.0", END).strip()
    reina_text = text_reina.get("1.0", END).strip()

    text_to_set = lambda txt: set([word.strip() for word in txt.replace(",", " ").split() if word.strip()])

    voyage = text_to_set(voyage_text)
    reina_tur = text_to_set(reina_text)

    default_voyage = lambda: {"Мексика", "Канада", "Израиль", "Италия"}
    default_reina = lambda: {"Англия", "Япония", "Канада", "ЮАР"}

    if not voyage:
        voyage = default_voyage()
        text_voyage.delete("1.0", END)
        text_voyage.insert("1.0", "Мексика, Канада, Израиль, Италия")

    if not reina_tur:
        reina_tur = default_reina()
        text_reina.delete("1.0", END)
        text_reina.insert("1.0", "Англия, Япония, Канада, ЮАР")

    only_voyage = voyage - reina_tur
    only_reina = reina_tur - voyage
    common = voyage & reina_tur
    are_equal = (voyage == reina_tur)

    set_to_str = lambda s: ", ".join(sorted(s)) if s else "нет"
    equal_str = lambda: "ДА, перечни одинаковые" if are_equal else "НЕТ, перечни разные"

    # Очистка и вывод результатов
    text_results.config(state=NORMAL)
    text_results.delete("1.0", END)

    text_results.insert(END, "=" * 55 + "\n\n")
    text_results.insert(END, "1. Туры только из Вояж (отсутствуют в РейнаТур):\n")
    text_results.insert(END, f"   {set_to_str(only_voyage)}\n\n")
    text_results.insert(END, "2. Туры только из РейнаТур (отсутствуют в Вояж):\n")
    text_results.insert(END, f"   {set_to_str(only_reina)}\n\n")
    text_results.insert(END, "3. Одинаковые туры (есть в обоих агентствах):\n")
    text_results.insert(END, f"   {set_to_str(common)}\n\n")
    text_results.insert(END, "4. Перечни туров равны?\n")
    text_results.insert(END, f"   {equal_str()}\n\n")
    text_results.insert(END, "=" * 55)

    text_results.config(state=DISABLED)

    label_info.config(text=f"Всего туров: Вояж={len(voyage)}, РейнаТур={len(reina_tur)} | Общих: {len(common)}")

def reset_fields():

    text_voyage.delete("1.0", END)
    text_voyage.insert("1.0", "Мексика, Канада, Израиль, Италия")

    text_reina.delete("1.0", END)
    text_reina.insert("1.0", "Англия, Япония, Канада, ЮАР")

    text_results.config(state=NORMAL)
    text_results.delete("1.0", END)
    text_results.config(state=DISABLED)

    label_info.config(text="Готов к сравнению. Нажмите 'Сравнить'")


def close_app():

    root.quit()
    root.destroy()

root = Tk()
root.title("Сравнение туров: Вояж vs РейнаТур")
root.geometry("700x600")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Заголовки
title = Label(root, text="Сравнение туристических агентств",
              font=("Arial", 16, "bold"), fg="darkblue", bg="#f0f0f0")
title.grid(row=0, column=0, columnspan=2, pady=10)

subtitle = Label(root, text="Введите названия стран (через пробел или запятую)",
                 font=("Arial", 9), fg="gray", bg="#f0f0f0")
subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Рамка для ввода туров
frame_input = LabelFrame(root, text="Введите туры", font=("Arial", 10, "bold"),
                         bg="white", padx=10, pady=10, relief="groove", bd=2)
frame_input.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=5)

# Вояж (слева)
frame_voyage = LabelFrame(frame_input, text="Вояж (туры)", font=("Arial", 10, "bold"),
                          fg="green", bg="white", padx=10, pady=10)
frame_voyage.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

Label(frame_voyage, text="Введите туры:", font=("Arial", 9), bg="white").grid(row=0, column=0, sticky="w")
text_voyage = Text(frame_voyage, height=8, width=30, font=("Arial", 10), wrap=WORD)
text_voyage.grid(row=1, column=0, pady=5)
text_voyage.insert("1.0", "Мексика, Канада, Израиль, Италия")

# РейнаТур (справа)
frame_reina = LabelFrame(frame_input, text="РейнаТур (туры)", font=("Arial", 10, "bold"),
                         fg="blue", bg="white", padx=10, pady=10)
frame_reina.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

Label(frame_reina, text="Введите туры:", font=("Arial", 9), bg="white").grid(row=0, column=0, sticky="w")
text_reina = Text(frame_reina, height=8, width=30, font=("Arial", 10), wrap=WORD)
text_reina.grid(row=1, column=0, pady=5)
text_reina.insert("1.0", "Англия, Япония, Канада, ЮАР")

# Настройка растягивания
frame_input.columnconfigure(0, weight=1)
frame_input.columnconfigure(1, weight=1)
frame_input.rowconfigure(0, weight=1)

# Кнопки
frame_buttons = Frame(root, bg="#f0f0f0")
frame_buttons.grid(row=3, column=0, columnspan=2, pady=10)

btn_calc = Button(frame_buttons, text="Сравнить", bg="lightblue", font=("Arial", 10, "bold"),
                  padx=20, pady=5, command=compare_tours)
btn_calc.grid(row=0, column=0, padx=10)

btn_reset = Button(frame_buttons, text="Сбросить", bg="lightgray", font=("Arial", 10),
                   padx=20, pady=5, command=reset_fields)
btn_reset.grid(row=0, column=1, padx=10)

# Информационная строка
label_info = Label(root, text="Готов к сравнению. Нажмите 'Сравнить'",
                   font=("Arial", 9), fg="darkgreen", bg="#f0f0f0")
label_info.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Рамка для результатов
frame_results = LabelFrame(root, text="Результаты сравнения", font=("Arial", 11, "bold"),
                           bg="white", padx=10, pady=10, relief="groove", bd=2)
frame_results.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

text_results = Text(frame_results, height=12, font=("Courier", 10), wrap=WORD)
text_results.grid(row=0, column=0, sticky="nsew")
text_results.config(state=DISABLED)

# Настройка растягивания
frame_results.columnconfigure(0, weight=1)
frame_results.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(5, weight=1)

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()