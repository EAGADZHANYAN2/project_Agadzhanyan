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

DEFAULT_V = "Мексика, Канада, Израиль, Италия"
DEFAULT_R = "Англия, Япония, Канада, ЮАР"

def get_set(text_widget, default_str):
    val = text_widget.get("1.0", END).strip()
    if not val:
        text_widget.delete("1.0", END)
        text_widget.insert("1.0", default_str)
        val = default_str
    return set(w.strip() for w in val.replace(",", " ").split() if w.strip())

def compare_tours():
    v = get_set(text_voyage, DEFAULT_V)
    r = get_set(text_reina, DEFAULT_R)

    only_v, only_r, common = v - r, r - v, v & r
    to_str = lambda s: ", ".join(sorted(s)) if s else "нет"

    res = (
        f"1. Туры только из Вояж:\n   {to_str(only_v)}\n\n"
        f"2. Туры только из РейнаТур:\n   {to_str(only_r)}\n\n"
        f"3. Одинаковые туры:\n   {to_str(common)}\n\n"
        f"4. Перечни равны? {'ДА' if v == r else 'НЕТ'}\n\n"
    )

    text_results.config(state=NORMAL)
    text_results.delete("1.0", END)
    text_results.insert("1.0", res)
    text_results.config(state=DISABLED)

    label_info.config(text=f"Вояж: {len(v)} | РейнаТур: {len(r)} | Общих: {len(common)}")


def reset_fields():
    text_voyage.delete("1.0", END)
    text_voyage.insert("1.0", DEFAULT_V)
    text_reina.delete("1.0", END)
    text_reina.insert("1.0", DEFAULT_R)

    text_results.config(state=NORMAL)
    text_results.delete("1.0", END)
    text_results.config(state=DISABLED)
    label_info.config(text="Готов к сравнению")

# Интерфейс
root = Tk()
root.title("Сравнение туров")
root.geometry("650x580")

Label(root, text="Сравнение туристических агентств", font=("Arial", 14, "bold")).pack(pady=5)
Label(root, text="Введите страны (через пробел или запятую)", fg="gray").pack(pady=2)

frame_input = LabelFrame(root, text=" Введите туры ", padx=10, pady=10)
frame_input.pack(fill=X, padx=15, pady=5)

# Блок Вояж
f_voyage = Frame(frame_input)
f_voyage.pack(side=LEFT, expand=True, fill=BOTH, padx=5)
Label(f_voyage, text="Вояж").pack(anchor=W)
text_voyage = Text(f_voyage, height=6, width=25)
text_voyage.pack(fill=BOTH, expand=True)
text_voyage.insert("1.0", DEFAULT_V)

# Блок РейнаТур
f_reina = Frame(frame_input)
f_reina.pack(side=RIGHT, expand=True, fill=BOTH, padx=5)
Label(f_reina, text="РейнаТур").pack(anchor=W)
text_reina = Text(f_reina, height=6, width=25)
text_reina.pack(fill=BOTH, expand=True)
text_reina.insert("1.0", DEFAULT_R)

# Кнопки управления
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)
Button(frame_buttons, text="Сравнить", command=compare_tours, width=15, bg="#e1e1e1").pack(side=LEFT, padx=5)
Button(frame_buttons, text="Сбросить", command=reset_fields, width=15).pack(side=LEFT, padx=5)

label_info = Label(root, text="Готов к сравнению", font=("Arial", 10, "italic"))
label_info.pack(pady=2)

# Блок результатов
frame_results = LabelFrame(root, text=" Результаты ")
frame_results.pack(fill=BOTH, expand=True, padx=15, pady=10)
text_results = Text(frame_results, height=10, state=DISABLED, bg="#f9f9f9")
text_results.pack(fill=BOTH, expand=True, padx=5, pady=5)

root.mainloop()