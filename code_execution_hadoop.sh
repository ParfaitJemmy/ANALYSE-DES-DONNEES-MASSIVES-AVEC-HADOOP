# Convertit les fichiers au format Unix
dos2unix /home/mapper1.py
dos2unix /home/reducer1.py
dos2unix /home/mapper2.py
dos2unix /home/reducer2.py
dos2unix /home/mapper3.py
dos2unix /home/reducer3.py
dos2unix /home/mapper4.py
dos2unix /home/reducer4.py
dos2unix /home/mapper5.py
dos2unix /home/reducer5.py

# Autorisation d'exécution des scripts Python pour Hadoop
chmod +x /home/mapper1.py
chmod +x /home/reducer1.py
chmod +x /home/mapper2.py
chmod +x /home/reducer2.py
chmod +x /home/mapper3.py
chmod +x /home/reducer3.py
chmod +x /home/mapper4.py
chmod +x /home/reducer4.py
chmod +x /home/mapper5.py
chmod +x /home/reducer5.py

# Affichage des premières lignes du fichier purchases.txt
echo "Aperçu des premières lignes du fichier purchases.txt:"
head -n 10 /root/purchases.txt

echo "Lecture complète du fichier purchases.txt:"
cat /root/purchases.txt

# Exécution locale des scripts pour vérifier les résultats
echo "Ventes totales par ville :"
cat /root/purchases.txt | /home/mapper1.py | sort | /home/reducer1.py

# Lancement du job MapReduce pour les ventes totales par ville
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input input/purchases.txt \
    -output /output/ventes_villes \
    -mapper "python3 /home/mapper1.py" \
    -reducer "python3 /home/reducer1.py" \
    -file /home/mapper1.py \
    -file /home/reducer1.py

# Exécution locale des scripts pour vérifier les résultats des ventes par catégorie
echo "Ventes totales par catégorie :"
cat /root/purchases.txt | /home/mapper2.py | sort | /home/reducer2.py

# Lancement du job MapReduce pour les ventes totales par catégorie
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input input/purchases.txt \
    -output /output/ventes_categories \
    -mapper "python3 /home/mapper2.py" \
    -reducer "python3 /home/reducer2.py" \
    -file /home/mapper2.py \
    -file /home/reducer2.py

# Exécution locale des scripts pour les ventes par types de paiement
echo "total des ventes par type de paiement :"
cat /root/purchases.txt | /home/mapper3.py | sort | /home/reducer3.py

# Lancement du job MapReduce pour la troisième question
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input input/purchases.txt \
    -output /output/ventes_paiement \
    -mapper "python3 /home/mapper3.py" \
    -reducer "python3 /home/reducer3.py" \
    -file /home/mapper3.py \
    -file /home/reducer3.py

# Exécution locale des scripts pour la vente moyenne
echo "Résultats de la vente moyenne :"
cat /root/purchases.txt | /home/mapper4.py | sort | /home/reducer4.py

# Lancement du job MapReduce pour la quatrième question
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input input/purchases.txt \
    -output /output/ventes_moyennes \
    -mapper "python3 /home/mapper4.py" \
    -reducer "python3 /home/reducer4.py" \
    -file /home/mapper4.py \
    -file /home/reducer4.py

# Exécution locale des scripts pour analyse de la répartition temporelle ( somme des ventes par heures)
echo "Résultats de la série temporelle :"
cat /root/purchases.txt | /home/mapper5.py | sort | /home/reducer5.py

# Lancement du job MapReduce pour la cinquième question
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input input/purchases.txt \
    -output /output/ventes_temporelle \
    -mapper "python3 /home/mapper5.py" \
    -reducer "python3 /home/reducer5.py" \
    -file /home/mapper5.py \
    -file /home/reducer5.py
