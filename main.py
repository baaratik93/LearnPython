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
from fn.screen import ShowOperator
from fn.screen import OperatorConstructTable
clients = [
    {
        "prenom": "Penda",
        "nom":  "DIA",
        "telepone": "776280898"
    },
    {
        "prenom": "Yaya",
        "nom":  "Wade",
        "telepone": "766280898"
    },
    {
        "prenom": "Amina",
        "nom":  "THIAM",
        "telepone": "756280898"
    },
    {
        "prenom": "Dooro",
        "nom":  "Dieng",
        "telepone": "706280898"
    }
]

operators ={
            "ORANGE":["776280898","782324455","779897656"],
            "EXPRESSO":["706280898","709997865"],
            "PROMOBILE":["756280898","754569988"],
            "FREE":["766458877","769806657"]
            }
# ORANGE-PROMOBILE-FREE-EXPRESSO
TabOp = OperatorConstructTable()
ShowOperator("{}:\t\t\t".format(TabOp[0]),operators[TabOp[0]])
ShowOperator("{}:\t\t\t".format(TabOp[2]),operators[TabOp[2]])
ShowOperator("{}:\t\t".format(TabOp[3]),operators[TabOp[3]])


# operator = input("Entrer une suite d'opérateurs téléphonique")
#Ranger les contacts sur un dictionnaire de liste

# for i in operators:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


