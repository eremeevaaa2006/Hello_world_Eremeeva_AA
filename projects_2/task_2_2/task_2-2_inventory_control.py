reagent_name = input("Введите название нового реагента: ")
reagent_sum = input("Введите количество реагента (целое число): ")
 
print(f"Реактив '{reagent_name}' поступил на склад в количестве {reagent_sum} шт.")


f = open("C:/Users/Anna/Desktop/eremeeva_aa/projects_2/task_2_2/inventory.txt", "w", encoding="utf-8")
print(f"Реактив '{reagent_name}' поступил на склад в количестве {reagent_sum} шт.", file=f)
f.close()