dna = input("Введите последовательность ДНК: ")
dna_up = dna.upper()

count_A = dna_up.count("A")
count_T = dna_up.count("T")
count_G = dna_up.count("G")
count_C = dna_up.count("C")

sum_dna = count_A + count_T + count_C + count_G
percent_A = round((count_A / sum_dna) * 100, 2)
percent_T = round((count_T / sum_dna) * 100, 2)
percent_G = round((count_G / sum_dna) * 100, 2)
percent_C = round((count_C / sum_dna) * 100, 2)

print("\n== Анализ последовательности ДНК ==")
print(f"\nПоследовательность ДНК: {dna}")
print(f"\nПоследовательность в верхнем регистре: {dna_up}")
print(f"\nПодсчет нуклеотидов:\nA: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}")
print(f"\nОбщая длина строки: {sum_dna}")
print(f"\nПроцентное содержание нуклеотидов:\nA: {percent_A} %\nT: {percent_T} %\nG: {percent_G} %\nC: {percent_C} %")
