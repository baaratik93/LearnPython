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
from fn.screen import ShowOperator,OperatorConstructTable,SaisieDeClient,CustomAppend
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
# ORANGE-PROMOBILE-FREE-EXPRESSO
#SAISIE DES OPERATEURS
TabOp = OperatorConstructTable()

# AFFICHAGE DES OPERATEURS
for k in TabOp:
    if k in ["EXPRESSO","PROMOBILE","ORANGE"]:
        ShowOperator("\t\t {}:".format(k),operators[k])
    else:
        ShowOperator("\t\t {}:\t".format(k),operators[k])
        
# AJOUT D'UN ETUDIANT
data = SaisieDeClient(clients)
clients = data[0]
CustomAppend(operators[data[2]],data[1])

for k in TabOp:
    if k in ["EXPRESSO","PROMOBILE","ORANGE"]:
        ShowOperator("\t\t {}:".format(k),operators[k])
    else:
        ShowOperator("\t\t {}:\t".format(k),operators[k])


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


