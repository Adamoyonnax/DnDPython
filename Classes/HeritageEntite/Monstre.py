from ..Entite import Entite
from ..Enum.MonstreEnum import Taille, Alignement, Type

class Monstre(Entite):
    compteur_idM = 0

    # Classe représentant un monstre héritant d'Entite.
    def __init__(self, nom, taille, puissance, alignement, type, classe_armure, pv, stats):
        super().__init__(nom, classe_armure, pv, stats)
        Monstre.compteur_idM += 1
        self.idM = Monstre.compteur_idM
        self.puissance = puissance # Niveau de puissance et XP associée (ENUM)
        self.taille = taille # Taille du monstre (Enum)
        self.alignement = alignement # Alignement du monstre (Enum)
        self.type = type # Type de monstre (Enum)

    # --- Getters / Setters ---



    @property
    def idM(self):
        return self._idM

    @idM.setter
    def idM(self, value):
        if value < 1:
            raise ValueError("L'ID doit être au moins 1")
        self._idM = value
    
    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, value):
        self._puissance = value

    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, value):
        self._taille = value

    @property
    def alignement(self):
        return self._alignement

    @alignement.setter
    def alignement(self, value):
        self._alignement = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value



    # --- Getters / Setters ---



    def afficher_monstre(self):
        print(f"👾 Monstre: {self.nom} (ID: {self.idM})")
        print(f"Taille: {self.taille.value}")
        print(f"Alignement: {self.alignement.value}")
        print(f"Type: {self.type.value}")
        print(f"Classe d'Armure: {self.classe_armure}")
        print(f"Points de Vie: {self.pv}")
        self.afficher_stats()
