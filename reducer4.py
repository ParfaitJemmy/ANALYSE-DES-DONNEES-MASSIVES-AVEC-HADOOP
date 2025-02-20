#!/usr/bin/env python3
import sys

total_sales = 0  # Somme des ventes
total_transactions = 0  # Nombre de transactions

# Lire l'entrée ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Séparer la ligne en éléments
    parts = line.split("\t")

    if len(parts) != 3:
        continue  # Ignorer les lignes mal formatées

    try:
        amount = float(parts[1])
        count = int(parts[2])

        total_sales += amount
        total_transactions += count
    except ValueError:
        continue

# Calculer la moyenne
if total_transactions > 0:
    avg_sales = total_sales / total_transactions
    print(f"Vente moyenne par transaction : {avg_sales:.2f}")
else:
    print("Aucune transaction trouvée")


