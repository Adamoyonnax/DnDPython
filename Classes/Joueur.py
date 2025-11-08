from .Enum.JoueurEnum import Race
from .Enum.JoueurEnum import Classe

from .Entite import Entite

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

    def __init__(self, nom, classe_armure, classe, race, pv, stats):
        super().__init__(nom, classe_armure, pv, stats)
        Joueur.compteur_idJ += 1
        self.experience = 0
        self.idJ = Joueur.compteur_idJ
        self.niveau = 1
        self.classe = classe
        self.race = race
        self.degat= 10
        self.appliquer_bonus_race()

    def appliquer_bonus_race(self):
        # stats = [FOR, DEX, CON, INT, SAG, CHA]
        if self.race == Race.ELF:
            self.stats[1] += 2  # +2 DEX
            self.stats[4] += 1  # +1 SAG
        elif self.race == Race.NAIN:
            self.stats[2] += 2  # +2 CON
            self.stats[0] += 1  # +1 FOR
        elif self.race == Race.HUMAIN:
            self.stats = [stat + 1 for stat in self.stats]
        # Ajouter d'autres races selon ton Enum Race

        # Optionnel : recalculer PV et classe d'armure après les bonus
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



