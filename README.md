# 🧩 Gale - Shapley  


![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/statut-en%20développement-yellow.svg)

## 📘 Présentation

**GaleImple** est un projet en **Python** qui propose une version **structurée, modulaire et extensible** de l’**algorithme de mariage stable** de **Gale–Shapley**.
 
Le but est d’explorer et de simuler différents **scénarios d’appariement** entre deux ensembles (ex. : élèves–établissements, candidats–entreprises)

## Architecture du projet

```text
GaleImple/
project/
│
├── __init__.py         
├── main.py             
├── rapport_final.pdf   
│
└── src/    
    ├── core.py         
    ├── analysis.py     
    ├── experiments.py  
    ├── visuals.py      
└── rapport/
    ├── main.tex       
    ├── images.png     
```

## 🎯 Objectifs du projet


1. **Implanter un programme** pour générer des préférences aléatoires  
   pour les étudiants et les établissements.
2. **Implanter l’algorithme du mariage stable** (Gale–Shapley).
3. **Proposer une méthode de mesure de satisfaction**,  
   pour les étudiants et pour les établissements,  
   et **l’intégrer dans l’implantation**.
4. **Tester le programme** sur plusieurs jeux de données.
5. **Proposer une extension théorique** permettant l’intégration  
   des **représentations compactes des préférences** vues en cours  
   (sans implantation pratique); application des algorithmes deja vue en cours sur notre propre cas d'usage.
 



## 🚀 Installation et exécution
1️⃣ Cloner le dépôt

```bash
# cloner le dépôt
git clone https://github.com/ibrayoubi10/GaleImple.git

# accéder au dossier
cd GaleImple
```
2️⃣ Exécuter la version modulaire
```bash
python3 main.py
```
Cela lance plusieurs scénarios, affiche un rapport détaillé,
puis génère des visualisations (distribution des rangs, satisfaction globale…).

## Auteurs
- Al Ayoubi Ibrahim
- Beguith Rami 
- Kammoun Habib 
- Toukebri Dhia

## 🏫 UFR Sciences de Montpellier
Ce projet est réalisé dans le cadre du module **Aide à la décision – M2 Informatique (IASD)**.
