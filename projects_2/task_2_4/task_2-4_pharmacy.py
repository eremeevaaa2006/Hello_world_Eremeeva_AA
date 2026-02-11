capsules_sum = int(input("Введите общее количество произведенных капсул: "))
packaging_capacity = int(input("Введите количество капсул в одной упаковке: "))

packaging_sum = capsules_sum // packaging_capacity
capsules_remain = capsules_sum % packaging_capacity

print("\n---Отчет фасовочного цеха---")
print(f"Полных упаковок: {packaging_sum}\nОстаток капсул:\t {capsules_remain}")
