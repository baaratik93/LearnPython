from fn.control import CustomSplit,IsCorrect,IsExistClient,CustomAppend

def ShowOperator(name,o):
    tmp = len(o) * "\t| {:5}"
    print("\t\t",len(o[0])*len(o)*(2)*'-'+'------')
    print(name,tmp.format(*o))


def OperatorConstructTable():
    return CustomSplit(input("Entrer une liste d'opérateurs séparés par un tiret(-): "),"-")
    

def AddStudent():
    nom = input("Entrer le nom de l'étudiant: ")
    prenom = input("Entrer le prénom de l'étudiant: ")
    numero = input("Entrer le numéro de téléphone de l'étudiant: ")
    if not IsCorrect(numero):
        AddStudent()
    else:
        return {"nom":nom,"prenom":prenom,"telephone":numero}

def SaisieDeClient(clients):
    client = AddStudent()
    if client:
        if not IsExistClient(clients,client):
            clients = CustomAppend(clients,client)
            operateur = WhatOperator(client["telephone"])
            return [clients,client["telephone"],operateur]
        else:
            print("Ce client existe déja")

def WhatOperator(num):
    code = num[0]+num[1]
    if code in ["77","78"]:
        return "ORANGE"
    elif code == "76":
        return "FREE"
    elif code == "75":
        return "PROMOBILE"
    elif code == "70":
        return "EXPRESSO"
    else:
        return False