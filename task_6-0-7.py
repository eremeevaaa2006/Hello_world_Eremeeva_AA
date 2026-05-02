import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")
columns = ['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/var_dev_coe.txt", "w", encoding="utf-8") as file:
    for column in columns:
        file.write(f"{column}")
        file.write(f"\nДисперсия: {df[column].var():.2f}")
        file.write(f"\nСтандартное отклонение: {df[column].std():.2f}")
        file.write(f"\nКоэффициент вариации: {(df[column].std() / df[column].mean()) * 100:.2f}\n\n")

