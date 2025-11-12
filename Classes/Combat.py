from Classes.HeritageEntite.Joueur import Joueur
from Classes.HeritageEntite.Monstre import Monstre
from Classes.Enum.MonstreEnum import Taille, Alignement, Type, Puissance
from Classes.Enum.MonstreEnum import XP_PUISSANCE
from Classes.Enum.JoueurEnum import Classe, Race

from Classes.HeritageObjets.Arme import Arme
from Classes.HeritageObjets.Armure import Armure, TypeArmure
from Classes.HeritageObjets.Consommable import Consommable
from Classes.Inventaire import Inventaire

from random import randint

class Combat:

    # Classe principale gérant un combat entre un joueur et un ou plusieurs monstres.
    def __init__(self, joueur, monstres):
        self.joueur = joueur  
        self.monstres = monstres # Liste de monstres
        self.tourGeneral = [] # Ordre d’initiative pour le tour courant
        self.morts = [] # Liste des monstres vaincus
        self.tour = 1 # Numéro du tour

    # --- Getters / Setters ---



    @property
    def joueur(self):
        return self._joueur

    @joueur.setter
    def joueur(self, value):
        self._joueur = value

    @property
    def monstres(self):
        return self._monstres

    @monstres.setter
    def monstres(self, value):
        self._monstres = value

    @property
    def tourGeneral(self):
        return self._tourGeneral

    @tourGeneral.setter
    def tourGeneral(self, value):
        self._tourGeneral = value
    
    @property
    def morts(self):
        return self._morts

    @morts.setter
    def morts(self, value):
        self._morts = value
    
    @property
    def tour(self):
        return self._tour

    @tour.setter
    def tour(self, value):
        if value < 1:
            raise ValueError("Le numéro du tour doit être supérieur ou égal à 1.")
        self._tour = value



    # --- Getters / Setters ---



    def afficher_combat(self):
        print("=== Combat ===")
        print("Joueur:")
        self.joueur.afficher_joueur()
        print("\nMonstres:")
        for monstre in self.monstres:
            monstre.afficher_monstre()


    """
        Calcule et affiche l'ordre d'initiative du tour.
        Chaque participant (joueur et monstres) lance un d20 + modificateur de DEX.
    """
    def initiative_tourGeneral(self):

        self.tourGeneral = []
        print(f"\n--- Tour {self.tour} ---")

        # Initiative des monstres
        for monstre in self.monstres:
            init = randint(1, 20) + monstre.modificateurs[1] #mod DEX
            nom = monstre.nom + str(monstre.idM)
            self.tourGeneral.append([monstre, nom, init])
        
        # Initiative du joueur
        init = randint(1, 20) + self.joueur.modificateurs[1] #mod DEX
        self.tourGeneral.append([self.joueur, self.joueur.nom, init])

        # Tri décroissant par valeur d’initiative
        self.tourGeneral.sort(key=lambda x: x[2], reverse=True)

        print("=== Participant avec Initiative ===")
        for participant in self.tourGeneral:
            print(f"{participant[1]} avec une initiative de {participant[2]}")
        print("=================================== \n")
        return self.tourGeneral


    """
        Interface textuelle pour les actions du joueur à son tour.
        Retourne un code d'action pour la gestion du flux du combat.
    """   
    def interface_combat(self):

        print(f"C'est le tour de {self.joueur.nom}.")
        print("----------------------------------\n")
        print("1. Attaquer")
        print("2. Utiliser une compétence (non implémentée)")
        print("3. Utiliser un objet (non implémentée)")
        print("4. Fuir le combat")

        while True:
            choix = input("Choisissez une action: ")
            match choix:
                # Le joueur attaque
                case "1":
                    self.attaque_joueur()
                    return 1
                # Le joueur utilise une compétence (à implémenter)
                case "2":
                    print("Compétence utilisée ! (fonctionnalité à implémenter)")
                    return 2
                # Le joueur utilise un objet (à implémenter)
                case "3":
                    print("Objet utilisé ! (fonctionnalité à implémenter)")
                    return 3
                # Le joueur fuit le combat
                case "4":
                    print(f"{self.joueur.nom} fuit le combat !")
                    return 4
                case _:
                    print("Choix invalide.")

    """
        Gère un tour complet de combat :
        - Détermine l'ordre d'initiative
        - Fait agir chaque participant à tour de rôle
        - Relance un nouveau tour si le combat n’est pas terminé
    """
    def combat_tour(self):
        tourGeneral = self.initiative_tourGeneral()

        for participant in tourGeneral:

            # Tour du joueur
            if participant[0] == self.joueur:
                res = self.interface_combat()
                if res == 4: # fuite
                    print("Le combat est terminé.")
                    return
            # Tour d’un monstre
            else:
                monstre = participant[0]
                if monstre.pv > 0:
                    print("----------------------------------")
                    print(f"C'est le tour de {participant[1]}.")
                    res = self.attaque_monstre(monstre)
                    if res == 1:  # joueur vaincu
                        print("Le combat est terminé, le joueur a été vaincu.")
                        return
                    
        # Si le combat continue, relancer un nouveau tour
        if self.joueur.pv > 0 and len(self.monstres) > 0:
            self.tour += 1
            self.combat_tour()
        else :
            print("Le combat est terminé, tous les ennemis ont été vaincu !")
            self.gagner_xp()


    """
        Permet au joueur d'attaquer un monstre sélectionné.
        Gère la réussite, les dégâts, et la mort éventuelle du monstre.
    """
    def attaque_joueur(self):

        # Choisir une cible parmi les monstres
        print(f"Quel monstre voulez-vous attaquer ?")
        for participant in self.tourGeneral:
            if participant[0] != self.joueur:
                print(f"- {participant[1]} (ID: {participant[0].idM})")

        # Sélection de la cible par ID
        cible_id = int(input("Entrez l'ID du monstre cible: "))
        monstres_vivants = [p[0] for p in self.tourGeneral if not isinstance(p[0], type(self.joueur))]
        cible = next((m for m in monstres_vivants if m.idM == cible_id), None)

        if cible:
            # Attaque du joueur
            print(f"{self.joueur.nom} attaque {cible.nom}{str(cible_id)} !")
            res = randint(1, 20)
            print(f"Résultat de l'attaque: {res+ self.joueur.modificateurs[0]}")

            # Vérification de la réussite de l'attaque
            match res :
                case 20 :
                    print("Coup critique !")
                    arme = self.joueur.inventaire.arme_equipee()  
                    if arme:
                        degats = randint(1, arme.degat) + self.joueur.modificateurs[0]
                    else:
                        degats = randint(1, 1) + self.joueur.modificateurs[0]  # Attaque à mains nues
                    cible.pv -= degats
                    print(f"Dégâts infligés: {degats}. PV restants de {cible.nom}: {cible.pv}")
                    print("----------------------------------\n")
                case 1 :
                    print("Échec critique ! L'attaque rate automatiquement.")
                    return
                case _ :
                    if res+self.joueur.modificateurs[0] >= cible.classe_armure:
                        print(f"Attaque réussie contre {cible.nom} !")

                        # Calcul des dégâts avec l'arme équipée
                        arme = self.joueur.inventaire.arme_equipee()  
                        if arme:
                            degats = randint(1, arme.degat) + self.joueur.modificateurs[0]
                        else:
                            degats = randint(1, 1) + self.joueur.modificateurs[0]  # Attaque à mains nues
                        cible.pv -= degats
                        print(f"Dégâts infligés: {degats}. PV restants de {cible.nom}: {cible.pv}")
                        print("----------------------------------\n")
                    else:             
                        print(f"Attaque ratée contre {cible.nom}.")
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
            print("Monstre cible non trouvé.")

    """
        Permet à un monstre d'attaquer le joueur.
        Gère la réussite de l’attaque et les dégâts infligés.
    """
    def attaque_monstre(self, monstre: Monstre):
        
        # Attaque du monstre
        print(f"{monstre.nom} attaque {self.joueur.nom} !")
        res = randint(1, 20)
        print(f"Résultat de l'attaque: {res+monstre.modificateurs[0]}")

        # Vérification de la réussite de l'attaque
        match res :  
            case 20 :
                print("Coup critique !")
                degats = (randint(1, 8) + monstre.modificateurs[0]) * 2  # Dégâts doublés pour un coup critique
                self.joueur.pv -= degats
                print(f"Dégâts infligés: {degats}. PV restants de {self.joueur.nom}: {self.joueur.pv}")
                print("----------------------------------\n")
            case 1 :
                print("Échec critique ! L'attaque rate automatiquement.")
                return 0
            case _ :
                if res + monstre.modificateurs[0] >= self.joueur.classe_armure:
                    print(f"Attaque réussie contre {self.joueur.nom} !")
                    degats = randint(1, 8) + monstre.modificateurs[0]  # Supposons que le monstre utilise un dé à 8 faces
                    self.joueur.pv -= degats
                    print(f"Dégâts infligés: {degats}. PV restants de {self.joueur.nom}: {self.joueur.pv}")
                    print("----------------------------------\n")
                else:
                    print(f"Attaque ratée contre {self.joueur.nom}.")
                    print("----------------------------------\n")
                    return 0
        if self.joueur.pv <= 0:
            print(f"{self.joueur.nom} est vaincu !")
            return 1
        return 0 

    """
        Calcule et attribue l'expérience totale gagnée par le joueur
        en fonction de la puissance des monstres vaincus.
    """
    def gagner_xp(self):
        total_xp = sum(XP_PUISSANCE[monstre.puissance] for monstre in self.morts)
        self.joueur.experience += total_xp
        print(f"{self.joueur.nom} gagne {total_xp} points d'expérience ! Total XP: {self.joueur.experience}")
        self.joueur.level_up()
