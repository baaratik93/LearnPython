from fn.control import CustomSplit
def ShowOperator(name,o):
    tmp = len(o) * "| {:15}"
    print(len(o[0])*len(o)*3*'-')
    print(name,tmp.format(*o))


def OperatorConstructTable():
    return CustomSplit(input("Entrer une liste d'opérateurs séparés par un tiret(-): "),"-")
    
    