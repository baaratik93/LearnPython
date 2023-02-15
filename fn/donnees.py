def students():
    return [
        {
            "prenom": "Mamadou",
            "nom": "Thiam",
            "telephone": 776280909,
            "classe":"L1",
            "dev":12.75,
            "projet":15.45,
            "exam":14.25,
            "moy":0.0
        },
        {
            "prenom": "Fama",
            "nom": "Mbow",
            "telephone": 776549987,
            "classe":"L1",
            "dev":10,
            "projet":10,
            "exam":10,
            "moy":0.0
        },
        {
            "prenom": "Demba",
            "nom": "BA",
            "telephone": 789854432,
            "classe":"L1",
            "dev":10,
            "projet":10,
            "exam":10,
            "moy":0.0
        },
        {
            "prenom": "Oumy",
            "nom": "DIAW",
            "telephone": 769453476,
            "classe":"L1",
            "dev":10,
            "projet":10,
            "exam":10,
            "moy":0.0
        }
    ]
    
def Entete():
        print('+---------------------------------------------------------------------------------------------------------------------------------------+')
        print('|\tPrénom\t|\tNom\t|\tTéléphone\t|\tClasses\t|\tDev\t|\tProj\t|\tExam\t|\tMoyenne\t|')
        print('+---------------------------------------------------------------------------------------------------------------------------------------+')

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
            if sens == "asc":
                if e[i]["moy"] > e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
            else:
                if e[i]["moy"] < e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
    return e



def ShowSingleStudent(etudiant):
        etudiant["moy"] = (etudiant["dev"] + etudiant["projet"] + etudiant["exam"])/3
        print('|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{}\t|\t{:.2f}\t|'
                .format(etudiant["prenom"],etudiant["nom"],
                etudiant["telephone"],etudiant["classe"],
                etudiant["dev"],etudiant["projet"],
                etudiant["exam"],etudiant["moy"]))
        print('+---------------------------------------------------------------------------------------------------------------------------------------+')



def MenuGenerate(list):
    for i in range(CustomLength(list)):
        print('\t\t\t\t+-----------------------------------------------+')
        print('\t\t\t\t|       {} - {}\t\t\t+'.format(i+1,list[i]))
        if i == CustomLength(list)-1:
         print('\t\t\t\t+-----------------------------------------------+')


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
    
def StudentsToFile(list):
    f = open("students.txt", "w")
    for k in list:
        f.write("{}-{}-{}-{}-{}-{}-{}#".format(k["nom"],k["prenom"],k["telephone"],k["classe"],k["dev"],k["projet"],k["exam"])) 
    f.close()
    
def FileToStudent():
    f = open("students.txt", "r")
    ch = f.read()

    std = CustomSplit(ch,"#")
    lstd = []

    for j in std:
        et = CustomSplit(j,"-")
        lstd.append({
            "nom": et[0],
            "prenom": et[1],
            "telephone": int(et[2]),
            "classe": et[3],
            "dev": float(et[4]),
            "projet": float(et[5]),
            "exam": float(et[6]),
            "moy": 0.0
        })
    return lstd

def IsStudent(list,number):
    t = False
    for k in list:
        if k["telephone"]==number:
            t = True
            break
    return t