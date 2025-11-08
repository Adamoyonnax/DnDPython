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


class Puissance(Enum):
    ZERO = "0"
    UH = "1/8"
    UQ = "1/4"
    UD = "1/2"
    UN = "1"
    DEUX = "2"
    TROIS = "3"
    QUATRE = "4"
    CINQ = "5"
    SIX = "6"
    SEPT = "7"
    HUIT = "8"
    NEUF = "9"
    DIX = "10"
    ONZE = "11"
    DOUZE = "12"
    TREIZE = "13"
    QUATORZE = "14"
    QUINZE = "15"
    SEIZE = "16"
    DIX_SEPT = "17"
    DIX_HUIT = "18"
    DIX_NEUF = "19"
    VINGT = "20"
    VINGT_ET_UN = "21"
    VINGT_DEUX = "22"
    VINGT_TROIS = "23"
    VINGT_QUATRE = "24"
    TRENTE = "30"

XP_PUISSANCE = {
    Puissance.ZERO: 10,
    Puissance.UH: 25,
    Puissance.UQ: 50,
    Puissance.UD: 100,
    Puissance.UN: 200,
    Puissance.DEUX: 450,
    Puissance.TROIS: 700,
    Puissance.QUATRE: 1100,
    Puissance.CINQ: 1800,
    Puissance.SIX: 2300,
    Puissance.SEPT: 2900,
    Puissance.HUIT: 3900,
    Puissance.NEUF: 5000,
    Puissance.DIX: 5900,
    Puissance.ONZE: 7200,
    Puissance.DOUZE: 8400,
    Puissance.TREIZE: 10000,
    Puissance.QUATORZE: 11500,
    Puissance.QUINZE: 13000,
    Puissance.SEIZE: 15000,
    Puissance.DIX_SEPT: 18000,
    Puissance.DIX_HUIT: 20000,
    Puissance.DIX_NEUF: 22000,
    Puissance.VINGT: 25000,
    Puissance.VINGT_ET_UN: 33000,
    Puissance.VINGT_DEUX: 41000,
    Puissance.VINGT_TROIS: 50000,
    Puissance.VINGT_QUATRE: 62000,
    Puissance.TRENTE: 155000
}