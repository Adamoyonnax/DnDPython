from Entite import Entite
from Enum.MonstreEnum import Taille, Alignement, Type

class Monstre(Entite):
    compteur_id = 0

    def __init__(self, nom, taille, xp, alignement, type, classe_armure, pv, stats):
        super().__init__(nom, classe_armure, pv, stats)
        Monstre.compteur_id += 1
        self.id = Monstre.compteur_id
        self.xp = xp
        self.taille = taille
        self.alignement = alignement
        self.type = type

    def afficher_monstre(self):
        print(f"👾 Monstre: {self.nom} (ID: {self.id})")
        print(f"Taille: {self.taille.value}")
        print(f"Alignement: {self.alignement.value}")
        print(f"Type: {self.type.value}")
        print(f"Classe d'Armure: {self.classe_armure}")
        print(f"Points de Vie: {self.pv}")
        self.afficher_stats()
