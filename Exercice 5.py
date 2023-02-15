from os import system

jaune = '\033[93m'
bleu = '\033[94m'
rouge = '\033[91m'

def Main():
    system("clear")     
    print("Entrerl l'ordre de la matrice")
    ordre = int(input())
    MenuPrincipale(ordre)

def PremiereDiagonale(ordre, color):
    system('clear')
    for i in range(ordre):
        for j in range(ordre):
            
            if j != i:
                continue
            else:
                print(color + 2 * i * '*')


def DeuxiemeDiagonale(ordre, color):
    system('clear')
    for i in range(ordre):
        for j in range(ordre):
            if j != i:
                continue
            else:
                print(color + 2 * i * " " + (2 * ordre - 2 * i) * '*')

def MenuPrincipale(n):
    system('clear')
    print('\t\t+--------------+')
    print('\t\t|  1 - BLEU    |')
    print('\t\t+--------------+')
    print('\t\t+--------------+')
    print('\t\t|  2 - ROUGE   |')
    print('\t\t+--------------+')
    print('\t\t+--------------+')
    print('\t\t|  0 - QUITTER |')
    print('\t\t+--------------+')
    print("\t\tEntrer votre choix: ")
    choix = input()
    if choix != '1' and choix != '2' and choix != '0':
        MenuPrincipale()
    elif choix == '1':
        MenuSecondaire(bleu,n)
    elif choix == '2':
        print("rouge")
        MenuSecondaire(rouge,n)
    else:
        exit
        
def MenuSecondaire(couleur, ordre):
    system('clear')
    print('\t\t+--------------+')
    print('\t\t|  1 - HAUT    |')
    print('\t\t+--------------+')
    print('\t\t+--------------+')
    print('\t\t|  2 - BAS     |')
    print('\t\t+--------------+')
    print('\t\t+--------------+')
    print('\t\t|  0 - QUITTER |')
    print('\t\t+--------------+')
    print("\t\tEntrer votre choix: ")
    choix = input()
    if choix != '1' and choix != '2' and choix != '0':
        MenuSecondaire()
    elif choix == '1':
        DeuxiemeDiagonale(ordre,couleur)
    elif choix == '2':
        PremiereDiagonale(ordre, couleur)
    else:
        exit
        
Main()