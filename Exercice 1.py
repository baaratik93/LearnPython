from os import system
fr = ["Janvier","Février","Mars", "Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
eng = ["January","February","March", "April","May","June","July","Agust","September","October","November","December"]
mois=[]
def afficherMois(List):
        mois = [OneLine(List,0),OneLine(List,1),OneLine(List,2)]
        print("\n")
        print("\n")
        for row in mois:
            print("\t\t\t\t-------------------------------------------------------------------------")
            print('\t\t\t\t| {:15} | {:15} | {:15} | {:15} |'.format(*row))
            
        print("\n")
        
def saisie():
    Affichage()
    c = input("\t\t\t\t\t\t\tFaites votre choix: ")
    if c == '1':
        system('clear')
        afficherMois(fr)
        saisie()
    elif c == '2':
        system('clear')
        afficherMois(eng)
        saisie()
    elif c == '3':
        exit
    else:
        saisie()
        
def Affichage():
    print("\t\t\t\t\t\t\t---------------------------------")
    print("\t\t\t\t\t\t\t|\t3-Mois en français\t|")
    print("\t\t\t\t\t\t\t|\t2-Mois en anglais\t|")
    print("\t\t\t\t\t\t\t|\t3-Quitter\t\t|")
    print("\t\t\t\t\t\t\t---------------------------------")
    
def OneLine(list,start):
    newList = []
    for i in range(start,CustomLength(list),3):
        newList.append(list[i])
    return newList

def CustomLength(list):
    k = 0
    for i in list:
        k+=1
    return k
afficherMois(fr)
saisie()