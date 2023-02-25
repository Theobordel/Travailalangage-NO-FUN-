f = open('test.txt','r')

Q = []
alphabet = []
F = []
info = (Q,alphabet,F)

l = f.readline()


def lecteur1(ligne,tablaux):
    i =0
    while ligne[i] != "{":
        i = i+1
    i= i+1
    while ligne[i] != "}":
        if ligne[i] != ",":
            tablaux.append(ligne[i])
        i=i+1
#print(l) 
#print(content)
print(etas)
