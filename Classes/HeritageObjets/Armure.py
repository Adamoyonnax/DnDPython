from Classes.Objet import Objet  
from enum import Enum

# Enum pour définir les types d'armures
class TypeArmure(Enum):
    LEGERE = "Armure légère"
    INTERMEDIAIRE = "Armure intermédiaire"
    LOURDE = "Armure lourde"

class Armure(Objet):

    # Classe représentant une armure héritant d'Objet.
    def __init__(self, nom, typearmure, prix, rarete, protection, force_min, propriete=None, equiper=False):
        super().__init__(nom=nom, prix=prix, type="Armure", rarete=rarete, propriete=propriete)
        self.protection = protection # Bonus de CA
        self.force_min = force_min # Force minimale pour porter l'armure
        self.typearmure= typearmure # Type d'armure (Enum)
        self.equiper = equiper # Booléen indiquant si l'arme est équipée



    # --- Getters / Setters --- 



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

    @property
    def equiper(self):
        return self._equiper
    
    @equiper.setter
    def equiper(self, valeur: bool):
        """Setter pour équiper ou déséquiper l’armure"""
        self._equiper = valeur



    # --- Getters / Setters ---



    # Permet à un joueur d'équiper ou déséquiper l'armure.
    # Vérifie la force minimale avant d'équiper.   
    def equiper_armure(self, joueur):
        if not self._equiper:
            if joueur.stats[0] >= self.force_min:   # stats[0] = Force
                self._equiper = True
                print(f"✅ {self.nom} équipé.")
            else:
                print("⚠️ Force insuffisante pour équiper cette armure.")
        else:
            self._equiper = False
            print(f"✅{self.nom} déséquipé.")

    def afficher_armure(self):
        print(f"Nom : {self.nom}")
        print(f"Type d'armure : {self.typearmure.value}")
        print(f"Force minimale requise : {self.force_min}")
        print(f"Equipée : {'Oui' if self.equiper else 'Non'}")
        print(f"Bonus CA : {self.protection}")
        print(f"Prix : {self.prix} pièces")
        print(f"Rareté : {self.rarete}")
        if self.propriete:
            print(f"Propriétés spéciales : {self.propriete}")
        print("-" * 30)
