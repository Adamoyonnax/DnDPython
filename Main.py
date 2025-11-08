from Classes.Monstre import Monstre
from Classes.Joueur import Joueur
from Classes.Enum.MonstreEnum import Taille, Alignement, Type, Puissance
from Classes.Enum.JoueurEnum import Classe, Race
from Classes.Combat import Combat
from Sauvegarde.Sauvegarde import sauvegarder_joueur, charger_joueur

def initialisation_data():
    monstre1 = Monstre("Orc", Taille.M, Puissance.UD, Alignement.CM, Type.HUMANOIDE, 13, 15, [16, 12, 16, 7, 11, 10])
    monstre2 = Monstre("Gobelin", Taille.P, Puissance.UQ, Alignement.NM, Type.HUMANOIDE, 15, 7, [8, 14, 10, 10, 8, 8])
    monstres = [monstre2]
    return monstres 
    
def creation_joueur():
    # Si une sauvegarde existe, proposer de la recharger
    joueur_existant = charger_joueur()
    if joueur_existant:
        choix = input("Un joueur sauvegardé a été trouvé. Voulez-vous le charger ? (O/N) : ").lower()
        if choix == "o":
            print("\n✅ Joueur chargé avec succès :")
            return joueur_existant
        else:
            print("⚠️ Création d’un nouveau joueur. L’ancienne sauvegarde sera remplacée.\n")

    print("=== Bienvenue dans le jeu de DnD Python ===")
    print("\n=== Création d'un Joueur ===")

    # Nom du joueur
    nom = input("Entrez le nom du joueur: ")

    # Choix de la classe
    print("\nChoisissez une classe:")
    for c in Classe:
        print(f"- {c.name} ({c.value})")
    while True:
        classe_input = input("Entrez la classe choisie: ").upper()
        if classe_input in Classe.__members__:
            classe = Classe[classe_input]
            break
        else:
            print("Classe invalide, réessayez.")

    # Choix de la race
    print("\nChoisissez une race:")
    for r in Race:
        print(f"- {r.name} ({r.value})")
    while True:
        race_input = input("Entrez la race choisie: ").upper()
        if race_input in Race.__members__:
            race = Race[race_input]
            break
        else:
            print("Race invalide, réessayez.")

    # Répartition des statistiques
    print("\nRépartition des statistiques (FOR, DEX, CON, INT, SAG, CHA)")
    stats_names = ["FOR", "DEX", "CON", "INT", "SAG", "CHA"]
    stats = [0] * 6
    points_disponibles = 70

    for i, stat in enumerate(stats_names):
        while True:
            try:
                print(f"Points restants: {points_disponibles}")
                valeur = int(input(f"Combien de points pour {stat}? "))
                if 0 <= valeur <= points_disponibles:
                    stats[i] = valeur
                    points_disponibles -= valeur
                    break
                else:
                    print("Nombre invalide. Réessayez.")
            except ValueError:
                print("Veuillez entrer un nombre entier.")

    # Création du joueur avec CA par défaut = 10 + mod DEX, PV = somme CON*2
    classe_armure = 10 + (stats[1] - 10) // 2  # mod DEX
    pv = stats[2] * 2  # PV de départ basé sur CON

    joueur = Joueur(nom, classe_armure, classe, race, pv, stats)

    print(f"\n✅ Création terminée ! Voici les stats de {joueur.nom} :")
    joueur.afficher_joueur()
    sauvegarder_joueur(joueur)
    return joueur

def menu_principal(joueur):
    while True:
        print("\n=== 🏰 MENU PRINCIPAL ===")
        print("1️⃣  Afficher les informations du joueur")
        print("2️⃣  Combattre un monstre")
        print("3️⃣  Sauvegarder le joueur")
        print("4️⃣  Quitter le jeu")

        choix = input("\n👉 Que souhaitez-vous faire ? ")

        match choix:

            case "1":
                joueur.afficher_joueur()

            case "2":
                monstres = initialisation_data()
                combat1 = Combat(joueur, monstres)
                combat1.combat_tour()

            case "3":
                sauvegarder_joueur(joueur)

            case "4":
                sauvegarder_joueur(joueur)
                print("👋 À bientôt, aventurier !")
                break

            case _:
                print("❌ Choix invalide. Réessayez.")


def main():
    joueur = creation_joueur()
    menu_principal(joueur)

main()