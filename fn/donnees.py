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


def CustomAppend(list,el):
    el = [el]
    list+=el
    return list

def CustomSort(e,sens):
    if sens=="asc":
        for i in range(0,len(e)):
            for j in range(i+1,len(e)):
                if e[i]["moy"] > e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
        return e
    else:
        for i in range(0,len(e)):
            for j in range(i+1,len(e)):
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
    for i in range(len(list)):
        print('\t\t\t\t+-----------------------------------------------+')
        print('\t\t\t\t|       {} - {}\t\t\t+'.format(i+1,list[i]))
        print('\t\t\t\t+-----------------------------------------------+')