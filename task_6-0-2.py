import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")
columns = ['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']
mean_values = df[columns].mean()

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/mean_values.txt", "w", encoding="utf-8") as file:
    for parametr, value in mean_values.items():
        file.write(f"{parametr}: {value:.2f}\n")