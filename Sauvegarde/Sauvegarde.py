
import json
import os

from Classes.Joueur import Joueur
from Classes.Enum.JoueurEnum import Classe, Race

def sauvegarder_joueur(joueur, fichier="Sauvegarde/joueur.json"):
    """Sauvegarde le joueur dans un fichier JSON."""
    data = {
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
    joueur.niveau = data["niveau"]
    joueur.experience = data["experience"]
    print(f"✅ Joueur {joueur.nom} chargé depuis la sauvegarde !")
    return joueur