#!/bin/bash

echo "1.Студенты с оценкой выше 80"
awk '{
	if ($2 > 80)
	print $1
}' students.txt

echo "2.Студенты с оценкой ниже 70"
awk '{
	if ($2 < 70)
	print $1
}' students.txt

echo "3.Только первая строка файла"
awk 'NR ==1' students.txt
