clavier = {2:["A","B","C"], 
           3:["D","E","F"],
           4:["G","H","I"],
           5:["J","K","L"],
           6:["M","N","O"],
           7:["P","Q","R","S"],
           8:["T","U","V"],
           9:["W","X","Y","Z"]}
chiffres = ["A","B","C","D","E","F","G","H","I","J"]

def CoderPhrase(phrase):
    coded = ""
    for i in phrase:
        if i == " ":
            coded += "00"
        for k in range(0,len(clavier)-1,1):
            indice = k + 2
            if i != " ":
                if i in clavier[indice]:
                    index=clavier[indice].index(i)
                    
                    if index != (index+1):
                        coded+=((index+1) * str(indice))
                    else:
                        coded+=((index+1) * str(indice)) + str(0)
                elif i in ["'",'.',',',':','?','!']:
                    coded+=i
                    break
                elif i >= '0' and i <= '9':
                    coded+=chiffres[int(i)]
                    break
                else:
                    ""
                    
                     
    return coded

# - J’ai 17,5 en algo ⇔ 5’244400bh,f0033660025554666
text ="J'AI 17,5 EN ALGO"
print(CoderPhrase(text))