solution_volume = float(input("Введите необходимый объем раствора (мл): "))
salt_mass = round(solution_volume * 0.009, 2)
water_volume = solution_volume

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_2/task_2_4/recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write(f"-" * 23)
    file.write(f"\nОбщий объем:\t{solution_volume} мл\nМасса соли:\t\t{salt_mass} г \nОбъем воды:\t\t{water_volume} мл")

