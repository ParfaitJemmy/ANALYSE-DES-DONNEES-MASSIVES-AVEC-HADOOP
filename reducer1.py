#!/usr/bin/env python3
import sys

current_city = None
total_sales = 0

# Lecture des résultats du Mapper
for line in sys.stdin:
    # Supprimer les espaces inutiles et diviser la ligne en clé et valeur
    line = line.strip()
    city, amount = line.split('\t')
    amount = float(amount)

    # Si la ville change, émettre le résultat précédent
    if current_city != city:
        if current_city:
            print(f"{current_city}\t{total_sales}")
        current_city = city
        total_sales = 0

    # Ajouter le montant au total de la ville
    total_sales += amount

# Émettre la dernière ville
if current_city:
    print(f"{current_city}\t{total_sales}")