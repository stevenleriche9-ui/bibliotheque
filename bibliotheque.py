import sys

from controler import bibliotheque_controler as ctrl
from view import vue


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ctrl.charger()
    while True:
        choix = vue.menu_principal()

        if choix == "1":
            infos = vue.saisir_lecteur()
            lecteur = ctrl.inscrire_lecteur(*infos)
            vue.afficher_inscription(lecteur)

        elif choix == "2":
            numero, ouvrage, categorie = vue.saisir_emprunt()
            resultat = ctrl.enregistrer_emprunt(numero, ouvrage, categorie)
            if resultat is None:
                print("Lecteur introuvable.")
            else:
                vue.afficher_emprunt(*resultat)

        elif choix == "3":
            numero = vue.lire_entier("Numéro du lecteur : ")
            ouvrage = vue.lire_texte("TITRE DE L'OUVRAGE : ")
            if ctrl.rendre_ouvrage(numero, ouvrage):
                print("✔ Ouvrage rendu.")
            else:
                print("Aucun emprunt correspondant.")

        elif choix == "4":
            vue.afficher_lecteurs(ctrl.lecteurs)

        elif choix == "5":
            vue.afficher_emprunts(ctrl.emprunts_en_cours(), ctrl.trouver_lecteur)

        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
