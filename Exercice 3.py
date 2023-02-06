'''
Écrire un programme qui permet de saisir une chaîne de N phrases. Le programme enlève
tous les espaces inutiles de chaque phrase puis réaffiche les phrases corrigées
Règles de Gestion
● La chaîne de saisie est Obligatoire
● Les phrases ne doivent pas contenir des caractères spéciaux
● Une phrase commence par une lettre majuscule et se termine par un point (. ou ?ou !)
● Chaque phrase contiendra au moins 25 caractères
'''
minuscule = "abcdefghijklmnopqrstuvwxyz"
majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allowed = ".,:;' "
end = '.!?'
def PhraseCorrect(ph):
    if ph[0] in majuscule and ph[len(ph)-1] in end:
        return True
    else:
        return False
def EstDansLaLimite(ph):
    if len(ph) > 25:
        return False
    else:
        return True

def Special(ph):
    trouve = False
    for i in ph:
        # if not ((ord(i) >= 65 and ord(i) <=90) or (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32 or ord(i) == 39):
        if not (i in majuscule or i in minuscule or i in allowed or i in end):
            trouve = True
            break
    return trouve

def EspaceInutile(phrase):
    phrase1 = ""
    i=0
    x=0
    taille = len(phrase)
    for i in range(0, taille):
        if i==0 and phrase[i] == ' ':
            continue
        if i+1 == taille:
            phrase1 = phrase1 + phrase[i]
            continue
        if phrase[i] == phrase[i + 1] == " ":
            x = x + 1
            if x > 2:
                continue
        else:
            phrase1 = phrase1 + phrase[i]
    return phrase1


b = []
b1 = []


def principale():
    tmp=""
    print("Entrer le texte")
    phrases = input()
    if phrases == '' or not PhraseCorrect(phrases) or phrases[len(phrases)-1] not in end:
        principale()
    else:
        for i in phrases:
                tmp = tmp + i
                if i in end:
                    b.append(tmp)
                    tmp=""
        
    
principale()

for i in b:
    b1.append(EspaceInutile(i))
for k in b1:
    if not PhraseCorrect(k):
        print("La phrase << {} >> est incorrect".format(k))
    else:
        print("La phrase << {} >> est correct".format(k))
        if not Special(k):
            print("La phrase << {} >> ne contient pas de caractères spéciaux".format(k))
            if EstDansLaLimite(k):
                print("La phrase << {} >> a la taille normale".format(k))
            else:
                print("La phrase << {} >> est supérieur à 25".format(k))
        else:
            print("La phrase << {} >> contient de caractères spéciaux".format(k))

    

# print(Special("Bonjour?"))
