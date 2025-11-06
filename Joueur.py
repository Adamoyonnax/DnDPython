from Enum.JoueurEnum import Race
from Enum.JoueurEnum import Classe
from Entite import Entite

# 🔹 Sous-classe Joueur
class Joueur(Entite):
    compteur_id = 0

    def __init__(self, nom, niveau, classe_armure, classe, race, pv, stats):
        super().__init__(nom, classe_armure, pv, stats)
        Joueur.compteur_id += 1
        self.id = Joueur.compteur_id
        self.niveau = niveau
        self.classe = classe
        self.race = race

    def afficher_joueur(self):
        print(f"👤 Joueur: {self.nom} (ID: {self.id})")
        print(f"Niveau: {self.niveau}")
        print(f"Classe: {self.classe.value}")
        print(f"Race: {self.race.value}")
        print(f"Points de Vie: {self.pv}")
        print(f"Classe d'Armure: {self.classe_armure}")
        self.afficher_stats()


