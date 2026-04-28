
Projet fait par LOTUE THRECIA JOHANNA KAMGA au matricule 24G2297



# Quizz App - Recensement des étudiants 

Application Flask permettant de collecter les informations des étudiants souhaitant obtenir une chambre universitaire.

##  Fonctionnalités
- Formulaire étudiant (nom, âge, filière, niveau)
- Base de données SQLite
- Statistiques (âge moyen, filières)
- Graphiques (camembert)
- Interface admin

##  Technologies
- Python (Flask)
- SQLite
- HTML / CSS
- Chart.js

##  Lancer le projet en local

```bash
pip install -r requirements.txt
python app.py

##Deploiement
projet deploye avec render

# 🏠 Fonctionnement de l’application

Cette application est une plateforme de recensement des étudiants souhaitant obtenir une chambre universitaire.

---

## 🧭 1. Page formulaire

L’utilisateur accède à un formulaire dans lequel il renseigne :

- Nom
- Âge (entre 18 et 26 ans)
- Email
- Filière (liste déroulante)
- Niveau d’études (liste déroulante)

Une fois les informations remplies, l’utilisateur soumet le formulaire.

---

## 💾 2. Enregistrement des données

Lors de la soumission :

- Les données sont enregistrées dans une base de données SQLite
- Chaque utilisateur est ajouté comme une nouvelle entrée

---

## 📊 3. Page résultats utilisateur

Après soumission, l’utilisateur est redirigé vers une page de résultats qui affiche :

- Les informations qu’il vient d’entrer
- Des statistiques globales du système

---

## 📈 4. Statistiques globales

L’application calcule et affiche :

- L’âge moyen des étudiants inscrits
- Le nombre d’étudiants par filière

Ces données permettent d’avoir une vue d’ensemble des profils des étudiants.

---

## 📊 5. Visualisation graphique

Les statistiques sont représentées sous forme de graphiques :

- Camembert (répartition des filières)
- Graphiques dynamiques générés avec Chart.js

---

## 🔐 6. Interface admin

Une interface administrateur permet de :

- Consulter tous les étudiants enregistrés
- Voir les données sous forme de tableau
- Accéder aux informations globales de la base


## 🎯 Objectif du projet

Permettre une collecte simple et structurée des données des étudiants afin d’analyser leur profil et faciliter la gestion des demandes de logement universitaire.
