import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")
columns = ['gender', 'age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/mode_values.txt", "w", encoding="utf-8") as file:
    for column in columns:
        mode_values = df[column].mode()
        if len(mode_values) > 0:
            modes_list = []
            for mode in mode_values:
                modes_list.append(str(mode))
            modes = ','.join(modes_list)
            file.write(f"{column}: {modes}\n")
        else:
            file.write(f"{column}: нет моды\n")