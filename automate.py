class Automate:
    #Cette classe représente toutes les méthodes de l'automate déterministe
    def __init__(moi, alphabet):
        #initialise l'automate
        moi.etats = []
        #initialise la liste des états
        moi.transitions = {}
        #initialise la liste des transitions
        moi.init = None
        #initialise la liste des états initiaux
        moi.finals = []
        #initialise la liste des états finaux
        moi.alphabet = ""
        #initialise l'alphabet
        for s in alphabet:
            if s not in moi.alphabet:
                moi.alphabet += s
        

    def add_state(moi, etat, final = False):
        #ajoute un état à la liste des états
        #si un état est déjà dans la liste des états, on ne l'ajoute pas
        if etat in moi.etats:
            print("erreur : l'etat " + etat + "n'existe pas.")
            return
        moi.transitions[etat] = []
        moi.etats.append(etat)
        if final:
            moi.finals.append(etat)



    def valid_symbol(moi, symbol):
        #vérifie si le symbole est dans l'alphabet
        if symbol not in moi.alphabet: return False
        return True
    
    def dst_etat(moi, src_etat, symbol):
        #cherche la transition correspondant à l'état source et le symbole et retourne 
        # l'état destination. Si la transition n'existe pas, la fonction retourne None
        #src_state : l'état source
        #symbol : le symbole à transmettre
        if src_etat not in moi.etats:
            print("erreur : l'etat " + src_etat + " n'existe pas.")
            return
        for (s, dst_etat) in moi.transitions[src_etat]:
            if s == symbol:
                return dst_etat
        return None
    
    def add_transition(moi, src_etat, symbol, dst_etat):
        #ajoute une transition entre l'état source et le symbole et l'état destination
        #ds_state : l'état destination
        if not moi.valid_symbol(symbol):
            print("erreur : le symbole " + symbol + " n'existe pas dan sl'alphabet.")
            return
        if src_etat not in moi.etats:
            print("erreur : l'état " + src_etat + " n'existe pas.")
            return
        if dst_etat not in moi.etats:
            print("erreur : l'état" + dst_etat + " n'existe pas.")
            return
    
        if moi.dst_etat(src_etat, symbol) != None:
            print("erreur : la transition (" + src_etat + ", " + symbol + ", ...) existe déjà.")
            return
    
        moi.transitions[src_etat].append((symbol, dst_etat))

    def __str__(moi):
        #retourne une chaîne de caractères représentant l'automate
        ret = "FA :\n"
        ret += "   - alphabet   : " + moi.alphabet + "\n"
        ret += "   - init       : " + str(moi.init) + "\n"
        ret += "   - finals     : " + str(moi.finals) + "\n"
        ret += "   - etats (%d) :\n" % (len(moi.etats))
        for state in moi.etats:
            ret += "       - (%s)" % (state)
            if len(moi.transitions[state]) == 0:
                ret += ".\n"
            else:
                ret += ret + ":\n"
                for (symbol, destination) in moi.transitions[state]:
                    ret += ret + "          --(%s)--> (%s)\n" % (symbol, destination)
        return ret
    



def run(automate, mot):
    Automate.alphabet = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        #fonction qui permet de tester l'automate sur une phrase donnée
    etat_courant = automate.init
    #initialise l'état courant à l'état initiaux
    for symbol in mot:
        #pour chaque symbole de la phrase, on cherche la transition correspondante et l'état courant
        etat_suivant = automate.dst_etat(etat_courant, symbol)
        #si la transition n'existe pas, la fonction retourne False
        if etat_suivant == None:
            return False
        etat_courant = etat_suivant
        i = i+1
    #si l'état courant est un état final, la fonction retourne True
    if etat_courant in automate.finals:
        return True
    return False


def enregistrer(automate, fichier):
    #fonction qui enregistre l'automate dans un fichier texte
    fichier = open(fichier, "w")
    fichier.write(str(automate))
    fichier.close()


    def lire(fichier):
        #fonction qui lit un fichier texte et retourne l'automate correspondant
        var_locale = locals()
        with open(fichier, "r") as file:
            exec(compile(open(fichier).read(), fichier, 'exec'), globals(), var_locale)
        return var_locale["a"]
    
