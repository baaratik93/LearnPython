#PYTHON CUSTOM FUNCTIONS
def CustomSplit(ch,sep):
    if ch[-1]==sep:
        pass
    else:
        ch+=sep
    ligne=""
    std = []
    for i in ch:
        if i != sep:
            ligne+=i
        else:
            std.append(ligne)
            ligne=""
            continue
    return std

def CustomLength(list):
    k = 0
    for i in list:
        k+=1
    return k

def CustomAppend(list,el):
    el = [el]
    list+=el
    return list

def CustomSort(e,sens):
        for i in range(0,CustomLength(e)):
            for j in range(i+1,CustomLength(e)):
                if sens=="asc":
                    if e[i]["moy"] > e[i+1]["moy"]:
                        e[i],e[j]=e[j],e[i]
                    else:
                        if e[i]["moy"] < e[i+1]["moy"]:
                            e[i],e[j]=e[j],e[i]
        return e

#Supprimer les èspaces entre les chiffres
def DelSpace(ch):
    num_tmp=""
    for k in ch:
        if k != " ":
            num_tmp+=k
    return num_tmp

def IsNumber(ch):
    num = DelSpace(ch)
    for c in num:
        trouve=True
        if c <'0' or c > '9':
            trouve = False
            return trouve
        else:
            trouve=True
    return trouve

#Vérifier la longueur du numéro
def IsCorrect(ch):
    num = DelSpace(ch)
    if IsNumber(num):
        if CustomLength(num) == 9:
            if num[0]+num[1] in ['77','78','76','70','75']:
                return num
            else:
                return False
        else:
            return False
    else:
        return False
    
def IsExistClient(list,number):
    t = False
    for k in list:
        if k["telephone"]==number:
            t = True
            break
    return t




