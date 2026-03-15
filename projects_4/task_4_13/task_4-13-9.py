a = [65, 34, 25, 12, 22, 11, 90]
n = len(a)

i = 0
sum = 0

while i < n:
    if a[i] % 2 != 0:
        sum = sum + a[i]
    i = i + 1

print(f"Сумма всех нечетных элементов в массиве равна {sum}")