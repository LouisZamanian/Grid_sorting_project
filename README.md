# Grid Sorting Project

## Description
Ce projet, réalisé dans le cadre du programme [ENSAE 1A 2023-2024], explore des algorithmes et approches pour résoudre un puzzle de tri sur une grille (**swap puzzle**). Le projet est basé sur une implémentation modulaire en Python et couvre des aspects allant de la modélisation du problème aux solutions optimisées.

---

## Fonctionnalités techniques
- **Génération de grilles** :
  - Création de grilles aléatoires de taille \( n \times n \) avec des valeurs initiales.
  - Visualisation des états initiaux de la grille.
  
- **Algorithmes de résolution** :
  - Implémentation de différents algorithmes (DFS, BFS, A*, heuristiques spécifiques).
  - Comparaison de la performance des solutions sur plusieurs configurations.
  
- **Graphes et structures de données** :
  - Utilisation de graphes pour modéliser les mouvements possibles sur la grille.
  - Parcours des graphes pour identifier la solution optimale.


---

## Structure du projet
Voici la structure principale des fichiers et dossiers :

```
Grid_sorting_project/
├── input/               # Données d'entrée (fichiers, configurations)
├── swap_puzzle/         # Modules Python pour la résolution
│   ├── creation_jeu.py  # Génération des grilles de jeu
│   ├── graph.py         # Gestion des graphes
│   ├── grid.py          # Modélisation des grilles et des déplacements
│   ├── solver.py        # Algorithmes de résolution
│   ├── main.py          # Point d'entrée principal
├── Notebooks/           # Notebooks Jupyter pour les analyses
├── tests/               # Scripts de tests unitaires
├── README.md            # Documentation du projet
└── requirements.txt     # Liste des dépendances Python
```

---


## Algorithmes implémentés
### 1. Recherche en profondeur (DFS)
- Utilisé pour explorer exhaustivement tous les chemins possibles.
- Limité par le risque de cycles infinis.

### 2. Recherche en largeur (BFS)
- Permet de trouver le chemin le plus court dans le graphe de la grille.
- Exige plus de mémoire que DFS.

### 3. A* avec heuristique
- Combine le coût du chemin parcouru et une estimation du coût restant.
- Heuristique utilisée : distance de Manhattan.

---

## Auteurs
- **Louis Zamanian** : Développeur principal
