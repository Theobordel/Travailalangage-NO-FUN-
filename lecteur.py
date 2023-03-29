import model


try :
    fichier = open('test.txt','r')
except :
    print("fichier nas pas pus etres")
    exit()

Q = []
alphabet = []
F = []
Qo =[]
info = [Q,alphabet,F,Qo]

#l = f.readline()#

def lecteurExt1(ligne,tablaux):
    p = len(ligne) 
    i = 0
    tablaux = []
    caractaire = ""
    try:
        while ligne[i] != "{":

            i = i+1
        while p > i:

            i= i+1
            if ligne[i] == "}":
                break
            if ligne[i]== ",":
                tablaux.append(caractaire)
                caractaire =""
            else:
                caractaire = caractaire + ligne[i]
        if caractaire == "":
            print("ereur dans le format ou un champ manquant")
            exit()
        tablaux.append(caractaire)    
        return tablaux
    except:
        print("ereur dans le format")
        exit()
    

def lecteurExt(tablaux):
    for i in range(4) :
        linge = fichier.readline()
        info[i] = lecteurExt1(linge,tablaux)

    return info



def aujoutautomate(tablaux,automate):
    for i in tablaux[2]:
        automate.add_state(i,True)
    for i in tablaux[0]:
        automate.add_state(i,False)
    for i in tablaux[1]:
        automate.add_letre(i)
def aujoutetas_ext(ligne,tablaux):
    p = len(ligne) 

    i = 0
    tablaux = []
    caractaire = ""
    try:
        while ligne[i] != "(":
            i = i+1
        while p-1 > i:
            i= i+1
            if ligne[i]== "," or ligne[i]==")":
                tablaux.append(caractaire)
                caractaire =""
            elif ligne[i]!= " " and ligne[i]!="=" and ligne[i]!="\n":
                caractaire = caractaire + ligne[i]
            elif ligne[i] == "\0":
                break
        if caractaire == "":
            print("ereur dans le format ou un champ manquant")
            exit()
        tablaux.append(caractaire)    
        return tablaux
    except:
        print("ereur dans le format")
        exit()
  

def aujoutrensition(automate):
    tablaux = []
    ligne = fichier.readline()
    while ligne != "":
        tablaux = aujoutetas_ext(ligne,tablaux)
        automate.add_transition(tablaux[0],tablaux[1],tablaux[2])
        tablaux = []
        ligne = fichier.readline()
    

    
#print(l) 
#print(content)
info = lecteurExt(info)
print(info)
automate1 = model.automate()
aujoutautomate(info,automate1)
aujoutrensition(automate1)
print(automate1.transitions)
print("toto")
##print(automate1)
print("tata")