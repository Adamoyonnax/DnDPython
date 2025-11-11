from random import randint

class Entite:

    # Constructor de la classe Entite.
    def __init__(self, nom, classe_armure, pv, stats):
        self.nom = nom
        self.classe_armure = classe_armure
        self.pv = pv
        self.stats = stats # Liste de 6 statistiques [FOR, DEX, CON, INT, SAG, CHA]
        self.modificateurs = [self.calcul_mod(stat) for stat in stats] # Modificateurs correspondants

    # --- Getters / Setters ---



    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def classe_armure(self):
        return self._classe_armure

    @classe_armure.setter
    def classe_armure(self, value):
        self._classe_armure = value

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, value):          
        self._pv = value

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, value):
        self._stats = value
        self._modificateurs = [self.calcul_mod(stat) for stat in value]

    @property
    def modificateurs(self):
        return self._modificateurs

    @modificateurs.setter
    def modificateurs(self, new_stats):
        self._modificateurs = new_stats



    # --- Getters / Setters ---



    # Calcule le modificateur d'une statistique selon la règle D&D : (stat - 10) // 2
    def calcul_mod(self, stat):
        return (stat - 10) // 2


    def afficher_stats(self):
        stats_names = ["FOR", "DEX", "CON", "INT", "SAG", "CHA"]
        print("Stats :")
        for i in range(len(self.stats)):
            print(f"  {stats_names[i]}: {self.stats[i]} (Mod: {self.modificateurs[i]})")

