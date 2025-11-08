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

    def afficher_joueur(self):
        print(f"👤 Joueur: {self.nom} (ID: {self.idJ})")
        print(f"Niveau: {self.niveau}")
        print(f"Expérience: {self.experience}")
        print(f"Classe: {self.classe.value}")
        print(f"Race: {self.race.value}")
        print(f"Points de Vie: {self.pv}")
        print(f"Classe d'Armure: {self.classe_armure}")
        self.afficher_stats()



