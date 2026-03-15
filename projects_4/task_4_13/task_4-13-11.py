a = [65, 34, 25, 12, 22, 11, 90]
n = len(a)

i = 0
sum = 0
count = 0

while i < n:
    sum = sum + a[i]
    count = count + 1
    i = i + 2

if count > 0:
    medium = round(sum / count, 2)
else:
    medium = 0

print(f"Среднее арифметическое элементов с четными индексами в массиве равно {medium}")