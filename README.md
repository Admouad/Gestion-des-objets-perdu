#AIT SAID MOUAD 5IIRG2


# Gestion Informatisée des Objets Perdus (Module Odoo 17)

![Odoo](https://img.shields.io/badge/Framework-Odoo%2017-875A7B.svg)
![Python](https://img.shields.io/badge/Language-Python%203-3776AB.svg)
![Docker](https://img.shields.io/badge/Deployment-Docker-2496ED.svg)

## 📝 Description du Projet
Le projet **"tp_objets_perdus"** est un module métier sur mesure conçu pour l'ERP **Odoo 17**. Il répond à une problématique logistique concrète : la gestion désorganisée des objets égarés au sein d'une structure à fort trafic (universités, gares, centres commerciaux). 

L'objectif est de remplacer les registres papier par une application web robuste capable de centraliser chaque étape du cycle de vie d'un objet trouvé, depuis son enregistrement jusqu'à sa restitution finale.

---

## 🚀 Fonctionnalités Clés
* **Enregistrement exhaustif :** Saisie rapide des caractéristiques de l'objet (type, marque, couleur, lieu de découverte).
* **Gestion visuelle :** Intégration de photographies pour chaque objet enregistré.
* **Workflow dynamique :** Suivi en temps réel des états (Disponible, Réclamé, Restitué).
* **Recherche avancée :** Vues Liste et Kanban avec filtres multicritères.
* **Architecture MVC :** Séparation stricte entre les modèles Python et les vues XML.

---

## 🛠️ Architecture Technique
L'application repose sur une pile technologique moderne garantissant performance et scalabilité :



* **Backend :** Python (Framework Odoo)
* **Frontend :** XML / Odoo Web Framework
* **Base de données :** PostgreSQL
* **Infrastructure :** Conteneurisation avec Docker et Docker-Compose.

---

## 📂 Structure du Module
```text
tp_objets_perdus/
├── models/             # Logique métier (objets_perdus.py)
├── views/              # Interfaces utilisateurs (XML)
├── security/           # Droits d'accès et groupes (CSV)
├── static/             # Images et icônes
├── __init__.py
└── __manifest__.py     # Métadonnées du module
