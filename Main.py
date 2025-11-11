from Classes.HeritageEntite.Monstre import Monstre
from Classes.HeritageEntite.Joueur import Joueur
from Classes.Enum.MonstreEnum import Taille, Alignement, Type, Puissance
from Classes.Enum.JoueurEnum import Classe, Race

from Classes.Combat import Combat

from Sauvegarde.Sauvegarde import sauvegarder_joueur, charger_joueur, charger_monstres, charger_objet

from Classes.HeritageObjets.Arme import Arme
from Classes.HeritageObjets.Armure import Armure
from Classes.HeritageObjets.Consommable import Consommable

from Classes.Inventaire import Inventaire

# ====================== MÉTADONNÉES DU PROJET ====================== #



def signature() :
    print("─────────────────────────────────────────────")
    print("Nom du projet : Donjon&Dragon Simulator") 
    print("Auteur : Ademo/Adamoyonnax")
    print("Débuté le : 6/11/2025")
    print("Discord : ademo")
    print("─────────────────────────────────────────────")



# ====================== CRÉATION / CHARGEMENT DU JOUEUR ====================== #



"""
    Crée un nouveau joueur ou charge une sauvegarde existante.
    - Si une sauvegarde est trouvée, demande à l'utilisateur s'il veut la charger.
    - Sinon, procède à la création d'un nouveau joueur avec saisie interactive.
"""
def creation_joueur():
    try:
        # Chargement d'une éventuelle sauvegarde
        joueur_existant = charger_joueur()
        if joueur_existant:
            while True:
                choix = input("Un joueur sauvegardé a été trouvé. Voulez-vous le charger ? (O/N) : ").strip().lower()
                if choix == "o":
                    print("\n✅ Joueur chargé avec succès :")
                    return joueur_existant
                elif choix == "n":
                    print("⚠️ Création d’un nouveau joueur. L’ancienne sauvegarde sera remplacée.\n")
                    break
                else:
                    print("❌ Réponse invalide. Entrez 'O' ou 'N'.")

        print("=== Bienvenue dans le jeu de DnD Python ===")
        print("\n=== Création d'un Joueur ===")

        # Nom du joueur
        while True:
            nom = input("Entrez le nom du joueur: ").strip()
            if nom:
                break
            print("❌ Le nom ne peut pas être vide.")

        # Choix de la classe
        print("\nChoisissez une classe:")
        for c in Classe:
            print(f"- {c.name} ({c.value})")

        while True:
            classe_input = input("Entrez la classe choisie: ").strip().upper()
            if classe_input in Classe.__members__:
                classe = Classe[classe_input]
                break
            print("❌ Classe invalide. Essayez encore.")

        # Choix de la race
        print("\nChoisissez une race:")
        for r in Race:
            print(f"- {r.name} ({r.value})")

        while True:
            race_input = input("Entrez la race choisie: ").strip().upper()
            if race_input in Race.__members__:
                race = Race[race_input]
                break
            print("❌ Race invalide. Essayez encore.")

        # Répartition des statistiques
        print("\nRépartition des statistiques (FOR, DEX, CON, INT, SAG, CHA)")
        stats_noms = ["FOR", "DEX", "CON", "INT", "SAG", "CHA"]
        stats = [0] * 6
        points_disponibles = 70

        for i, stat in enumerate(stats_noms):
            while True:
                try:
                    print(f"Points restants: {points_disponibles}")
                    valeur = int(input(f"Combien de points pour {stat}? "))
                    if 0 <= valeur <= points_disponibles:
                        stats[i] = valeur
                        points_disponibles -= valeur
                        break
                    print("❌ Nombre invalide. Réessayez.")
                except ValueError:
                    print("⚠️ Veuillez entrer un nombre entier.")
        
        # Calcul des valeurs CA et PV
        classe_armure = 10 + (stats[1] - 10) // 2  # mod DEX
        pv = stats[2] * 2  # PV de départ basé sur CON

        # Création du joueur
        joueur = Joueur(nom, classe_armure, classe, race, pv, stats)

        # Application des bonus raciaux et de classe
        joueur.appliquer_bonus_race()
        joueur.appliquer_bonus_classe()

        # Création d’un inventaire de départ (3 objets de base)        
        objet_depart=[]
        objet_depart.append([charger_objet("Bâton"), 1])
        objet_depart.append([charger_objet("Potion de Soin Mineure"), 3])
        objet_depart.append([charger_objet("Cotte de mailles"), 1])
        inventaire = Inventaire(objet_depart)
        joueur.inventaire = inventaire

        print(f"\n✅ Création terminée !")
        sauvegarder_joueur(joueur)

        '''
        # 🔹 Sauvegarde avec gestion d'erreur
        # try:
            sauvegarder_joueur(joueur)
        except Exception as e:
            print(f"⚠️ Erreur lors de la sauvegarde : {e}")
        '''

        return joueur

    except KeyboardInterrupt:
        print("\n🚫 Création annulée par l'utilisateur.")
        return None



