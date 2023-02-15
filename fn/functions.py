from os import system
from os.path import exists
from fn.donnees import Entete,CustomAppend,ShowSingleStudent,MenuGenerate,CustomSort,CustomLength,IsCorrect,StudentsToFile,FileToStudent,IsStudent
def Menu(etudiants):
    if exists("students.txt"):
        e = FileToStudent()
    else:
        e = etudiants
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
        system("clear")
        ModifierEtudiant(e)
    elif choice == "5":
        ControlInput(e)
    elif choice =="6":
        StudentsToFile(e)
        exit    
        
def ControlInput(e):
    NewStudent = SaisiEtudiant(e)
    if NewStudent:
        rep=input("Voulez-vous ajouter un nouveau étudiant (o/n): ")
        if rep == 'o' or rep == "O":
            system("clear")
            NewStudent = ControlInput(e)
        else:
            system("clear")
            ModifierEtudiant(e)

def afficherTout(etudiants):
    Entete()
    for etudiant in etudiants:
        ShowSingleStudent(etudiant)
            
    
def TAMenu(e):
    system("clear")
    afficherTout(e)
    MenuGenerate(["\tCROISSANT","\tDECROISSANT","\tRETOUR\t","\tQUITTER\t"])
    choice = input("\t\t\t\tEnter votre choix: ")
    if choice == "2":
        for i in range(CustomLength(e)):
            newEtudiant = CustomSort(e,"desc")
        afficherTout(newEtudiant)
        TAMenu(newEtudiant)
    elif choice == "1":
        for i in range(CustomLength(e)):
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
    MenuGenerate(["\tPAR NOM\t","\tPAR PRENOM","\tPAR TELEPHONE","\tPAR CLASSE"])
    choix = input("\t\t\t\tChoisir le critère de recherche: ")
    if choix == "1":
        nom = input("\t\t\t\tEntrer le nom de l'étudiant: ")
        etudiant = RecherchePar(e,"nom",nom)
    elif choix == "2":
        prenom = input("\t\t\t\tEntrer le prénom de l'étudiant: ")
        etudiant = RecherchePar(e,"prenom",prenom)
    elif choix == "3":
        telephone = input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant: ")
        telephone = IsCorrect(telephone)
        if not telephone:
            system('clear')
            print("Numéro incorrect")
            RechercheEtudiant(e)
        else:
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
            
    StudentsToFile(list)
    return list
        
# ------------------ MODIFICATION -------------------

def ModifierEtudiant(e):
    afficherTout(e)
    NewStudentList= []
    num = input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant à modifier: ")
    num = IsCorrect(num)
    if not num:
            system("clear")
            print("Ce numéro n'est pas correct")
            ModifierEtudiant(e)
    else:
        MenuGenerate(["\t\tDev","\t\tProj","\t\tExam"])
        choix = input("Choisir la note à modifier: ")
        if choix == "1":
            note = float(input("\t\t\t\tEntrer la nouvelle note Dev: "))
            if note >=0 and note <=20:
                NewStudentList = Modifier(e,num,"dev",note)
            else:
                system("clear")
                print("Veuillez saisir une note comprise entre 0 et 20")
                ModifierEtudiant(e)
        elif choix == "2":
            note = float(input("\t\t\t\tEntrer la nouvelle note Proj: "))
            if note >=0 and note <=20:
                NewStudentList = Modifier(e,num,"projet",note)
            else:
                system("clear")
                print("Veuillez saisir une note comprise entre 0 et 20")
                ModifierEtudiant(e)
        elif choix == "3":
            note = float(input("\t\t\t\tEntrer la nouvelle note Exam: "))
            if note >=0 and note <=20:
                NewStudentList = Modifier(e,num,"exam",note)
            else:
                system("clear")
                print("Veuillez saisir une note comprise entre 0 et 20")
                ModifierEtudiant(e)
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
    telephone = input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant: ")
    telephone = IsCorrect(telephone)
    if not telephone:
            system("clear")
            print("Veuillez saisir un numéro correct")
            SaisiEtudiant(e)
    elif IsStudent(e,int(telephone)):
        system("clear")
        print("Ce numéro existe déja !!! Veuillez saisir un autre!")
        SaisiEtudiant(e)
    classe = input("\t\t\t\tEntrer la classe de l'étudiant: ")
    return CustomAppend(e,{
        "nom": nom,
        "prenom": prenom,
        "telephone": int(telephone),
        "classe": classe,
        "dev": 0.0,
        "projet": 0.0,
        "exam": 0.0
    })