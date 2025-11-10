
import json
import os

from Classes.HeritageEntite.Joueur import Joueur
from Classes.Enum.JoueurEnum import Classe, Race
from Classes.HeritageEntite.Monstre import Monstre
from Classes.Enum.MonstreEnum import Taille, Alignement, Type, Puissance

def sauvegarder_joueur(joueur, fichier="Sauvegarde/joueur.json"):
    """Sauvegarde le joueur dans un fichier JSON."""
    data = {
        "idJ": joueur.idJ,
        "nom": joueur.nom,
        "classe": joueur.classe.name,
        "race": joueur.race.name,
        "classe_armure": joueur.classe_armure,
        "pv": joueur.pv,
        "stats": joueur.stats,
        "niveau": joueur.niveau,
        "experience": joueur.experience
    }
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)
    print("💾 Joueur sauvegardé avec succès !")

def charger_joueur(fichier="Sauvegarde/joueur.json"):

    """Charge un joueur existant depuis un fichier JSON, s’il existe."""
    if not os.path.exists(fichier):
        return None
    with open(fichier, "r") as f:
        data = json.load(f)
    joueur = Joueur(
        nom=data["nom"],
        classe_armure=data["classe_armure"],
        classe=Classe[data["classe"]],
        race=Race[data["race"]],
        pv=data["pv"],
        stats=data["stats"]
    )
    joueur.idJ = data["idJ"]
    joueur.niveau = data["niveau"]
    joueur.experience = data["experience"]
    print(f"✅ Joueur {joueur.nom} chargé depuis la sauvegarde !")
    return joueur

def sauvegarder_monstres(monstres, fichier="Sauvegarde/monstres.json"):
    """Sauvegarde la liste des monstres dans un fichier JSON."""
    data = []
    for monstre in monstres:
        monstre_data = {
            "idM": monstre.idM,
            "nom": monstre.nom,
            "taille": monstre.taille.name,
            "puissance": monstre.puissance.name,
            "alignement": monstre.alignement.name,
            "type": monstre.type.name,
            "classe_armure": monstre.classe_armure,
            "pv": monstre.pv,
            "stats": monstre.stats
        }
        data.append(monstre_data)
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)
    print("💾 Monstres sauvegardés avec succès !")
    
def charger_monstres(fichier="Sauvegarde/monstres.json"):
    """Charge la liste des monstres depuis un fichier JSON."""
    if not os.path.exists(fichier):
        return []
    with open(fichier, "r") as f:
        data = json.load(f)

    monstres = []
    for monstre_data in data:
        monstre = Monstre(
            nom=monstre_data["nom"],
            taille=Taille[monstre_data["taille"]],
            puissance=Puissance[monstre_data["puissance"]],  # On reconvertit en Enum
            alignement=Alignement[monstre_data["alignement"]],
            type=Type[monstre_data["type"]],
            classe_armure=monstre_data["classe_armure"],
            pv=monstre_data["pv"],
            stats=monstre_data["stats"]
        )
        monstre.idM=monstre_data["idM"]
        monstres.append(monstre)
    print("✅ Monstres chargés depuis la sauvegarde !")
    return monstres

