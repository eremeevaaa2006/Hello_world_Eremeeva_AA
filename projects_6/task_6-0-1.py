import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")

min_tusk = df['tusk_length_cm'].min()
max_tusk = df['tusk_length_cm'].max()

print(f"Самые короткие клыки: {min_tusk} см")
print(f"Самые длинные клыки: {max_tusk} см")