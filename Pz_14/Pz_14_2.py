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
    to_set = lambda txt: set(w.strip() for w in txt.replace(",", " ").split() if w.strip())
    v, r = to_set(text_voyage.get("1.0", END).strip()), to_set(text_reina.get("1.0", END).strip())

    if not v:
        v = {"Мексика", "Канада", "Израиль", "Италия"}
        text_voyage.delete("1.0", END)
        text_voyage.insert("1.0", "Мексика, Канада, Израиль, Италия")
    if not r:
        r = {"Англия", "Япония", "Канада", "ЮАР"}
        text_reina.delete("1.0", END)
        text_reina.insert("1.0", "Англия, Япония, Канада, ЮАР")

    only_v, only_r, common = v - r, r - v, v & r
    to_str = lambda s: ", ".join(sorted(s)) if s else "нет"

    text_results.config(state=NORMAL)
    text_results.delete("1.0", END)
    text_results.insert(END, f"=" * 55 + "\n\n")
    text_results.insert(END, f"1. Туры только из Вояж:\n   {to_str(only_v)}\n\n")
    text_results.insert(END, f"2. Туры только из РейнаТур:\n   {to_str(only_r)}\n\n")
    text_results.insert(END, f"3. Одинаковые туры:\n   {to_str(common)}\n\n")
    text_results.insert(END, f"4. Перечни равны? {'ДА' if v == r else 'НЕТ'}\n\n")
    text_results.insert(END, "=" * 55)
    text_results.config(state=DISABLED)

    label_info.config(text=f"Вояж:{len(v)} | РейнаТур:{len(r)} | Общих:{len(common)}")


def reset_fields():
    text_voyage.delete("1.0", END)
    text_voyage.insert("1.0", "Мексика, Канада, Израиль, Италия")
    text_reina.delete("1.0", END)
    text_reina.insert("1.0", "Англия, Япония, Канада, ЮАР")
    text_results.config(state=NORMAL)
    text_results.delete("1.0", END)
    text_results.config(state=DISABLED)
    label_info.config(text="Готов к сравнению")


root = Tk()
root.title("Сравнение туров")
root.geometry("700x600")

Label(root, text="Сравнение туристических агентств", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2,
                                                                                      pady=10)
Label(root, text="Введите страны (через пробел или запятую)").grid(row=1, column=0, columnspan=2)

frame_input = LabelFrame(root, text="Введите туры")
frame_input.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=5)

frame_voyage = LabelFrame(frame_input, text="Вояж")
frame_voyage.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
text_voyage = Text(frame_voyage, height=8, width=30)
text_voyage.grid(row=0, column=0, pady=5)
text_voyage.insert("1.0", "Мексика, Канада, Израиль, Италия")

frame_reina = LabelFrame(frame_input, text="РейнаТур")
frame_reina.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
text_reina = Text(frame_reina, height=8, width=30)
text_reina.grid(row=0, column=0, pady=5)
text_reina.insert("1.0", "Англия, Япония, Канада, ЮАР")

frame_input.columnconfigure(0, weight=1)
frame_input.columnconfigure(1, weight=1)

frame_buttons = Frame(root)
frame_buttons.grid(row=3, column=0, columnspan=2, pady=10)
Button(frame_buttons, text="Сравнить", command=compare_tours, padx=20, pady=5).grid(row=0, column=0, padx=10)
Button(frame_buttons, text="Сбросить", command=reset_fields, padx=20, pady=5).grid(row=0, column=1, padx=10)

label_info = Label(root, text="Готов к сравнению")
label_info.grid(row=4, column=0, columnspan=2)

frame_results = LabelFrame(root, text="Результаты")
frame_results.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)
text_results = Text(frame_results, height=12)
text_results.grid(row=0, column=0, sticky="nsew")
text_results.config(state=DISABLED)

frame_results.columnconfigure(0, weight=1)
frame_results.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(5, weight=1)

root.mainloop()