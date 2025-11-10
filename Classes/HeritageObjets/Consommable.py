from Classes.Objet import Objet  

class Consommable(Objet):

    def __init__(self, nom, prix, rarete, propriete=None):
        super().__init__(nom=nom, prix=prix, type="Consommable", rarete=rarete, propriete=propriete)
    
    @property
    def idConsommable(self):
        return self._idConsommable

    @idConsommable.setter
    def idConsommable(self, value):
        if value < 1:
            raise ValueError("L'ID doit être au moins 1")
        self._idConsommable = value

    def afficher_consommable(self):
        print("-" * 30)
        print(f"Nom : {self.nom}")
        print(f"Prix : {self.prix} pièces")
        print(f"Rareté : {self.rarete}")
        if self.propriete:
            print(f"Propriétés spéciales : {self.propriete}")
        print("-" * 30)

potion_vie = Consommable(
    nom="Potion de Soin Mineure",
    prix=50,
    rarete="Commun",
    propriete="Restaure 10 PV lorsqu'elle est utilisée."
)