import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")

q1 = df.groupby('gender')['length_cm'].quantile(0.25)
q3 = df.groupby('gender')['length_cm'].quantile(0.75)
iqr = q3 - q1

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/interquartile_range.txt", "w", encoding="utf-8") as file:
    file.write(f"Male:\nQ1 (25%): {q1['Male']:.1f} cm\nQ3 (75%): {q3['Male']:.1f} cm\nIQR: {iqr['Male']:.2f} cm")
    file.write(f"\n\nFemale:\nQ1 (25%): {q1['Female']:.1f} cm\nQ3 (75%): {q3['Female']:.1f} cm\nIQR: {iqr['Female']:.2f} cm")