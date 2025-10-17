# Audit RGPD d'une IA de prédiction du prix des maisons 🏠<!-- <a href="../../"><img align="right" src="https://upload.wikimedia.org/wikipedia/commons/5/5d/JetBrains_PyCharm_Product_Logo.svg" alt="PyCharm" height="64px"></a> -->

<div align="center">

![Python](https://img.shields.io/badge/python-3.13-blue?style=flat&logo=python&logoColor=ffd43b) 
![Streamlit](https://img.shields.io/badge/Streamlit-Data_App-FF4B4B?style=flat&logo=streamlit&logoColor=white) 
![NumPy](https://img.shields.io/badge/NumPy-1.25-blue?style=flat&logo=NumPy&logoColor=white) 
![Joblib](https://img.shields.io/badge/Joblib-Model_Loading-0078D4?style=flat) 
<!-- ![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)  -->

</div><hr>

## **Le projet**
Cette application web interactive, développée avec **Streamlit**, permet d’estimer le prix médian d’une maison en Californie à partir de ses caractéristiques géographiques et démographiques.  
Le modèle de prédiction est un modèle de forêt aléatoire (`RandomForestRegressor`) pré-entraîné et sauvegardé, chargé via **joblib**.
---
## Fonctionnalités principales
* Interface utilisateur intuitive avec des champs de saisie numériques et sliders pour les caractéristiques suivantes :
  * Longitude et latitude  
  * Âge médian des maisons  
  * Nombre moyen de pièces et chambres  
  * Population locale et nombre de ménages  
  * Revenu médian du quartier  
  * Proximité de l'océan (catégorielle)  
* Prédiction instantanée via un bouton dédié, affichage clair et stylisé du prix médian estimé.
* Protection de la vie privée : aucune donnée personnelle n’est collectée ou stockée.
## Structure du projet
```txt
├── rfr_model.pkl # Modèle pré-entraîné (Random Forest)
├── app.py # Script principal Streamlit (cette application)
├── README.md # Documentation
└── requirements.txt # Dépendances nécessaires
```
## Lancer l'application
```bash
streamlit run main.py
```
Le navigateur ouvrira l’interface.  
Vous pourrez ajuster les paramètres et obtenir la prédiction du prix.
## **Le modèle**
Le modèle de forêt aléatoire a été entraîné sur le jeu de données California Housing, [dont le notebook est disponible ici](https://github.com/MiKL5/machineLearning/blob/master/projects/house).
## **Avertissements**
* Ce modèle est un prototype pédagogique et ne garantit pas une précision parfaite en conditions réelles.
* Les données saisies ne sont pas stockées, respectant ainsi la confidentialité de l'utilisateur.
___
## Auteurs
Quentin HECQUET  
Mickael GAILLARD