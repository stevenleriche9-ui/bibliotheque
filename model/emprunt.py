from dataclasses import dataclass
from datetime import date, timedelta

DUREE_JOURS = 14  


@dataclass
class Emprunt:
    numero_lecteur: int
    ouvrage: str
    categorie: str
    date_emprunt: str = ""
    date_retour_prevue: str = ""
    rendu: bool = False

    def __post_init__(self):
        if not self.date_emprunt:
            debut = date.today()
            self.date_emprunt = debut.isoformat()
            self.date_retour_prevue = (debut + timedelta(days=DUREE_JOURS)).isoformat()

    @property
    def en_retard(self) -> bool:
        return not self.rendu and date.today() > date.fromisoformat(self.date_retour_prevue)
