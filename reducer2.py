#!/usr/bin/env python3
import sys

current_category = None
current_total  = 0.0

# Lecture des résultats du Mapper ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Vérifier que la ligne contient une tabulation avant de séparer
    if '\t' not in line:
        continue  # Ignorer les lignes mal formatées

    try:
        product, amount = line.split('\t')
        amount = float(amount)  # Convertir en float
    except ValueError:
        continue  # Ignorer les lignes où le montant est invalide

    # Si la ville change, afficher l'ancienne et réinitialiser
    if current_category and current_category != product:
        print(f"{current_category}\t{current_total}")
        current_total = 0.0  # Réinitialiser le total

    current_category = product
    current_total += amount  # Ajouter au total de la ville

# Afficher la dernière ville après la boucle
if current_category:
    print(f"{current_category}\t{current_total}")
