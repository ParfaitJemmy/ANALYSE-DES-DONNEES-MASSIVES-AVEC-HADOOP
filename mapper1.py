#!/usr/bin/env python3
import sys

# Lecture de l'entrée ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces inutiles et diviser la ligne en colonnes
    line = line.strip()
    columns = line.split()

    # Extraire la ville (3ème colonne) et le montant (5ème colonne)
    city = columns[2]
    amount = float(columns[5])

    # Émettre la paire clé-valeur (ville, montant)
    print(f"{city}\t{amount}")