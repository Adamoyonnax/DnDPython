from Classes.Objet import Objet  
from enum import Enum


class TypeArmure(Enum):
    LEGERE = "Armure légère"
    INTERMEDIAIRE = "Armure intermédiaire"
    LOURDE = "Armure lourde"

class Armure(Objet):

    compteur_idArmure = 0

    def __init__(self, nom, typearmure, prix, rarete, protection, force_min, propriete=None):
        super().__init__(nom=nom, prix=prix, type="Armure", rarete=rarete, propriete=propriete)
        self.protection = protection
        self.force_min = force_min
        self.typearmure= typearmure
        Armure.compteur_idArmure += 1
        self.idArmure = Armure.compteur_idArmure
    
    @property
    def idArmure(self):
        return self._idArmure
    
    @idArmure.setter
    def idArmure(self, value):
        if value < 1:
            raise ValueError("L'ID doit être au moins 1")
        self._idArmure = value

    @property
    def protection(self):
        return self._protection

    @protection.setter
    def protection(self, value):
        if value < 0:
            raise ValueError("La protection doit être positive.")
        self._protection = value

    @property
    def force_min(self):
        return self._force_min

    @force_min.setter
    def force_min(self, value):
        self._force_min = value

    @property
    def typearmure(self):
        return self._typearmure

    @typearmure.setter
    def typearmure(self, value):
        self._typearmure = value

    def afficher_armure(self):
        print(f"Nom : {self.nom}")
        print(f"Type d'armure : {self.typearmure.value}")
        print(f"Force minimale requise : {self.force_min}")
        print(f"Bonus CA : {self.protection}")
        print(f"Prix : {self.prix} pièces")
        print(f"Rareté : {self.rarete}")
        if self.propriete:
            print(f"Propriétés spéciales : {self.propriete}")
        print("-" * 30)

cotte_mailles = Armure(
    nom="Cotte de mailles",
    typearmure=TypeArmure.INTERMEDIAIRE,
    prix=75,
    rarete="Peu commune",
    protection=15,
    force_min=13,
    propriete="Lourde, bruit métallique"
)

cotte_mailles.afficher_armure()
