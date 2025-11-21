# 🎮 Tic Tac Toe

Un jeu de morpion moderne avec interface graphique développé en Python avec Tkinter.

## 📋 Fonctionnalités

- **Mode 2 Joueurs** : Jouez contre un ami sur le même ordinateur
- **Mode Contre IA** : Affrontez une intelligence artificielle avec stratégie avancée
- **Interface moderne** : Design coloré avec thème
- **Navigation intuitive** : Menu principal et retour facile entre les parties

## 🚀 Installation et Lancement

### Prérequis
- Python 3.x
- Tkinter (inclus par défaut avec Python)

### Lancer le jeu
```bash
python tic_tac_toe.py
```

## 🎯 Comment jouer

1. Lancez le jeu et choisissez votre mode :
   - **2 Joueurs** : X et O jouent à tour de rôle
   - **Contre IA** : Vous êtes X, l'IA est O

2. Cliquez sur une case vide pour placer votre symbole

3. Le premier à aligner 3 symboles (horizontal, vertical ou diagonal) gagne !

## 🏗️ Architecture du Code

### Structure Principale

Le code est organisé en deux composants principaux :

#### 1. Classe `TicTacToe`
Gère l'interface graphique et la logique du jeu.

**Attributs clés :**
- `board` : Liste de 9 éléments représentant l'état du plateau
- `current_player` : Joueur actuel ('X' ou 'O')
- `game_mode` : Mode de jeu ('pvp' ou 'pvia')
- `wins` : Liste des 8 combinaisons gagnantes possibles

**Méthodes principales :**
- `create_menu()` : Affiche le menu principal avec les options de jeu
- `create_board()` : Génère la grille de jeu 3×3 avec les boutons
- `move(pos)` : Gère un coup de joueur à la position donnée
- `ia_move()` : Déclenche le coup de l'IA après un délai de 50ms
- `check_win(p)` : Vérifie si le joueur p a gagné
- `end(msg)` : Affiche le message de fin et retourne au menu

#### 2. Fonction `ia(b, s)`
Implémente la stratégie de l'intelligence artificielle.

**Paramètres :**
- `b` : État actuel du plateau (liste de 9 éléments)
- `s` : Symbole de l'IA ('O')

**Retour :**
- Position (0-8) où l'IA doit jouer
- `False` si aucun coup n'est possible

## 🧠 Stratégie de l'IA

L'IA suit une hiérarchie de priorités pour choisir son coup :

### 1. Gagner immédiatement
Si l'IA peut compléter une ligne de 3, elle joue ce coup gagnant.

```python
# Exemple : O O _ → L'IA joue en position 2
```

### 2. Bloquer l'adversaire
Si le joueur peut gagner au prochain coup, l'IA bloque.

```python
# Exemple : X X _ → L'IA joue en position 2 pour bloquer
```

### 3. Prendre le centre
Si disponible, le centre (position 4) offre le plus d'opportunités.

### 4. Prendre un coin
Les coins (0, 2, 6, 8) sont les positions stratégiques suivantes.

### 5. Prendre une case restante
En dernier recours, l'IA prend n'importe quelle case libre.



### Dimensions
- Fenêtre : 500×600 pixels (non redimensionnable)
- Boutons de jeu : 5 caractères de large × 2 de haut
- Police : Arial, tailles variées selon le contexte

## 💡 Détails Techniques Intéressants

### Utilisation de `is` vs `==`
Dans la fonction `ia_move()`, on utilise `if m is not False` plutôt que `if m != False`. Ceci est important car en Python, `0 == False` est `True`, donc l'opérateur `is` qui vérifie l'identité (et non l'égalité) est nécessaire pour distinguer la position 0 de la valeur `False`.

### Délai de l'IA
L'IA joue après un délai de 50ms (`self.root.after(50, self.ia_move)`) pour rendre le jeu plus naturel et éviter que le coup de l'IA apparaisse instantanément.

## 📝 Structure des Données

### Représentation du plateau
```python
# Indices des positions :
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

board = ['', '', '', '', '', '', '', '', '']  # Plateau vide
```

### Combinaisons gagnantes
```python
wins = [
    [0,1,2],  # Ligne 1
    [3,4,5],  # Ligne 2
    [6,7,8],  # Ligne 3
    [0,3,6],  # Colonne 1
    [1,4,7],  # Colonne 2
    [2,5,8],  # Colonne 3
    [0,4,8],  # Diagonale \
    [2,4,6]   # Diagonale /
]
```

## 🔧 Technologies Utilisées

- **Python 3.x** : Langage de programmation
- **Tkinter** : Bibliothèque GUI native de Python
- **Messagebox** : Pour les notifications de fin de partie

## 📈 Améliorations Possibles

- Ajouter des niveaux de difficulté (facile, moyen, difficile)
- Implémenter l'algorithme Minimax pour une IA imbattable
- Ajouter un système de score persistant
- Permettre de choisir qui commence (X ou O)
- Ajouter des effets sonores
- Créer un mode en ligne multijoueur
- Sauvegarder l'historique des parties

## 📄 Licence

Ce projet est libre d'utilisation pour un usage personnel et éducatif.

## 👤 Auteur
gabin salucci
