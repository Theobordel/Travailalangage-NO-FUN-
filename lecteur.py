f = open('test.txt','r')

Q = []
alphabet = []
F = []
info = [Q,alphabet,F]

#l = f.readline()#

def lecteurExt1(ligne,tablaux):
    p = len(ligne) 
    i = 0
    tablaux = []
    print(p,i,ligne)
    caractaire = ""
            
    while ligne[i] != "{":
        print(i)
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
            print(caractaire,"toto")
    tablaux.append(caractaire)    
    return tablaux

def lecteurExt(tablaux):
    for i in range(4) :
        l = f.readline()
        info[i] = lecteurExt1(l,tablaux)
    return info

#print(l) 
#print(content)
print(lecteurExt(info))

