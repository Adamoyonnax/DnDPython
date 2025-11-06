from enum import Enum

class Alignement(Enum):
    LB = "Loyal Bon"
    NB = "Neutre Bon"
    CB = "Chaotique Bon"
    LN = "Loyal Neutre"
    NN = "Neutre"
    CN = "Chaotique Neutre"
    LM = "Loyal Mauvais"
    NM = "Neutre Mauvais"
    CM = "Chaotique Mauvais"

class Taille(Enum):
    TP="Très Petit"
    P="Petit"
    M="Moyen"
    G="Grand"
    TG="Très Grand"

class Type(Enum):
    HUMANOIDE = "Humanoïde"
    ABERRATION = "Aberration"
    ARTIFICIEL = "Artificiel"
    BÊTE = "Bête"
    CELESTE = "Céleste"
    DRAGON = "Dragon"
    ELÉMENTAIRE = "Elémentaire"
    FÉE = "Fée"
    FIELON = "Fiélon"
    GÉANT = "Géant"
    MONSTRUOSITÉ = "Monstruosité"
    MORT_VIVANT = "Mort-vivant"
    PLANTE = "Plante"
    VASE = "Vase"