from Monstre import Monstre
from Joueur import Joueur
from Enum.MonstreEnum import Taille, Alignement, Type
from Enum.JoueurEnum import Classe, Race


def main():
# Création d’un joueur et d’un monstre
    joueur1 = Joueur("Arthas", 5, 16, Classe.GUERRIER, Race.HUMAIN, 45, [16, 12, 14, 10, 13, 8])
    monstre1 = Monstre("Orc", Taille.M, Alignement.CB, Type.HUMANOIDE, 13, 22, [14, 10, 12, 8, 10, 9])
    monstre2 = Monstre("Gobelin", Taille.P, Alignement.NM, Type.HUMANOIDE, 15, 7, [8, 14, 10, 10, 8, 8])
    # Affichage des informations
    joueur1.afficher_joueur()
    print("\n")
    monstre1.afficher_monstre()
    print("\n")
    monstre2.afficher_monstre()


main()