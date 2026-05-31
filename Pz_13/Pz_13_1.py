#Вапмант2
#Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
#произведения ими написанные. Посчитать общее количество произведений в данном файле.

import re

with open("writer.txt", "r", encoding="utf-8") as f:
    text = f.read()

writers = re.findall(r"([А-ЯЁ][а-яё]+)\s*\((\d{4})-(\d{4})\)", text)

works = re.findall(r'«([^»]+)»|"([^"]+)"', text)
clean_works = list(dict.fromkeys([w[0] or w[1] for w in works]))

print("Писатели и годы жизни:")
list(map(lambda w: print(f"  {w[0]} ({w[1]}-{w[2]})"), writers))

print("\nПроизведения:")
list(map(lambda x: print(f"  {x[0]+1}. {x[1]}"), enumerate(clean_works)))

print(f"\nОбщее количество произведений: {len(clean_works)}")