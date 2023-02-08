from os import system
def Menu(e):
    MenuGenerate(["AFFICHER TOUT","TRIER  ","RECHERCHE","MODIFICATION","NOUVEAU","SORTIR"])
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
        
def Entete():
        print('+---------------------------------------------------------------------------------------------------------------------------------------+')
        print('|\tPrénom\t|\tNom\t|\tTéléphone\t|\tClasses\t|\tDev\t|\tProj\t|\tExam\t|\tMoyenne\t|')
        print('+---------------------------------------------------------------------------------------------------------------------------------------+')
def CustomAppend(list,el):
    el = [el]
    list+=el
    return list

def afficherTout(etudiants):
    Entete()
    for etudiant in etudiants:
        ShowSingleStudent(etudiant)
        
def ShowSingleStudent(etudiant):
        etudiant["moy"] = (etudiant["dev"] + etudiant["projet"] + etudiant["exam"])/3
        print('|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{:.2f}\t|'
                .format(etudiant["prenom"],etudiant["nom"],
                etudiant["telephone"],etudiant["classe"],
                etudiant["dev"],etudiant["projet"],
                etudiant["exam"],etudiant["moy"]))
        print('+---------------------------------------------------------------------------------------------------------------------------------------+')
    
    
def TAMenu(e):
    system("clear")
    afficherTout(e)
    MenuGenerate(["CROISSANT","DECROISSANT","RETOUR","QUITTER"])
    choice = input("\t\t\t\tEnter votre choix: ")
    if choice == "2":
        for i in range(len(e)):
            newEtudiant = trier(e,"desc")
        afficherTout(newEtudiant)
        TAMenu(newEtudiant)
    elif choice == "1":
        for i in range(len(e)):
            newEtudiant =trier(e,"asc")
        afficherTout(newEtudiant)
        TAMenu(newEtudiant)
    elif choice == "3":
        system("clear")
        Menu(e)
    else:
        exit
def trier(e,sens):
    if sens=="asc":
        for i in range(0,len(e)):
            for j in range(i+1,len(e)):
                if e[i]["moy"] > e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
    
        return e
    else:
        for i in range(0,len(e)):
            for j in range(i+1,len(e)):
                if e[i]["moy"] < e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
        
        return e
    
    
#---------------- Générateur de Menu -------------

def MenuGenerate(list):
    for i in range(len(list)):
        print('\t\t\t\t+-----------------------+')
        print('\t\t\t\t|    {} - {} \t+'.format(i+1,list[i]))
        print('\t\t\t\t+-----------------------+')
        
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
        afficherTout(e)
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
        
# ------------------ RECHERCHE-------------------

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
    telephone = input("\t\t\t\tEntrer le numéro de téléphone de l'étudiant: ")
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