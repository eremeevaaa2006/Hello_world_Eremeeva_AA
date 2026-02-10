operator_name = input("Введите имя оператора: ")
pressure_sensor_value = input("Введите текущее значение давления (Па): ")

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_2/task_2_3/sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"ИМЯ ОПЕРАТОРА:\t\t\t\t{operator_name}\nЗНАЧЕНИЕ ДАТЧИКА ДАВЛЕНИЯ:\t{pressure_sensor_value}")


print("Данные успешно сохранены в sensor_log.txt")