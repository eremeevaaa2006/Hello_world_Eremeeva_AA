#!/bin/bash

read -p "Введите имя гена: " NAME
read -p "Введите уровень экспрессии гена (целое число): " LEVEL

if [ -z "$NAME" ] || [ -z "$LEVEL" ]; then 
        echo "Ошибка! Недостаточно данных!"
        exit 1
fi

echo "Экспрессия гена $NAME составляет $LEVEL единиц"