# ========================== MENU PRINCIPAL ========================== #



def menu_principal(joueur):
    while True:
        print("\n=== 🏰 MENU PRINCIPAL ===")
        print("1️⃣  Afficher les informations du joueur")
        print("2️⃣  Voir l'inventaire")
        print("3️⃣  Combattre un monstre")
        print("4️⃣  Sauvegarder le joueur")
        print("5️⃣  Quitter le jeu")

        choix = input("\n👉 Que souhaitez-vous faire ? ")

        match choix:

            case "1":
                # Affiche les infos du joueur
                joueur.afficher_joueur()

            case "2":
                # Affiche l'inventaire
                print(f"Inventaire de {joueur.nom}")
                joueur.inventaire.afficher_inventaire()
                interface_inventaire(joueur)

            case "3":
                # Lance un combat contre des monstres chargés depuis la sauvegarde
                monstres = charger_monstres()
                combat1 = Combat(joueur, monstres)
                combat1.combat_tour()

            case "4":
                # Sauvegarde le joueur
                sauvegarder_joueur(joueur)

            case "5":
                # Quitte le jeu après sauvegarde
                sauvegarder_joueur(joueur)
                print("👋 À bientôt, aventurier !")
                break

            case _:
                print("❌ Choix invalide. Réessayez.")


# ====================== INTERFACE D’INVENTAIRE ====================== #


'''
    Interface pour gérer l'inventaire du joueur.
    Permet de jeter des objets ou d'afficher les détails d'un objet spécifique.
'''
def interface_inventaire(joueur) :
    while True:
                print("\n=== 🏰 INVENTAIRE ===")
                print("1️⃣  Jeter un objet")
                print("2️⃣  Détail d'un objet")
                print("3️⃣  Retourner au menu principal")

                choix = input("\n👉 Que souhaitez-vous faire ? ")

                match choix:
                    case "1":
                        # Jeter un objet
                        id = int(input("\n👉 Donner l'ID de l'item que vous souhaitez jeter"))
                        quantite = int(input("👉 Combien ? "))
                        joueur.inventaire.retirer_objet(id, quantite)
                        print("✅ Objet(s) retiré(s) de l'inventaire.")

                    case "2":
                        # Détail d'un objet
                        objet_id = int(input("\n👉 Donner l'ID de l'item dont vous voulez connaître les détails"))
                        detail_objet(joueur, objet_id)

                    case "3":
                        # Retour au menu principal
                        break


"""
    Affiche les détails d’un objet à partir de son ID
    et propose des actions selon le type (équiper, utiliser, etc.)
"""
def detail_objet(joueur, objet_id) :
    # Recherche de l'objet dans l'inventaire
    for objet, quantite in joueur.inventaire.inventaire :
        if objet.idO == objet_id :
            # Affichage des détails selon le type d'objet
            type = objet.type 
            match type :
                case "Arme" :
                    objet.afficher_arme()
                    # Propose d'équiper l'arme
                    while True:
                        choix = input("Souhaitez-vous équiper cette arme ? (O/N)")
                        if choix.lower() == 'o':
                            objet.equiper_arme()
                            break
                        elif choix.lower() == 'n':
                            break
                        else:
                            print("❌ Réponse invalide. Entrez 'O' ou 'N'.")
                case "Armure" :
                    objet.afficher_armure()
                    # Propose d'équiper l'armure
                    while True:
                        choix = input("Souhaitez-vous équiper cette armure ? (O/N)")
                        if choix.lower() == 'o':
                            objet.equiper_armure(joueur)
                            break
                        elif choix.lower() == 'n':
                            break
                        else:
                            print("❌ Réponse invalide. Entrez 'O' ou 'N'.")
                case "Consommable" :
                    objet.afficher_consommable()




# ====================== POINT D’ENTRÉE DU PROGRAMME ====================== #



# Fonction principale du programme (point d'entrée du jeu).
def main():
    joueur = creation_joueur()
    signature()
    menu_principal(joueur)


# Exécution directe du jeu
main()