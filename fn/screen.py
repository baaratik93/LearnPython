from fn.control import CustomSplit,IsCorrect,IsExistClient,CustomAppend,CustomLength
# operators ={
#             "ORANGE":["776280898","782324455"],
#             "EXPRESSO":["706280898","709997865","709909988"],
#             "PROMOBILE":["756280898","754569988"],
#             "FREE":["766458877","769806657"]
#             }
from os import system
def ShowOperator(name,o):
    tmp = len(o) * "\t| {:5}"
    print("\t\t",len(o[0])*len(o)*(2)*'-'+'------')
    print(name,tmp.format(*o))
    
def ListOperator(TabOp,operators):
    for k in TabOp:
        if k in ["EXPRESSO","PROMOBILE","ORANGE"]:
            ShowOperator("\t\t {}:".format(k),operators[k])
        else:
            ShowOperator("\t\t {}:\t".format(k),operators[k])

def OperatorConstructTable():
    list = CustomSplit(input("Entrer une liste d'opérateurs séparés par un tiret(-): "),"-")
    for k in list:
        if k not in ["EXPRESSO","PROMOBILE","ORANGE","FREE"]:
            system("clear")
            print("L'opérateur {} n'existe pas".format(k))
            OperatorConstructTable()
    return list
    

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
    
def Menu(operateurs,clients):
    MenuGenerate(["CLIENTS PAR OPERATEUR","CLIENTS D'UN OPERATEUR","NUMEROS D'UN CLIENT","QUITTER\t\t"])
    choix = input("\t\t\tEntrer votre choix: ")
    if choix == "1":
        for i in operateurs:
            print("{:15}|{:15}|{:15}|{:15}|".format(i))
    elif choix == "2":
        ""
    elif choix == "3":
        ""
    elif choix == "4":
        exit
    else:
        system("clear")
        print("\t\t\tChoix incorrect, Faites un bonchoix!!!")
        Menu()
def MenuGenerate(list):
    for i in range(CustomLength(list)):
        print("\t\t\t+---------------------------------------+")
        print('\t\t\t|\t{} -\t{}\t|'.format(i+1,list[i]))
        if i == CustomLength(list)-1:
            print("\t\t\t+---------------------------------------+")
            
