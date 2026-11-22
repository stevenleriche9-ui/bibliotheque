import json
import os
from dataclasses import asdict

from model.lecteur import Lecteur
from model.emprunt import Emprunt

FICHIER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "donnees.json")

lecteurs: list[Lecteur] = []
emprunts: list[Emprunt] = []


def charger():
    if not os.path.exists(FICHIER):
        return
    with open(FICHIER, encoding="utf-8") as f:
        data = json.load(f)
    lecteurs.extend(Lecteur(**d) for d in data.get("lecteurs", []))
    emprunts.extend(Emprunt(**d) for d in data.get("emprunts", []))


def sauvegarder():
    data = {
        "lecteurs": [asdict(l) for l in lecteurs],
        "emprunts": [asdict(e) for e in emprunts],
    }
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def inscrire_lecteur(nom, prenom, contact, motif, profession) -> Lecteur:
    lecteur = Lecteur(nom, prenom, contact, motif, profession)
    lecteurs.append(lecteur)
    sauvegarder()
    return lecteur


def trouver_lecteur(numero: int) -> Lecteur | None:
    for lecteur in lecteurs:
        if lecteur.numero == numero:
            return lecteur
    return None


def enregistrer_emprunt(numero_lecteur, ouvrage, categorie):
    """Retourne (emprunt, lecteur, carte_creee) ou None si lecteur inconnu."""
    lecteur = trouver_lecteur(numero_lecteur)
    if lecteur is None:
        return None

    carte_creee = False
    if not lecteur.carte_fidelite:  
        lecteur.activer_emprunt()
        carte_creee = True

    emprunt = Emprunt(numero_lecteur, ouvrage, categorie)
    emprunts.append(emprunt)
    sauvegarder()
    return emprunt, lecteur, carte_creee


def rendre_ouvrage(numero_lecteur, ouvrage) -> bool:
    for e in emprunts:
        if (e.numero_lecteur == numero_lecteur
                and e.ouvrage.lower() == ouvrage.lower()
                and not e.rendu):
            e.rendu = True
            sauvegarder()
            return True
    return False


def emprunts_en_cours():
    return [e for e in emprunts if not e.rendu]
