from ..Objet import Objet

class Arme(Objet) :

    def __init__(self, nom, prix, rarete, degat, propriete=None, equiper=False):
        super().__init__(nom=nom, prix=prix, type="Arme", rarete=rarete, propriete=propriete)
        self.degat = degat
        self.equiper = equiper
    
    @property
    def idArme(self):
        return self._idArme

    @idArme.setter
    def idArme(self, value):
        if value < 1:
            raise ValueError("L'ID doit être au moins 1")
        self._idArme = value
       
    @property
    def degat(self):
        return self._degat

    @degat.setter
    def degat(self, value):
        if value < 0:
            raise ValueError("Les dégâts doivent être positifs.")
        self._degat = value

    @property
    def equiper(self):
        return self._equiper
    
    @equiper.setter
    def equiper(self, valeur: bool):
        """Setter pour équiper ou déséquiper l’armure"""
        self._equiper = valeur
    
    def equiper_arme(self):
        if not self._equiper:
            self._equiper = True
            print(f"✅ {self.nom} équipé.")
        else:
            self._equiper = False
            print(f"✅ {self.nom} déséquipé.")
    
    def afficher_arme(self):
        """Affiche les informations complètes de l'arme."""
        print("-" * 30)
        print(f"Nom : {self.nom}")
        print(f"Dégâts : 1d{self.degat}")
        print(f"Equipée : {'Oui' if self.equiper else 'Non'}")
        print(f"Prix : {self.prix} pièces")
        print(f"Type : {self.type}")
        print(f"Rareté : {self.rarete}")
        if self.propriete:
            print(f"Propriétés spéciales : {self.propriete}")
        print("-" * 30)
