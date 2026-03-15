a = [64, 34, 25, 12, 22, 11, 90]
n = len(a)

i = 0
sum = 0

while i < n:
    sum = sum + a[i]
    i = i + 1

medium = round(sum / n, 2)
print(f"Среднее арифметическое элементов массива равно {medium}")
