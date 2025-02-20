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
        # Extraire la méthode de paiement (6ᵉ colonne) et le montant (5ᵉ colonne)
        payment_method = columns[5]
        amount = float(columns[4])

        # Émettre la paire clé-valeur (méthode de paiement, montant) séparée par une tabulation
        print(f"{payment_method}\t{amount}")
    except ValueError:
        continue  # Ignorer les lignes où le montant n'est pas un nombre valide
