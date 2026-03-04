#!/bin/bash

read -p "Введите ваш рост (см): " HEIGHT
read -p "Введите ваш вес (кг): " WEIGHT

BMI=$((WEIGHT * 10000 / (HEIGHT * HEIGHT)))

echo "Ваш индекс маccы тела равен ${BMI%.*}"


