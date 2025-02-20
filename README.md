##                        Analyse de données massives avec Hadoop

## Description du projet

Cette présentation explore le fonctionnement de Hadoop et la mise en œuvre d’une analyse de données
massives à l’aide de MapReduce.

## Objectif du projet

- Comprendre l’architecture Hadoop et son rôle dans les environnements distribués.
- Apprendre à utiliser MapReduce pour traiter de grandes quantités de données.

## Contenu du document

- Introduction à Hadoop (dans le fichier powerpoint)
- Architecture et composants (HDFS, YARN, MapReduce) (dans le fichier powerpoint également)
- Les étapes pour mettre en œuvre une analyse de données massives avec Hadoop
- Cas d'utilisation et démonstration pratique (*le cas d'utilisation sera fait dans un document 
pdf avec des captures pour illustrer, étant donnée que nous utilions le terminal de la machine 
pour exécuter nos commandes et interagir avec hadoop*)

---

## 1. Les étapes pour mettre en œuvre une analyse de données massives avec Hadoop


*** Première étape: Installation des ressources nécessaires***

### 1.1 Installation de Hadoop sur la machine locale

Avant d'installer Hadoop, il est essentiel de s'assurer que les éléments suivants sont installés et
 configurés sur la machine :

#### 1.1.1 Prérequis

- **Java JDK (version 8 ou supérieure)** :
  Hadoop est développé en Java, ce qui rend ce langage indispensable pour son fonctionnement. Les API 
  de Hadoop, y compris celles de HDFS (Hadoop Distributed File System) et de MapReduce, sont écrites en Java.
  Cela permet à Hadoop de tirer parti des fonctionnalités du langage pour gérer des tâches complexes de manière distribuée.

  *Pour vérifier si Java est installé, exécutez la commande suivante dans un terminal :*

  ```sh
  java -version
  ```
  
  Si Java est installé, on doit voir cela :
  ```sh
  java version "1.8.0_441"
  Java(TM) SE Runtime Environment (build 1.8.0_441-b07)
  Java HotSpot(TM) 64-Bit Server VM (build 25.441-b07, mixed mode)
  ```

  Si Java n'est pas installé, téléchargez-le depuis le site officiel d'Oracle : 
  [Oracle Java Download](https://www.oracle.com/java/technologies/javase-downloads.html)

#### 1.1.2 Installation de Hadoop

- **Téléchargement de Hadoop** :

  Téléchargez la dernière version stable de Hadoop depuis le site officiel : Apache Hadoop Releases.

  Par exemple, pour Hadoop 3.3.4, utilisez la commande suivante :
  ```sh
  wget https://downloads.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
  ```
- **Extraction de l'archive téléchargée** :
  ```sh
  tar -xzvf hadoop-3.3.4.tar.gz
  ```
- **Déplacement du dossier Hadoop** :
  ```sh
  sudo mv hadoop-3.3.4 /usr/local/hadoop
  ```
- **Configuration des variables d'environnement** :
  ```sh
  nano ~/.bashrc
  ```
  Ajoutez les lignes suivantes à la fin du fichier :
  ```sh
  export HADOOP_HOME=/usr/local/hadoop
  export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  # Remplacez par le chemin de votre JDK
  export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
  ```

### 1.2 Installation de Docker

#### 1.2.1 Pourquoi utiliser Docker ?

Docker permet d'éviter les problèmes de compatibilité et de configuration en encapsulant Hadoop et
ses dépendances dans un environnement conteneurisé. Cela facilite l'installation et le déploiement
 en environnement local, tout en garantissant la reproductibilité des tests et analyses.

#### 1.2.2 Installation de Docker

1. **Mettre à jour le système**
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```
2. **Installer les dépendances requises**
   ```sh
   sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
   ```
3. **Ajouter la clé GPG de Docker**
   ```sh
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```
4. **Ajouter le dépôt officiel de Docker**
   ```sh
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg]
   https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
5. **Installer Docker**
   ```sh
   sudo apt update
   sudo apt install docker-ce docker-ce-cli containerd.io -y
   ```
6. **Vérifier l'installation**
   ```sh
   docker --version
   ```
   Vous devriez voir une sortie similaire à :
   ```sh
   Docker version 24.0.2, build 1234567
   ```

   *Déconnectez-vous et reconnectez-vous pour que les modifications prennent effet.*

#### 1.2.3 Exécution de Hadoop dans un conteneur Docker

Avec Docker installé, il est possible de lancer un cluster Hadoop en conteneurs sans avoir à configurer 
manuellement chaque composant. Une solution courante est d'utiliser des images Docker préconfigurées pour Hadoop.

1. **Télécharger une image Hadoop**
Pour notre cas, nous avons utilisé l'image suivante
   ```sh
   docker pull liliasfaxi/hadoop-cluster:latest
   ```
2. **Lancer un conteneur Hadoop**
   ```sh
   docker run -it --rm sequenceiq/hadoop-docker /etc/bootstrap.sh -bash
   ```

Cette approche permet une gestion plus simple des dépendances et une isolation des environnements, évitant ainsi
 les conflits liés aux versions des bibliothèques système.

---

Après ces étapes d'installation, et apres que tout fonctionne, la premiere étape pour faire une analyse des données sur
hadoop est réalisée.


*** Deuxième étape: Faire l'analyse avec hadoop***

Cette étape sera faite dans le document pdf ou nous allons faire de l'analyse des données avec hadoop.


*** Lien vers les ressources utilisées:***

 * https://www.youtube.com/watch?v=knAS0w-jiUk&pp=ygUYY29tbWVudCBpbnN0YWxsw6kgaGFkb29w
 * https://insatunisia.github.io/TP-BigData/tp1.pdf
 * https://chatgpt.com/

