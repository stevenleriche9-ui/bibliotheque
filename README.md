# 📚 Gestion de bibliothèque

Application en ligne de commande (Python) pour gérer une petite bibliothèque : inscription des lecteurs, emprunts, retours et suivi des retards. Les données sont enregistrées dans un fichier JSON.

## Fonctionnalités

- **Inscrire un lecteur** : nom, prénom, contact, motif de la visite (lecture sur place ou emprunt) et profession.
- **Enregistrer un emprunt** : titre et catégorie de l'ouvrage, date de retour calculée automatiquement (14 jours).
- **Enregistrer un retour** d'ouvrage.
- **Lister les lecteurs** inscrits.
- **Lister les emprunts en cours**, avec signalement des retards ⚠.
- **Carte de fidélité** (`FID-0001`, …) créée automatiquement dès qu'un lecteur emprunte, avec abonnement annuel selon la profession.

### Tarifs d'abonnement annuel

| Profession          | Abonnement   |
|---------------------|--------------|
| Élève               | 1 000 FCFA   |
| Étudiant            | 2 000 FCFA   |
| Salarié             | 3 000 FCFA   |
| Commerçant / Autre  | 5 000 FCFA   |

La lecture sur place ne nécessite aucun abonnement.

## Prérequis

- Python **3.10 ou supérieur**
- Aucune dépendance externe (bibliothèque standard uniquement)

## Lancement

```bash
cd bibliotheque
python bibliotheque.py
```

Menu principal :

```
===== GESTION DE BIBLIOTHÈQUE =====
1. Inscrire un lecteur
2. Enregistrer un emprunt
3. Enregistrer un retour
4. Liste des lecteurs
5. Emprunts en cours
0. Quitter
```

## Structure du projet

Le projet suit l'architecture **MVC** :

```
bibliotheque/
├── bibliotheque.py                 # Point d'entrée : boucle du menu
├── donnees.json                    # Données persistantes (créé automatiquement)
├── model/
│   ├── lecteur.py                  # Classe Lecteur, tarifs, carte de fidélité
│   └── emprunt.py                  # Classe Emprunt, dates et retards
├── view/
│   └── vue.py                      # Saisies et affichages (console)
└── controler/
    └── bibliotheque_controler.py   # Logique métier et sauvegarde JSON
```

## Données

Les lecteurs et les emprunts sont sauvegardés dans `donnees.json` après chaque modification, et rechargés au démarrage. Si le fichier n'existe pas, il est créé automatiquement à la première inscription.

> ⚠️ `donnees.json` contient des informations personnelles (noms, numéros de téléphone) : il est exclu du dépôt Git via le `.gitignore`.

## Idées d'amélioration

- Catalogue d'ouvrages avec gestion du stock
- Recherche d'un lecteur par nom
- Gestion du paiement et du renouvellement des abonnements
- Tests unitaires
