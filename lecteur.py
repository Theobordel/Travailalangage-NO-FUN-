
try :
    f = open('test.txt','r')
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
        l = f.readline()
        info[i] = lecteurExt1(l,tablaux)

    return info

#print(l) 
#print(content)
print(lecteurExt(info))

