#!/bin/bash

for i in {1..10}; do
	touch "test$i.txt"
	echo "Создан файл: test$i.txt"
done
echo "Файлы созданы"

i=10
while [ $i -ge 1 ]; do
	rm -f "test$i.txt"
	echo "Удален файл: test$i.txt"
	let "i--"
done
echo "Файлы удалены"

