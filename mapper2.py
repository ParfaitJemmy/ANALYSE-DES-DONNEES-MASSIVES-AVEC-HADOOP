#!/usr/bin/env python3
import sys

# Lecture de l'entrée ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()
    
    # Séparer les colonnes en utilisant plusieurs espaces comme séparateur
    columns = line.split()

    # Vérifier que la ligne contient au moins 6 colonnes (pour éviter les erreurs d'index)
    if len(columns) < 6:
        continue  # Ignorer les lignes mal formatées

    try:
        # Extraire la ville (3ᵉ colonne) et le montant (5ᵉ colonne)
        product = columns[3]
        amount = float(columns[4])

        # Émettre la paire clé-valeur (ville, montant) séparée par une tabulation
        print(f"{product}\t{amount}")
    except ValueError:
        continue  # Ignorer les lignes où le montant n'est pas un nombre valide
