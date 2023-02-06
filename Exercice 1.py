fr = ["Janvier","Février","Mars", "Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
eng = ["January","February","March", "April","May","June","July","Agust","September","October","November","December"]
mois=[]
def afficherMois(List):
        mois.append(List[0:12:3])
        mois.append(List[1:12:3])
        mois.append(List[2:12:3])
        for row in mois:
            print('| {:15} | {:15} | {:15} | {:15} |'.format(*row))
        
def saisie():
    c = input()
    if c == '1':
        afficherMois(fr)
        saisie()
    elif c == '2':
        afficherMois(eng)
        saisie()
    elif c == '3':
        exit
    else:
        saisie()
print("1-Mois en français")
print("2-Mois en anglais")
print("3-Quitter")
print("Choix:")
afficherMois(fr)
saisie()