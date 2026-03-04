#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "File" "A" "T" "G" "C"

for file in *.fasta; do
	if [ ! -s "$file" ]; then 
	continue
	fi

seq=$(grep -v "^>" "$file" | tr -d '\n')
a=$(echo "$seq" | grep -o "A" | wc -l)
g=$(echo "$seq" | grep -o "G" | wc -l)
c=$(echo "$seq" | grep -o "C" | wc -l)
t=$(echo "$seq" | grep -o "T" | wc -l)

printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$a" "$t" "$g" "$c"
done
