
class Objet:

    compteur_idO = 0

    def __init__(self, nom, prix, type, rarete, propriete=None):
        Objet.compteur_idO += 1
        self.idO = Objet.compteur_idO 
        self.nom = nom
        self.prix = prix
        self.type = type
        self.rarete = rarete
        self.propriete = propriete

    # --- Getters / Setters ---
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        if value < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        self._prix = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def rarete(self):
        return self._rarete

    @rarete.setter
    def rarete(self, value):
        self._rarete = value

    @property
    def propriete(self):
        return self._propriete

    @propriete.setter
    def propriete(self, value):
        self._propriete = value