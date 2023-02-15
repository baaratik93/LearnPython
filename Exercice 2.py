"""
Écrire un programme qui permet de saisir une phrase. Le programme enlève tous les espaces
inutiles de la phrase.
"""


# phrase = input("Entrer une phrase:")
# phrase1 = ""
# i=0
# x=0
# taille = len(phrase)
# for i in range(0, taille):
#     if i+1 == taille:
#         phrase1 = phrase1 + phrase[i]
#         continue
#     if phrase[i] == phrase[i + 1] == " ":
#         x = x + 1
#         if x > 2:
#             continue
#     else:
#         phrase1 = phrase1 + phrase[i]
# print(phrase1)
def FirstAndLastSignifiantLetter(ch,position):
    start = 0
    stop =0
    step = 0
    s=""
    t=False
    if position == "f":
        start = 0
        stop = len(ch)
        step = 1
    elif position == "l":
        start = len(ch)-1
        stop = 0
        step = -1
    for i in range(start,stop,step):
        if ch[i] != " ":
                        t=True
                        return i
phrase = input("Entrer une phrase:")
phrase1 = ""
for i in range(FirstAndLastSignifiantLetter(phrase,"f"),FirstAndLastSignifiantLetter(phrase,"l")+1):
    if phrase[i] == " " and phrase[i + 1] == " ":
            continue
    else:
        phrase1 = phrase1 + phrase[i]
print(phrase1)
