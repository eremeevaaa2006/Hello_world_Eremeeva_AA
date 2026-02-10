environment_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°С): ")

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_2/task_2_3/recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{environment_name}\nКонцентрация агара: {agar_concentration}%\nТемпература стерилизации: {sterilization_temperature}°C")


print("Файл 'recipe.txt' успешно сформирован!")