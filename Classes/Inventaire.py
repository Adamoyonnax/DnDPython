from Classes.Objet import Objet  
from Classes.HeritageObjets.Armure import Armure, TypeArmure
from Classes.HeritageObjets.Arme import Arme
from Classes.HeritageObjets.Consommable import Consommable
from Classes.HeritageEntite.Joueur import Joueur
from Classes.Enum.JoueurEnum import Classe, Race


class Inventaire() :
    def __init__(self, inventaire):
        self.inventaire = inventaire  # Contient [[Objet, int], [Objet, int]]

    def afficher_inventaire(self) :
        print("----------------------")
        for objet in self.inventaire :
            print(f"Nom : {objet[0].nom} (ID : {objet[0].idO} )")
            print(f"Quantité : {objet[1]}")
            print("----------------------")
    
    def ajouter_objet(self, objet, quantite):
        for item in self.inventaire:
            if item[0] == objet:
                item[1] += quantite
                return
        self.inventaire.append([objet, quantite])
    
    def retirer_objet(self, id, quantite) :
        for item in self.inventaire :
            if item[0].idO == id:
                if item[1] <= quantite :
                    self.inventaire.remove(item)
                    return
                else :
                    item[1] -= quantite

    def objet_par_type(self, type_objet):
        objets_type = []
        for item in self.inventaire:
            if item[0].type == type_objet:
                print(f"Nom : {item[0].nom} (ID : {item[0].idO} ) - Quantité : {item[1]}")
                objets_type.append(item)
        return objets_type

    def arme_equipee(self):
        for obj, quantite in self.inventaire:
            if isinstance(obj, Arme) and obj.equiper:
                return obj
        return None
      