
import json
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Classes.HeritageEntite.Joueur import Joueur
from Classes.Enum.JoueurEnum import Classe, Race

from Classes.HeritageEntite.Monstre import Monstre
from Classes.Enum.MonstreEnum import Taille, Alignement, Type, Puissance

from Classes.HeritageObjets.Arme import Arme
from Classes.HeritageObjets.Armure import Armure, TypeArmure
from Classes.HeritageObjets.Consommable import Consommable
from Classes.Inventaire import Inventaire



# ========================== SAUVEGARDE DU JOUEUR ========================== #



# Sauvegarde le joueur dans un fichier JSON, y compris son inventaire.
def sauvegarder_joueur(joueur, fichier="Sauvegarde/joueur.json"):
    inventaire_data = []   

    # On parcourt les objets de l’inventaire du joueur
    for obj, quantite in joueur.inventaire.inventaire:  
        # Données communes à tous les objets
        obj_data = {
            "idO": obj.idO,
            "nom": obj.nom,
            "prix": obj.prix,
            "type": obj.type,
            "rarete": obj.rarete,
            "propriete": obj.propriete,
        }

        # Données spécifiques selon le type d’objet
        match obj.type:
            case "Armure":
                obj_data.update({
                    "protection": obj.protection,
                    "typearmure": obj.typearmure.name if obj.typearmure else None,
                    "force_min": obj.force_min,
                    "equiper": obj.equiper
                })
            case "Arme":
                obj_data.update({
                    "degat": obj.degat,
                    "equiper": obj.equiper
                })
            case "Consommable":
                pass  # aucun attribut supplémentaire
        
        # Ajout de l’objet et de sa quantité à la liste d’inventaire sérialisée
        inventaire_data.append({"objet": obj_data, "quantite": quantite})

    # Données principales du joueur
    data = {
        "idJ": joueur.idJ,
        "nom": joueur.nom,
        "classe": joueur.classe.name,
        "race": joueur.race.name,
        "classe_armure": joueur.classe_armure,
        "pv": joueur.pv,
        "stats": joueur.stats,
        "niveau": joueur.niveau,
        "experience": joueur.experience,
        "inventaire": inventaire_data
    }
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)
    print("💾 Joueur sauvegardé avec succès !")



# ========================== CHARGEMENT DU JOUEUR ========================== #



