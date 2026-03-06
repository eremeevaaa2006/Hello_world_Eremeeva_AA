#!/bin/bash

echo "Название файловой системы и процент ее заполнения:"
df -h | awk 'NR > 1 {
	if ($5 > 90)
		print $1, $5, "WARNING!"
	else
		print $1, $5
}'
