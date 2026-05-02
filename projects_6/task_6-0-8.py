import pandas as pd
df = pd.read_csv("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/wild_boars.csv")

tusk_length = (df.groupby('gender')['tusk_length_cm'].std() / df.groupby('gender')['tusk_length_cm'].mean()) * 100

with open("C:/Users/Anna/Desktop/eremeeva_aa/projects_6/tusk_length.txt", "w", encoding="utf-8") as file:
    file.write(f"Male:\nДлина клыков, коэффициент вариации: {tusk_length['Male']:.2f} cm")
    file.write(f"\n\nFemale:\nДлина клыков, коэффициент вариации: {tusk_length['Female']:.2f} cm")