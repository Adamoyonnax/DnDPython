from Monstre import Monstre
from Joueur import Joueur
from Enum.MonstreEnum import Taille, Alignement, Type
from Enum.JoueurEnum import Classe, Race

import json
import os

def sauvegarder_joueur(joueur, fichier="joueur.json"):
    """Sauvegarde le joueur dans un fichier JSON."""
    data = {
        "nom": joueur.nom,
        "classe": joueur.classe.name,
        "race": joueur.race.name,
        "classe_armure": joueur.classe_armure,
        "pv": joueur.pv,
        "stats": joueur.stats,
        "niveau": joueur.niveau,
        "experience": joueur.experience
    }
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)
    print("💾 Joueur sauvegardé avec succès !")

def charger_joueur(fichier="joueur.json"):
    """Charge un joueur existant depuis un fichier JSON, s’il existe."""
    if not os.path.exists(fichier):
        return None
    with open(fichier, "r") as f:
        data = json.load(f)
    joueur = Joueur(
        nom=data["nom"],
        classe_armure=data["classe_armure"],
        classe=Classe[data["classe"]],
        race=Race[data["race"]],
        pv=data["pv"],
        stats=data["stats"]
    )
    joueur.niveau = data["niveau"]
    joueur.experience = data["experience"]
    print(f"✅ Joueur {joueur.nom} chargé depuis la sauvegarde !")
    return joueur

def initialisation_data():
    monstre1 = Monstre("Orc", Taille.M, 20, Alignement.CB, Type.HUMANOIDE, 13, 22, [14, 10, 12, 8, 10, 9])
    monstre2 = Monstre("Gobelin", Taille.P, 20, Alignement.NM, Type.HUMANOIDE, 15, 7, [8, 14, 10, 10, 8, 8])
    monstres = [monstre1, monstre2]
    return monstres 
    
def creation_joueur():
    # Si une sauvegarde existe, proposer de la recharger
    joueur_existant = charger_joueur()
    if joueur_existant:
        choix = input("Un joueur sauvegardé a été trouvé. Voulez-vous le charger ? (O/N) : ").lower()
        if choix == "o":
            print("\n✅ Joueur chargé avec succès :")
            joueur_existant.afficher_joueur()
            return joueur_existant
        else:
            print("⚠️ Création d’un nouveau joueur. L’ancienne sauvegarde sera remplacée.\n")

    print("=== Bienvenue dans le jeu de DnD Python ===\n")
    print("=== Création d'un Joueur ===")

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

def menu_principal(joueur, monstres):
    while True:
        print("\n=== 🏰 MENU PRINCIPAL ===")
        print("1️⃣  Afficher les informations du joueur")
        print("2️⃣  Combattre un monstre")
        print("3️⃣  Gagner de l'expérience (test)")
        print("4️⃣  Sauvegarder le joueur")
        print("5️⃣  Quitter le jeu")

        choix = input("\n👉 Que souhaitez-vous faire ? ")

        if choix == "1":
            joueur.afficher_joueur()

        elif choix == "2":
            print("\n⚔️  Combat non implémenté — à venir.")

        elif choix == "3":
            # Simulation de gain d'expérience pour tester la progression
            joueur.gagner_xp(10000)

        elif choix == "4":
            # Sauvegarder le joueur
            sauvegarder_joueur(joueur)

        elif choix == "5":
            # Quitter le jeu
            sauvegarder_joueur(joueur)
            print("👋 À bientôt, aventurier !")
            break

        else:
            print("❌ Choix invalide. Réessayez.")


def main():
    monstres = initialisation_data()
    joueur = creation_joueur()
    menu_principal(joueur, monstres)

main()