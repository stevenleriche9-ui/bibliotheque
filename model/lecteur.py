from dataclasses import dataclass
from datetime import date
from typing import ClassVar

TARIFS = {
    "Élève": 1000,
    "Étudiant": 2000,
    "Salarié": 3000,
    "Commerçant / Autre": 5000,
}

SUR_PLACE = "lecture sur place"
EMPRUNT = "emprunt"


@dataclass
class Lecteur:
    nom: str
    prenom: str
    contact: str
    motif: str
    profession: str
    numero: int = 0
    carte_fidelite: str = ""
    abonnement: int = 0
    date_inscription: str = ""

    compteur: ClassVar[int] = 0

    def __post_init__(self):
        if self.numero == 0:
            Lecteur.compteur += 1
            self.numero = Lecteur.compteur
        else:  
            Lecteur.compteur = max(Lecteur.compteur, self.numero)

        if not self.date_inscription:
            self.date_inscription = date.today().isoformat()

        if self.motif == EMPRUNT and not self.carte_fidelite:
            self.activer_emprunt()

    def activer_emprunt(self):
        self.motif = EMPRUNT
        self.carte_fidelite = f"FID-{self.numero:04d}"
        self.abonnement = TARIFS[self.profession]
