import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")
columns = ['age_years', 'weight_kg', 'length_cm', 'shoulder_height_cm', 'tusk_length_cm', 'litter_size', 'health_score', 'territory_ha']

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/percentiles.txt", "w", encoding="utf-8") as file:
    for column in columns:
       file.write(f'{column}:')
       file.write(f"\nPercentile 25 (Q1):\t{df[column].quantile(0.25):.1f} kg")
       file.write(f"\nMedian 50 (Q2):\t{df[column].quantile(0.50):.1f} kg")
       file.write(f"\nPercentile 75 (Q3):\t{df[column].quantile(0.75):.1f} kg")
       file.write(f"\nPercentile 90:\t{df[column].quantile(0.90):.1f} kg")
       file.write(f"\nPercentile 95:\t{df[column].quantile(0.95):.1f} kg")
       file.write(f"\nMax:\t{df[column].quantile(1.00):.1f} kg\n\n")