# Charge un joueur sauvegardé depuis un fichier JSON, y compris son inventaire.
def charger_joueur(fichier="Sauvegarde/joueur.json"):
    # Charge un joueur existant depuis un fichier JSON, y compris son inventaire.
    if not os.path.exists(fichier):
        return None

    with open(fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Reconstruction de l'inventaire
    inventaire_instances = []
    for item in data.get("inventaire", []):
        objet_data = item["objet"]
        quantite = item["quantite"]

        # Reconstruction selon le type d'objet
        type_objet = objet_data["type"]
        if type_objet == "Armure":
            typearmure = None
            if objet_data.get("typearmure"):
                try:
                    typearmure = TypeArmure[objet_data["typearmure"]]
                except KeyError:
                    print(f"⚠️ TypeArmure inconnu : {objet_data['typearmure']}")
            objet = Armure(
                nom=objet_data["nom"],
                typearmure=typearmure,
                prix=objet_data["prix"],
                rarete=objet_data["rarete"],
                protection=objet_data["protection"],
                force_min=objet_data["force_min"],
                propriete=objet_data["propriete"]
            )
            objet.equiper =objet_data["equiper"]

        elif type_objet == "Arme":
            objet = Arme(
                nom=objet_data["nom"],
                prix=objet_data["prix"],
                rarete=objet_data["rarete"],
                degat=objet_data["degat"],
                propriete=objet_data["propriete"]
            )
            objet.equiper =objet_data["equiper"]

        elif type_objet == "Consommable":
            objet = Consommable(
                nom=objet_data["nom"],
                prix=objet_data["prix"],
                rarete=objet_data["rarete"],
                propriete=objet_data["propriete"]
            )
        else:
            print(f"⚠️ Type d'objet inconnu dans l'inventaire : {type_objet}")
            continue

        # Création de l’objet Inventaire à partir des instances reconstituées
        inventaire_instances.append([objet, quantite])
        inventaire = Inventaire(inventaire_instances)

    # Création du joueur
    joueur = Joueur(
        nom=data["nom"],
        classe_armure=data["classe_armure"],
        classe=Classe[data["classe"]],
        race=Race[data["race"]],
        pv=data["pv"],
        stats=data["stats"],
    )

    # Application des attributs restants
    joueur.inventaire=inventaire
    joueur.idJ = data["idJ"]
    joueur.niveau = data["niveau"]
    joueur.experience = data["experience"]

    print(f"✅ Joueur {joueur.nom} chargé depuis la sauvegarde !")
    return joueur



# ========================== SAUVEGARDE / CHARGEMENT DES MONSTRES ========================== #



# Sauvegarde une liste de monstres dans un fichier JSON.
def sauvegarder_monstres(monstres, fichier="Sauvegarde/monstres.json"):
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

# Charge la liste des monstres depuis un fichier JSON et recrée leurs instances.    
def charger_monstres(fichier="Sauvegarde/monstres.json"):

    if not os.path.exists(fichier):
        return []
    with open(fichier, "r") as f:
        data = json.load(f)

    monstres = []
    for monstre_data in data:
        # Reconstitution du monstre avec conversion des champs Enum
        monstre = Monstre(
            nom=monstre_data["nom"],
            taille=Taille[monstre_data["taille"]],
            puissance=Puissance[monstre_data["puissance"]],  
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



# ========================== SAUVEGARDE / CHARGEMENT DES OBJETS ========================== #



# Sauvegarde une liste d’objets (armes, armures, consommables) dans un fichier JSON.
def sauvegarder_objets(objets, fichier="Sauvegarde/objets.json") :
    data = []
    for objet in objets:
        # Données communes
        objet_data = {
            "idO": objet.idO,
            "nom": objet.nom,
            "prix": objet.prix,
            "type": objet.type,
            "rarete": objet.rarete,
            "propriete": objet.propriete
        }

        # Données spécifiques selon le type
        type = objet.type 
        match type :
            case "Armure" :
                objet_data.update({
                    "protection": objet.protection,
                    "typearmure": objet.typearmure.name,
                    "equiper": objet.equiper,
                    "force_min": objet.force_min,
                })  
            case "Arme" :
                objet_data.update({
                    "degat": objet.degat,
                    "equiper": objet.equiper,
                })
            case _ :
                pass

        data.append(objet_data)

    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("💾 Objets sauvegardés avec succès !")

# Charge tous les objets depuis le fichier JSON et recrée leurs instances correspondantes.
def charger_objets(fichier="Sauvegarde/objets.json"):

    objets = []
    with open(fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        type_objet = item["type"]

        if type_objet == "Armure":
            objet = Armure(
                nom=item["nom"],
                typearmure = TypeArmure[item["typearmure"]],
                prix=item["prix"],
                rarete=item["rarete"],
                protection=item["protection"],
                force_min=item["force_min"],
                propriete=item["propriete"],
                equiper=item["equiper"]
            )

        elif type_objet == "Arme":
            objet = Arme(
                nom=item["nom"],
                prix=item["prix"],
                rarete=item["rarete"],
                degat=item["degat"],
                propriete=item["propriete"],
                equiper=item["equiper"]
            )

        elif type_objet == "Consommable":
            objet = Consommable(
                nom=item["nom"],
                prix=item["prix"],
                rarete=item["rarete"],
                propriete=item["propriete"],
            )

        else:
            print(f"⚠️ Type d'objet inconnu : {type_objet}")
            continue

        objets.append(objet)

    print(f"📦 {len(objets)} objets chargés avec succès !")
    return objets

# Charge un objet spécifique depuis son nom.
def charger_objet(objet_nom, fichier="Sauvegarde/objets.json") :
    with open(fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data :
        # Reconstruction selon le type d’objet
        if item["nom"] == objet_nom :
            if item["type"] == "Armure":
                objet = Armure(
                    nom=item["nom"],
                    typearmure=TypeArmure[item["typearmure"]],
                    prix=item["prix"],
                    rarete=item["rarete"],
                    protection=item["protection"],
                    force_min=item["force_min"],
                    propriete=item["propriete"],
                    equiper=item["equiper"]
                )
                objet.idO = item["idO"]
                
            elif item["type"] == "Arme":
                objet = Arme(
                    nom=item["nom"],
                    prix=item["prix"],
                    rarete=item["rarete"],
                    degat=item["degat"],
                    propriete=item["propriete"],
                    equiper=item["equiper"]
                )
                objet.idO = item["idO"]
            else :
                objet = Consommable(
                    nom=item["nom"],
                    prix=item["prix"],
                    rarete=item["rarete"],
                    propriete=item["propriete"],
                )
                objet.idO = item["idO"]
            return objet
    else:
        # Si aucun objet ne correspond
        print(f"⚠️ Objet inconnu")
        return None
