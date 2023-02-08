from os import system
from fn.donnees import Entete,CustomAppend,ShowSingleStudent,MenuGenerate,CustomSort
def Menu(e):
    MenuGenerate(["\t AFFICHER TOUT","\t TRIER\t","\t RECHERCHE","\t MODIFICATION","\t NOUVEAU","\t SORTIR "])
    choice = input("\t\t\t\tEnter votre choix: ")
    if choice == "1":
        system("clear")
        afficherTout(e)
        Menu(e)
    elif choice == "2":
        TAMenu(e)
    elif choice == "3":
        system("clear")
        RechercheEtudiant(e)
    elif choice == "4":
        ModifierEtudiant(e)
    elif choice == "5":
        ModifierEtudiant(SaisiEtudiant(e))
    elif choice =="6":
        exit    

def afficherTout(etudiants):
    Entete()
    for etudiant in etudiants:
        ShowSingleStudent(etudiant)
            
    
def TAMenu(e):
    system("clear")
    afficherTout(e)
    MenuGenerate(["CROISSANT","DECROISSANT","RETOUR","QUITTER"])
    choice = input("\t\t\t\tEnter votre choix: ")
    if choice == "2":
        for i in range(len(e)):
            newEtudiant = CustomSort(e,"desc")
        afficherTout(newEtudiant)
        TAMenu(newEtudiant)
    elif choice == "1":
        for i in range(len(e)):
            newEtudiant =CustomSort(e,"asc")
        afficherTout(newEtudiant)
        TAMenu(newEtudiant)
    elif choice == "3":
        system("clear")
        Menu(e)
    else:
        exit
    
        
# ------------------ RECHERCHE-------------------

def RechercheEtudiant(e):
    etudiant= {}
    MenuGenerate(["PAR NOM","PAR PRENOM","PAR TELEPHONE","PAR CLASSE"])
    choix = input("\t\t\t\tChoisir le critère de recherche: ")
    if choix == "1":
        nom = input("\t\t\t\tEntrer le nom de l'étudiant: ")
        etudiant = RecherchePar(e,"nom",nom)
    elif choix == "2":
        prenom = input("\t\t\t\tEntrer le prénom de l'étudiant: ")
        etudiant = RecherchePar(e,"prenom",prenom)
    elif choix == "3":
        telephone = input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant: ")
        etudiant = RecherchePar(e,"telephone",int(telephone))
    elif choix == "4":
        classe = input("\t\t\t\tEntrer la classe de l'étudiant: ")
        etudiant = RecherchePar(e,"classe",classe)
    else:
        system("clear")
        print("Veuillez faire un choix correct.")
        RechercheEtudiant(e)
    if choix in ["1","2","3","4"]:
        Entete()
        ShowSingleStudent(etudiant)
        Menu(e)
def RecherchePar(e,critere,valeur):
    system("clear")
    for i in e:
        if i[critere] == valeur:
            return i
def Modifier(list,numero,critere,valeur):
    system("clear")
    for k in list:
        if k["telephone"] != int(numero):
            continue
        else:
            k[critere]=valeur
    return list
        
# ------------------ MODIFICATION -------------------

def ModifierEtudiant(e):
    system("clear")
    afficherTout(e)
    NewStudentList= []
    num = input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant à modifier: ")
    MenuGenerate(["Dev  ","Proj ","Exam "])
    choix = input("Choisir la note à modifier: ")
    if choix == "1":
        note = float(input("\t\t\t\tEntrer la nouvelle note Dev: "))
        NewStudentList = Modifier(e,num,"dev",note)
    elif choix == "2":
        note = float(input("\t\t\t\tEntrer la nouvelle note Proj: "))
        NewStudentList = Modifier(e,num,"projet",note)
    elif choix == "3":
        note = float(input("\t\t\t\tEntrer la nouvelle note Exam: "))
        NewStudentList = Modifier(e,num,"exam",note)
    else:
        system("clear")
        print("Veuillez faire un choix correct.")
        ModifierEtudiant(e)
    if choix in ["1","2","3"]:
        afficherTout(NewStudentList)
        Menu(NewStudentList)
        
# ----------------- SAISI -------------------------

def SaisiEtudiant(e):
    nom = input("\t\t\t\tEntrer le nom de l'étudiant: ")
    prenom = input("\t\t\t\tEntrer le prénom de l'étudiant: ")
    telephone = int(input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant: "))
    classe = input("\t\t\t\tEntrer la classe de l'étudiant: ")
    return CustomAppend(e,{
        "nom": nom,
        "prenom": prenom,
        "telephone": telephone,
        "classe": classe,
        "dev": 0.0,
        "projet": 0.0,
        "exam": 0.0
    })