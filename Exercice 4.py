# Écrire un programme qui permet de remplir N numéros à partir d’une chaîne. Le programme
# réaffiche les numéros valides à gauche et les numéros invalides à droite de l’écran. Le
# programme affichera aussi le nombre de numéros de chaque opérateur.
# Règles de Gestion
# ● La chaîne de saisie des numéros est obligatoire
# ● Les numéros doivent être valides.
# ● Un numéro est valide :
# ○ S’il commence par 77,78,76,70 ou 75
# ○ S’il contient que 9 chiffres
# ○ Un numéro peut contenir des espaces
import os
NumeroInvalide = []
def reverse(text):
    rev = ''
    for i in range(len(text), 0, -1):
        rev += text[i-1]
    return rev
def FistNumber(ch):
    num = ""
    for i in ch:
        if i != '-':
            num+=i
        else:
            break
    return num
def LastNumber(ch):
    b=reverse(ch)
    return reverse(FistNumber(b))

def ListNumero(ch):
  t = ""
  l = len(ch) - 1
  b = []
  j=0
  for i in ch:
    if i != '-':
      t += i
    else:
      b.append(t)
      t = ""
      continue
  b.append(LastNumber(ch))
  return b

#VERIFIER LA LONGUEUR DU NUMERO
def EstNeuf(N):
    if len(N) != 9:
        return False
    else:
        return True

def ListNormal(list):
    NewList = []
    for k in list:
        code = k[0]+k[1]
        if EstNeuf(k) and (code == '77' or code == '78' or code == '76' or code == '70' or code == '75'):
            NewList.append(k)
        else:
            NumeroInvalide.append(k)
    return NewList

def PresenceOperateur(list):
    orange = []
    expresso = []
    free= []
    promobile = []
    for i in list:
        code = i[0]+i[1]
        if code == '77' or code=='78':
            orange.append(i)
        elif code == '76':
            free.append(i)
        elif code == '70':
            expresso.append(i)
        elif code == '75':
            promobile.append(i)
        else:
            print("Ce numéro n'est pas d'un opérateur existant")
    return [orange,expresso,free,promobile]
    
#VERIFIER SI L'UTILISATEUR NE SAISIE PAS DE CARACTERE ALPHABETIQUE
def ChiffreSeulement(ph):
    t=0
    for i in ph:
        if i >= '0' and i <= '9':
            continue
        else:
            t+=1
    if t != 0:
      return False
    else:
      return True
    

#SUPPRIMER LES ESPACES
def SansEspace(list):
    NewList = []
    for n in list:
        num = ''
        for k in n:
            if k == ' ':
                continue
            else:
                num = num + k
        NewList.append(num)
    return NewList
        
#SAISIR UN NUMERO DE TELEPHONE
def SaisieDeTelephone():
    annuaire = []
    print("Entrer la liste de numéro de téléphone séparé par un tiret(-):  ")
    list = input()
    #VÉRIFIER SI LE NUMERO N'EST PAS VIDE
    if list == '':
        os.system('clear')
        print("Assurez-vous d'avoir un ou des numéros.")
        SaisieDeTelephone()
    wnb = SansEspace(ListNumero(list))
    for i in wnb:
        if not ChiffreSeulement(i):
            NumeroInvalide.append(i)
            # os.system("clear")
            print("Un numéro de téléphone ne peut pas contenir de lettre")
            # SaisieDeTelephone()
        else:
            annuaire.append(i)
    return [wnb, annuaire]
        
# 77 628 08 98 - 77 448 51 32 - 77 969 59 98 - 7hkjhk -77 989 09 89 -0OPI
# 98 765 66 78 - jhjjgh - 77 666 66 66 - 76 666 66 66 - 78 666 66 66 - HKJHkjhk- 7865 -75 6666666 -70448 5132
annuaire = SaisieDeTelephone()
NumeroValide = ListNormal(annuaire[1])
operateurs = PresenceOperateur(NumeroValide)
# print("Voici l'annuaire saisie",annuaire[0])
# print("Voici les numéros valides: ",NumeroValide )
# print("Voici les numéros invalide",NumeroInvalide)
tailleTableau = 0
if len(NumeroInvalide) >= len(NumeroValide):
    tailleTableau = len(NumeroInvalide)
else:
    tailleTableau = len(NumeroValide)

for e in range(tailleTableau):
    print('{}\t|\t{}'.format(NumeroValide[e],NumeroInvalide[e]))
print("Le nombre de numéros d'Orange est ", len(operateurs[0]))
print("Le nombre de numéros d'Expresso est ", len(operateurs[1]))
print("Le nombre de numéros de Free est ", len(operateurs[2]))
print("Le nombre de numéros de Promobile est ", len(operateurs[3]))

