#!/usr/bin/env python3
import sys

# Initialisation des variables pour la méthode de paiement courante et le total des ventes
current_payment_method = None
current_total = 0.0

# Lecture ligne par ligne des données triées (déjà agrégées par méthode de paiement)
for line in sys.stdin:
    # Supprimer les espaces en début et fin de ligne
    line = line.strip()

    # Séparer les données par la tabulation
    payment_method, amount = line.split("\t")

    try:
        # Convertir le montant en float
        amount = float(amount)
    except ValueError:
        continue  # Ignorer les lignes mal formatées

    # Si on est sur la même méthode de paiement, on cumule les montants
    if current_payment_method == payment_method:
        current_total += amount
    else:
        # Si la méthode change, afficher le total pour la méthode précédente
        if current_payment_method:
            print(f"{current_payment_method}\t{current_total}")
        current_payment_method = payment_method
        current_total = amount

# Affichage final pour la dernière méthode de paiement
if current_payment_method == payment_method:
    print(f"{current_payment_method}\t{current_total}")
