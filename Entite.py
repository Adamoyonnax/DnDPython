class Entite:

    def __init__(self, nom, classe_armure, pv, stats):
        self.nom = nom
        self.classe_armure = classe_armure
        self.pv = pv
        self.stats = stats
        self.modificateurs = [self.calcul_mod(stat) for stat in stats]

    def calcul_mod(self, stat: int):
        return (stat - 10) // 2

    def afficher_stats(self):
        stats_names = ["FOR", "DEX", "CON", "INT", "SAG", "CHA"]
        print("Stats :")
        for i in range(len(self.stats)):
            print(f"  {stats_names[i]}: {self.stats[i]} (Mod: {self.modificateurs[i]})")

