# Écrire un programme qui, à partir d’une phrase, affiche son équivalent codé
# Règles de codage de la phrase :
# On considère le clavier avec les anciens téléphones avec touches.
# - Pour Écrire la lettre A : il faut appuyer une fois sur la touche 2
# - Pour Écrire la lettre B : il faut appuyer deux fois sur la touche 2
# - Pour écrire la lettre S : il faut appuyer trois fois sur la touche 7.
# Dans le programme on a les règles suivantes :
# - Pour écrire des chiffres, on écrit des lettres et les lettres deviennent des chiffres :
# - Pour écrire le chiffre ZÉRO (0), on écrit : A,
# - Le chiffre UN (1) devient la lettre B, ainsi de suite jusqu’au chiffre NEUF (9) qui
# devient la lettre J.
# - Le caractère ESPACE est représenté par DEUX ZÉROS (00).
# - Les autres caractères ne sont pas changés.
# - Si des lettres partageant le même chiffre se succèdent, alors il faut les séparer par le
# chiffre ZÉRO (0)
# - Exemples :
# - Bonjour aly ⇔ 22666066566688777002555999
# - J’ai 17,5 en algo ⇔ 5’244400bh,f0033660025554666

clavier = {2:["A","B","C"], 3:["D","E","F"], 4:["G","H","I"],5:["J","K","L"],6:["M","N","O"],7:["P","Q","R","S"],8:["T","U","V"],9:["W","X","Y","Z"]}
print(clavier)

choix = input()
i = int(choix[0])
print(clavier[i][len(choix)-1])

