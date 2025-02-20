#!/usr/bin/env python3
import sys

current_hour = None
total_sales = 0

# Lire l'entrée ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Séparer la ligne en heure et montant
    parts = line.split("\t")

    if len(parts) != 2:
        continue  

    try:
        hour = parts[0]
        amount = float(parts[1])

        # Si on change d'heure, afficher le total précédent
        if current_hour and current_hour != hour:
            print(f"{current_hour}:00 - {current_hour}:59\t{total_sales:.2f}")
            total_sales = 0

        current_hour = hour
        total_sales += amount
    except ValueError:
        continue  

# Afficher la dernière heure traitée
if current_hour:
    print(f"{current_hour}:00 - {current_hour}:59\t{total_sales:.2f}")
