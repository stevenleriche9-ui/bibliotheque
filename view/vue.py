from model.lecteur import TARIFS, SUR_PLACE, EMPRUNT


def lire_texte(message: str) -> str:
    while True:
        valeur = input(message).strip()
        if valeur:
            return valeur
        print("Ce champ ne peut pas être vide.")


def lire_entier(message: str) -> int:
    while True:
        valeur = input(message).strip()
        if valeur.isdigit():
            return int(valeur)
        print("Veuillez entrer un nombre.")


def lire_choix(message: str, options: list[str]) -> str:
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        choix = input(message).strip()
        if choix.isdigit() and 1 <= int(choix) <= len(options):
            return options[int(choix) - 1]
        print("Choix invalide.")


def menu_principal() -> str:
    print("\n===== GESTION DE BIBLIOTHÈQUE =====")
    print("1. Inscrire un lecteur")
    print("2. Enregistrer un emprunt")
    print("3. Enregistrer un retour")
    print("4. Liste des lecteurs")
    print("5. Emprunts en cours")
    print("0. Quitter")
    return input("Votre choix : ").strip()


def saisir_lecteur():
    print("\n--- Inscription d'un lecteur ---")
    nom = lire_texte("NOM : ").upper()
    prenom = lire_texte("PRENOM : ").capitalize()
    while True:
        contact = input("CONTACT (numéro de tel) : ").strip().replace(" ", "")
        if contact.isdigit() and len(contact) >= 8:
            break
        print("Numéro invalide (chiffres uniquement, 8 minimum).")
    print("MOTIF DE LA VISITE :")
    motif = lire_choix("Votre choix : ", [SUR_PLACE, EMPRUNT])
    print("PROFESSION :")
    profession = lire_choix("Votre choix : ", list(TARIFS))
    return nom, prenom, contact, motif, profession


def afficher_inscription(lecteur):
    print("\n✔ Lecteur inscrit avec succès")
    print(f"  Numéro de lecteur : {lecteur.numero}")
    print(f"  Nom               : {lecteur.nom} {lecteur.prenom}")
    print(f"  Motif             : {lecteur.motif}")
    if lecteur.carte_fidelite:
        afficher_carte(lecteur)


def afficher_carte(lecteur):
    print(f"  Carte de fidélité : {lecteur.carte_fidelite}")
    print(f"  Abonnement annuel : {lecteur.abonnement} FCFA à payer")


def saisir_emprunt():
    print("\n--- Nouvel emprunt ---")
    numero = lire_entier("Numéro du lecteur : ")
    ouvrage = lire_texte("TITRE DE L'OUVRAGE : ")
    categorie = lire_texte("CATEGORIE DE L'OUVRAGE : ")
    return numero, ouvrage, categorie


def afficher_emprunt(emprunt, lecteur, carte_creee):
    if carte_creee:
        print("\nCe lecteur n'avait pas encore de carte, elle vient d'être créée :")
        afficher_carte(lecteur)
    print(f"\n✔ Ouvrage « {emprunt.ouvrage} » emprunté par {lecteur.nom} {lecteur.prenom}")
    print(f"  Date d'emprunt : {emprunt.date_emprunt}")
    print(f"  À rendre avant : {emprunt.date_retour_prevue} (2 semaines)")


def afficher_lecteurs(lecteurs):
    print("\n--- Liste des lecteurs ---")
    if not lecteurs:
        print("Aucun lecteur.")
    for l in lecteurs:
        carte = l.carte_fidelite or "-"
        print(f"N°{l.numero:<4} {l.nom} {l.prenom} | {l.contact} | {l.motif} "
              f"| {l.profession} | carte: {carte} | abonnement: {l.abonnement} FCFA")


def afficher_emprunts(emprunts, trouver_lecteur):
    print("\n--- Emprunts en cours ---")
    if not emprunts:
        print("Aucun emprunt en cours.")
    for e in emprunts:
        l = trouver_lecteur(e.numero_lecteur)
        nom = f"{l.nom} {l.prenom}" if l else "?"
        retard = "  ⚠ EN RETARD" if e.en_retard else ""
        print(f"{e.ouvrage} ({e.categorie}) | {nom} (N°{e.numero_lecteur}) "
              f"| retour avant {e.date_retour_prevue}{retard}")
