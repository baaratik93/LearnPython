# Proposer un programme qui permet la saisie :


# ○ ADDS, au-dessus de la diagonale secondaire.
# ○ EDDS, en dessous de la diagonale secondaire
# ○ SDS, sur la diagonale secondaire
# ● Un Menu de choix ayant comme options des couleurs
# Lorsque l’utilisateur valide, le programme devra dessiner la matrice en la coloriant suivant les
# couleurs et les positions choisies par l’utilisateur.
# Initialiser un tableau de couleurs. Ce tableau sera utilisé pour générer le Menu choix des
# couleurs.
# Initialiser un tableau de positions formé des valeurs :
# ○ ADDP, au-dessus de la diagonale principale.
# ○ EDDP, en dessous de la diagonale principale
# ○ SDP, sur la diagonale principale
# ○ ADDS, au-dessus de la diagonale secondaire.
# ○ EDDS, en dessous de la diagonale secondaire
# ○ SDS, sur la diagonale secondaire
# Ce tableau sera utilisé pour générer les options du menu de position.
# Règles de Gestion
# ● A chaque choix d’une position on devra l’associer a une couleur.
# ● Toutes les valeurs sont Obligatoires
# ● Le champ de saisi de l’ordre de la matrice est un entier et est supérieur à 4
# ● Une couleur est choisie une et une seule fois
from os import system
# ● De l’ordre d’une matrice carrée
def MenuPrincipale():
    system("clear")
    o = Main()
    c = MenuCouleur()
    MenuPosition(o,c)
def MenuChangerCouleur(ordre):
    system("clear")
    c = MenuCouleur()
    MenuPosition(ordre,c)
def Main():    
    print("Entrerl l'ordre de la matrice")
    return int(input())
    
def Couleur():
    return {"noir":"\033[0;30m","rouge":"\033[0;31m","vert": "\033[0;32m","jaune": "\033[0;33m","bleu": "\033[0;34m","violet": "\033[0;35m","cyan": "\033[0;36m","blanc": "\033[0;37m"}

def Position ():
    return ["ADDP","EDDP","SDP","ADDS","EDDS","SDS"]


# ● Un Menu de choix pour la position de la couleur
def MenuCouleur():
    system('clear')
    all = Couleur()
    k=0
    for i in all:
        k+=1
        print('\t\t+-----------------------+')
        print('\t\t|     {} - {}     \t|'.format(k,i))
        print('\t\t+-----------------------+')
    print('\t\t+-----------------------+')
    print('\t\t|     9 - QUITTER  \t|')
    print('\t\t+-----------------------+')
    print("Choisissez une couleur")
    c = int(input())
    if(c==9):
        system("clear")
        exit()
    else:
        return all[list(all)[c-1]]
def MenuPosition(order,color):
    k=0
    for i in Position():
        k+=1
        print('\t\t+-----------------------+')
        print('\t\t|     {} - {}     \t|'.format(k,i))
        print('\t\t+-----------------------+')
    print('\t\t+-----------------------+')
    print('\t\t|     0 - RETOUR  \t|')
    print('\t\t+-----------------------+')
    print("Choisissez une position")
    c = input()
    if c=='1':
        ADDP(order, color)
    elif c=='2':
        EDDP(order, color)
    elif c=='3':
        SDP(order, color)
    elif c=='4':
        ADDS(order, color)
    elif c=='5':
        EDDS(order, color)
    elif c=='6':
        SDS(order, color)
    elif c=='0':
        MenuChangerCouleur(order)
    else:
        MenuPosition(order,color)
            

# ○ ADDP, au-dessus de la diagonale principale.   
def ADDP(ordre, color):
    system('clear')
    for i in range(ordre):
        for j in range(ordre):
            if j == i:
                print(color + 3 * i * ' ' + (ordre-i)  * ' * ')
    MenuPosition(ordre,color)
# ○ EDDP, en dessous de la diagonale principale
def EDDP(ordre,color):
    system('clear')
    for i in range(ordre):
        for j in range(ordre):
            if j == i:
                print(color + j * ' * ')
    MenuPosition(ordre,color)
                
# ○ SDP, sur la diagonale principale

def SDP(ordre, color):
    system('clear')
    for i in range(ordre):
        for j in range(ordre):
            if j == i:
                print(color + 2 * i * "  " + "*")
    MenuPosition(ordre,color)

def SDS(n, color):
    system('clear')
    for i in range(n):
        for j in range(n):
            if i==j:
                print(color + (n-i) * "  "+ " * ")
    MenuPosition(n,color)

def ADDS(n,color):
    system('clear')
    for i in range(n): 
        for j in range(n):
            if i == j:
                print(color + (n-j) * ' * ')
    MenuPosition(n,color)
          
def EDDS(n, color):
    system('clear')
    for i in range(n): 
        for j in range(n):
            if i == j:
                print(color + '   ' * (n-j) + j * ' * ')
    MenuPosition(n,color)
          

MenuPrincipale()