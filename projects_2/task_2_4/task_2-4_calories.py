proteins_weight = int(input("Введите массу белков в продукте (г): "))
fats_weight = int(input("Введите массу жиров в продукте (г): "))
carbohydrates_weight = int(input("Введите массу углеводов в продукте (г): "))

calories = proteins_weight * 4 + fats_weight * 9 + carbohydrates_weight * 4

print(f"Общая энергетическая ценность: {calories} кал")