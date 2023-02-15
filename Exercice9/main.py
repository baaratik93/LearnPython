# Écrire un programme qui permet la saisie
# 1. Saisir une suite d’ opérateurs téléphoniques
# (Orange,Tigo,expresso,...) puis génère une matrice dont le nombre de
# lignes est égal au nombre d’opérateurs saisis.
# 1. Saisir les informations d’un client (nom,prénom,numéro téléphone) et
# le ranger dans la ligne de l'opérateur correspondant à son numéro de
# téléphone.
# 2. Afficher les clients de la matrice par opérateurs
# 3. Afficher les clients d’un opérateur
# 4. Afficher les numéros téléphone d’un client
# 5. Modifier ou ajouter un numero telephone pour un client
# 6. Lorsque l’utilisateur quitte le programme, les données de la matrice
# sont enregistrées dans un fichier texte.
from fn.screen import OperatorConstructTable,SaisieDeClient,CustomAppend,ListOperator,Menu
from os import system
clients = [
    {
        "prenom": "Penda",
        "nom":  "DIA",
        "telephone": "776280898"
    },
    {
        "prenom": "Yaya",
        "nom":  "Wade",
        "telephone": "766280898"
    },
    {
        "prenom": "Amina",
        "nom":  "THIAM",
        "telephone": "756280898"
    },
    {
        "prenom": "Dooro",
        "nom":  "Dieng",
        "telephone": "706280898"
    }
]

operators ={
            "ORANGE":["776280898","782324455"],
            "EXPRESSO":["706280898","709997865","709909988"],
            "PROMOBILE":["756280898","754569988"],
            "FREE":["766458877","769806657"]
            }
#SAISIE DES OPERATEURS
# OperatorConstructTable() Donne la main pour saisir une liste d'opérateur et de stocker dans la variable TabOp
TabOp = OperatorConstructTable()

# AFFICHAGE DES OPERATEURS
ListOperator(TabOp,operators)
        
# AJOUT D'UN ETUDIANT
# Cette fonction reçoit la liste de clients existantes, ajoute un client puis renvoie
# une liste contenant successivement 3 éléments:
# data[0] <=> la nouvelle liste de client
# data[1] <=> le numéro de téléphone du nouveau client
# data[2] <=> le nom de l'opérateur
data = SaisieDeClient(clients)
clients = data[0]
# Ajouter le nouveau nouveau numéro à la liste de numéro de l'opérateur concerné
CustomAppend(operators[data[2]],data[1])
# Actualiser la liste d'opérateur à afficher
if not data[2] in TabOp:
    CustomAppend(TabOp,data[2])
#Actualiser l'affichage
ListOperator(TabOp,operators)
Menu(operators,clients)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


