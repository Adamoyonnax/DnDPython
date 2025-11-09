from Classes.Joueur import Joueur
from Classes.Monstre import Monstre
from Classes.Enum.MonstreEnum import Taille, Alignement, Type, Puissance
from Classes.Enum.MonstreEnum import XP_PUISSANCE
from Classes.Enum.JoueurEnum import Classe, Race

from random import randint

class Combat:

    def __init__(self, joueur, monstres):
        self.joueur = joueur #Un joueur  
        self.monstres = monstres #Liste de monstres
        self.tourGeneral = []
        self.morts = []
        self.tour = 1

    def afficher_combat(self):
        print("=== Combat ===")
        print("Joueur:")
        self.joueur.afficher_joueur()
        print("\nMonstres:")
        for monstre in self.monstres:
            monstre.afficher_monstre()
    
    def initiative_tourGeneral(self):

        self.tourGeneral = []
        
        print(f"\n--- Tour {self.tour} ---")
        for monstre in self.monstres:
            init = randint(1, 20) + monstre.modificateurs[1] #mod DEX
            nom = monstre.nom + str(monstre.idM)
            self.tourGeneral.append([monstre, nom, init])
        
        init = randint(1, 20) + self.joueur.modificateurs[1] #mod DEX
        self.tourGeneral.append([self.joueur, self.joueur.nom, init])

        self.tourGeneral.sort(key=lambda x: x[2], reverse=True)

        print("=== Participant avec Initiative ===")
        for participant in self.tourGeneral:
            print(f"{participant[1]} avec une initiative de {participant[2]}")
        print("=================================== \n")
        return self.tourGeneral

    def interface_combat(self):
        print(f"C'est le tour de {self.joueur.nom}.")
        print("----------------------------------\n")
        print("1. Attaquer")
        print("2. Utiliser une compétence (non implémentée)")
        print("3. Utiliser un objet (non implémentée)")
        print("4. Fuir le combat (non implémentée)")

        while True:
            choix = input("Choisissez une action: ")
            match choix:
                case "1":
                    self.attaque_joueur()
                    return 1
                case "2":
                    print("Compétence utilisée ! (fonctionnalité à implémenter)")
                    return 2
                case "3":
                    print("Objet utilisé ! (fonctionnalité à implémenter)")
                    return 3
                case "4":
                    print(f"{self.joueur.nom} fuit le combat !")
                    return 4
                case _:
                    print("Choix invalide.")

    def combat_tour(self):
        tourGeneral = self.initiative_tourGeneral()

        for participant in tourGeneral:
            if participant[0] == self.joueur:
                res = self.interface_combat()
                if res == 4:
                    print("Le combat est terminé.")
                    return
            else:
                monstre = participant[0]
                if monstre.pv > 0:
                    print("----------------------------------")
                    print(f"C'est le tour de {participant[1]}.")
                    res = self.attaque_monstre(monstre)
                    if res == 1:
                        print("Le combat est terminé, le joueur a été vaincu.")
                        return

        if self.joueur.pv > 0 and len(self.monstres) > 0:
            self.tour += 1
            self.combat_tour()
        else :
            print("Le combat est terminé, tous les ennemis ont été vaincu !")
            self.gagner_xp()

    def attaque_joueur(self):
        # Choisir une cible parmi les monstres
        print(f"Quel monstre voulez-vous attaquer ?")
        for participant in self.tourGeneral:
            if participant[0] != self.joueur:
                print(f"- {participant[1]} (ID: {participant[0].idM})")
        cible_id = int(input("Entrez l'ID du monstre cible: "))

        monstres_vivants = [p[0] for p in self.tourGeneral if not isinstance(p[0], type(self.joueur))]
        cible = next((m for m in monstres_vivants if m.idM == cible_id), None)

        # Cible trouvée
        if cible:
            # Attaque du joueur
            print(f"{self.joueur.nom} attaque {cible.nom}{str(cible_id)} !")
            res = randint(1, 20) + self.joueur.modificateurs[0]
            print(f"Résultat de l'attaque: {res}")

            # Vérification de la réussite de l'attaque
            if res >= cible.classe_armure:
                print(f"Attaque réussie contre {cible.nom} !")
                degats = randint(1, self.joueur.degat) + self.joueur.modificateurs[0]
                cible.pv -= degats
                print(f"Dégâts infligés: {degats}. PV restants de {cible.nom}: {cible.pv}")
                print("----------------------------------\n")

                # Vérification si le monstre est vaincu
                if cible.pv <= 0:
                    print(f"{cible.nom} est vaincu !")
                    # Retirer de la liste d’initiative
                    self.tourGeneral = [
                        participant for participant in self.tourGeneral
                        if participant[0] != cible
                    ]

                    # Retirer de la liste de monstres vivants
                    self.monstres = [
                        monstre for monstre in self.monstres
                        if monstre != cible
                    ]

                    self.morts.append(cible)

            else:             
                print(f"Attaque ratée contre {cible.nom}.")
                print("----------------------------------\n")
        else:
            print("Monstre cible non trouvé.")

    def attaque_monstre(self, monstre: Monstre):
        
        print(f"{monstre.nom} attaque {self.joueur.nom} !")
        res = randint(1, 20) + monstre.modificateurs[0]
        print(f"Résultat de l'attaque: {res}")

        # Vérification de la réussite de l'attaque
        if res >= self.joueur.classe_armure:
            print(f"Attaque réussie contre {self.joueur.nom} !")
            degats = randint(1, 8) + monstre.modificateurs[0]  # Supposons que le monstre utilise un dé à 8 faces
            self.joueur.pv -= degats
            print(f"Dégâts infligés: {degats}. PV restants de {self.joueur.nom}: {self.joueur.pv}")
            print("----------------------------------\n")
            # Vérification si le joueur est vaincu
            if self.joueur.pv <= 0:
                print(f"{self.joueur.nom} est vaincu !")
                return 1
            return 0
        else:
            print(f"Attaque ratée contre {self.joueur.nom}.")
            print("----------------------------------\n")
            return 0

    def gagner_xp(self):
        total_xp = sum(XP_PUISSANCE[monstre.puissance] for monstre in self.morts)
        self.joueur.experience += total_xp
        print(f"{self.joueur.nom} gagne {total_xp} points d'expérience ! Total XP: {self.joueur.experience}")
        self.joueur.level_up()
    