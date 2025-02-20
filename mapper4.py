#!/usr/bin/env python3
import sys

# Lire l'entrée ligne par ligne
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Séparer les colonnes en utilisant plusieurs espaces comme séparateur
    columns = line.split()

    # Vérifier que la ligne contient au moins 6 colonnes (éviter les erreurs d'index)
    if len(columns) < 6:
        continue  

    try:
        # Extraire le montant de la vente (5ᵉ colonne)
        amount = float(columns[4])

        # Émettre une clé constante "total" avec la valeur du montant et un compteur 1
        print(f"total\t{amount}\t1")
    except ValueError:
        continue  # Ignorer les lignes mal formatées
