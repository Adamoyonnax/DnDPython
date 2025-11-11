from ..Enum.JoueurEnum import Race
from ..Enum.JoueurEnum import Classe
from Classes.HeritageObjets.Arme import Arme
from Classes.HeritageObjets.Armure import Armure
from Classes.HeritageObjets.Consommable import Consommable

from ..Entite import Entite

# Dictionnaire définissant l'expérience nécessaire pour chaque niveau
XP_PALIERS = {
    1: 0,
    2: 300,
    3: 900,
    4: 2700,
    5: 6500,
    6: 14000,
    7: 23000,
    8: 34000,
    9: 48000,
    10: 64000,
    11: 85000,
    12: 100000,
    13: 120000,
    14: 140000,
    15: 165000,
    16: 195000,
    17: 225000,
    18: 265000,
    19: 305000,
    20: 355000
}


class Joueur(Entite):
    compteur_idJ = 0

    # Classe représentant un joueur héritant d'Entite.
    def __init__(self, nom, classe_armure, classe, race, pv, stats):
        super().__init__(nom, classe_armure, pv, stats)
        Joueur.compteur_idJ += 1
        self.experience = 0
        self.idJ = Joueur.compteur_idJ
        self.niveau = 1
        self.classe = classe
        self.race = race
        self.degat= 10
        self.inventaire = None

    # --- Getters / Setters ---



    @property
    def idJ(self):
        return self._idJ

    @idJ.setter
    def idJ(self, value):
        if value < 1:
            raise ValueError("L'ID doit être au moins 1")
        self._idJ = value
    
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError("L'expérience ne peut pas être négative.")
        self._experience = value

    @property
    def niveau(self):
        return self._niveau

    @niveau.setter
    def niveau(self, value):
        if value < 1:
            raise ValueError("Le niveau doit être au minimum 1.")
        self._niveau = value

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._race = value

    @property
    def degat(self):
        return self._degat

    @degat.setter
    def degat(self, value):
        if value < 0:
            raise ValueError("Les dégâts ne peuvent pas être négatifs.")
        self._degat = value

    @property
    def inventaire(self):
        return self._inventaire

    @inventaire.setter
    def inventaire(self, value):
        self._inventaire = value   

    # --- Getters / Setters ---




    # Applique les bonus raciaux aux statistiques du joueur
    def appliquer_bonus_race(self):
        # stats = [FOR, DEX, CON, INT, SAG, CHA]
        if self.race == Race.ELF:
            self.stats[1] += 2  # +2 DEX
            self.stats[4] += 1  # +1 SAG
        elif self.race == Race.NAIN:
            self.stats[2] += 2  # +2 CON
            self.stats[0] += 1  # +1 FOR
        elif self.race == Race.HUMAIN:
            self.stats = [stat + 1 for stat in self.stats] # +1 à toutes les stats
        # Ajouter d'autres races selon ton Enum Race

        # Recalculer PV et classe d'armure après les bonus
        self.classe_armure = 10 + (self.stats[1] - 10) // 2
        self.pv = self.stats[2] * 2

    # Applique les bonus de classe aux statistiques du joueur
    def appliquer_bonus_classe(self):
        # stats = [FOR, DEX, CON, INT, SAG, CHA]
        if self.classe == Classe.GUERRIER:
            self.stats[0] += 2  # +2 FOR
            self.stats[2] += 1  # +1 CON
        elif self.classe == Classe.ROUBLARD:
            self.stats[1] += 2  # +2 DEX
            self.stats[0] += 1  # +1 FOR
        elif self.classe == Classe.MAGE:
            self.stats[3] += 2  # +2 INT
            self.stats[4] += 1  # +1 SAG
        # Ajouter d'autres classes selon ton Enum Classe

        # Recalculer PV et classe d'armure après les bonus
        self.classe_armure = 10 + (self.stats[1] - 10) // 2
        self.pv = self.stats[2] * 2

    def afficher_joueur(self):
        print(f"👤 Joueur: {self.nom} (ID: {self.idJ})")
        print(f"Niveau: {self.niveau}")
        print(f"Expérience: {self.experience}")
        print(f"Classe: {self.classe.value}")
        print(f"Race: {self.race.value}")
        print(f"Points de Vie: {self.pv}")
        print(f"Classe d'Armure: {self.classe_armure}")
        self.afficher_stats()

    # Vérifie si le joueur a atteint un nouveau palier d'expérience et augmente le niveau si nécessaire.
    def level_up(self):
        for niveau, palier in sorted(XP_PALIERS.items()) :
            if self.experience < palier:
                return           
            if niveau > self.niveau:
                print(f"✨ Level up ! Vous êtes passé niveau {niveau} !")
                self.niveau = niveau

