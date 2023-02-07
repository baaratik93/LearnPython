# On considère le clavier
clavier = {2:["A","B","C"], 
           3:["D","E","F"],
           4:["G","H","I"],
           5:["J","K","L"],
           6:["M","N","O"],
           7:["P","Q","R","S"],
           8:["T","U","V"],
           9:["W","X","Y","Z"]}
keybord = {2:["a","b","c"], 
           3:["d","e","f"],
           4:["g","h","i"],
           5:["j","k","l"],
           6:["m","n","o"],
           7:["p","q","r","s"],
           8:["t","u","v"],
           9:["w","x","y","z"]}
chiffres = ["A","B","C","D","E","F","G","H","I","J"]
numbers = ["a","b","c","d","e","f","g","h","i","j"]

def GenerateCode (i,kb,nb):
    coded = ""
    if i == " ":
        coded += "00"
    for k in range(0,len(kb)-1,1):
        indice = k + 2
        if i != " ":
            if i in kb[indice]:
                index=kb[indice].index(i)
                if index != (index+1):
                    coded+=((index+1) * str(indice))
                else:
                    coded+=((index+1) * str(indice)) + str(0)
            elif i in ["'",'.',',',':','?','!','’']:
                coded+=i
                break
            elif i >= '0' and i <= '9':
                coded+=nb[int(i)]
                break
    return coded

def CoderPhrase(phrase):
    coded = ""
    for i in phrase:
        if (i>="A" and i <= "Z"):
            coded += GenerateCode(i,clavier,chiffres)
        elif i>="a" and i<= "z":
            coded += GenerateCode(i,keybord,numbers)
        elif i >= '0' and i <='9' or i in ["'",'.',',',':','?','!','’',' ']:
            coded += GenerateCode(i,keybord,numbers)
    return coded
# - J’ai 17,5 en algo ⇔ 5’244400bh,f0033660025554666
text ="J’ai 17,5 en algo"
print(CoderPhrase(text))