from ..Objet import Objet

class Arme(Objet) :

    compteur_idArme = 0

    def __init__(self, nom, prix, rarete, degat, propriete=None):
        super().__init__(nom=nom, prix=prix, type="Arme", rarete=rarete, propriete=propriete)
        self.degat = degat
        Arme.compteur_idArme += 1
        self.idArme = Arme.compteur_idArme
    
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

    def afficher_armes(self):
        """Affiche les informations complètes de l'arme."""
        print(f"Nom : {self.nom}")
        print(f"Dégâts : 1d{self.degat}")
        print(f"Prix : {self.prix} pièces")
        print(f"Type : {self.type}")
        print(f"Rareté : {self.rarete}")
        if self.propriete:
            print(f"Propriétés spéciales : {self.propriete}")
        print("-" * 30)

bâton = Arme(
    nom="Bâton", 
    degat=6, 
    prix=2, 
    rarete="Commune",
    propriete="Polyvalente (1d8)"
)

dague = Arme(
    nom="Dague", 
    degat=4, 
    prix=2, 
    rarete="Commune",
    propriete="Finesse, légère, lancer (portée 6 m/18 m)"
)

gourdin = Arme(
    nom="Gourdin", 
    degat=4, 
    prix=1, 
    rarete="Commune",
    propriete="Légère"
)

hachette = Arme(
    nom="Hachette", 
    degat=6, 
    prix=5, 
    rarete="Peu commune",
    propriete="Légère, lancer (portée 6 m/18 m)"
)

javeline = Arme(
    nom="Javeline", 
    degat=6, 
    prix=5, 
    rarete="Peu commune",
    propriete="Lancer (portée 9 m/36 m)"
)

armes = [bâton, dague, gourdin, hachette, javeline]

for arme in armes:
    arme.afficher_armes()
