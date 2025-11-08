from .Entite import Entite
from .Enum.MonstreEnum import Taille, Alignement, Type

class Monstre(Entite):
    compteur_idM = 0

    def __init__(self, nom, taille, puissance, alignement, type, classe_armure, pv, stats):
        super().__init__(nom, classe_armure, pv, stats)
        Monstre.compteur_idM += 1
        self.idM = Monstre.compteur_idM
        self.puissance = puissance
        self.taille = taille
        self.alignement = alignement
        self.type = type

    def afficher_monstre(self):
        print(f"👾 Monstre: {self.nom} (ID: {self.idM})")
        print(f"Taille: {self.taille.value}")
        print(f"Alignement: {self.alignement.value}")
        print(f"Type: {self.type.value}")
        print(f"Classe d'Armure: {self.classe_armure}")
        print(f"Points de Vie: {self.pv}")
        self.afficher_stats()
