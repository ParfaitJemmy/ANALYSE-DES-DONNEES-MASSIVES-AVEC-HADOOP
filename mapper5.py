#!/usr/bin/env python3
import sys

# Lire l'entrée ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Séparer les colonnes en utilisant plusieurs espaces comme séparateur
    columns = line.split()

    # Vérifier que la ligne contient au moins 6 colonnes
    if len(columns) < 6:
        continue  

    try:
        # Extraire l'heure (2ᵉ colonne) et le montant de la vente (5ᵉ colonne)
        hour = columns[1].split(":")[0]  # Extraire uniquement l'heure (HH:mm)
        amount = float(columns[4])

        # Émettre la paire clé-valeur (heure, montant)
        print(f"{hour}\t{amount}")
    except ValueError:
        continue  # Ignorer les lignes mal formatées
