class automate:

    def __init__(self):
        self.states = []
        self.transitions = {}
        self.init = []
        self.finals = []
        self.alphabet = []


    def add_letre(self,lettre):
        if lettre in self.alphabet:
            print("error : lettre '" + lettre + "' already exists.")
            return
        self.alphabet.append(lettre)

    def add_init(self,states):
        if states in self.states:
            if states in self.init:
                print("error : etas deja inicial")
                return
            else :
                self.init.append(states)
        else :
            print("error : state do not exist")
            


    def add_state(self, state, final = False):
        if state in self.states:
            print("error : state '" + state + "' already exists.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)
        return



    def valid_symbol(self, symbol):
        if symbol not in self.alphabet: return False
        return True
    
    def dst_state(self, src_state, symbol):
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        for (s, dst_state) in self.transitions[src_state]:
            if s == symbol:
                return dst_state
        return None
    
    def add_transition(self, src_state, symbol, dst_state):
        if not self.valid_symbol(symbol):
            print("error : the symbol '",symbol,"' is not part of the alphabet.")
            return
        if src_state not in self.states:
            print("error : the state '",src_state,"' is not an existing state.")
            return
        if dst_state not in self.states:
            print("error : the state '",dst_state,"' is not an existing state.")
            return
        self.transitions[src_state].append((symbol, dst_state))

    def __str__(self):
        print("-----------------------------")
        print(self.states)
        print(self.alphabet)
        print(self.finals)
        print(self.init)
        for i in self.transitions:
            print(i,"-->", self.transitions[i])
        return "-----------------------------------"
    def cree_etas_poubelle(self,nom_poubelle):
        self.add_state(nom_poubelle,False)
        for i in self.alphabet:
            self.add_transition(nom_poubelle,i,nom_poubelle)

    def completer_automate(self,nom_poubelle):
        self.cree_etas_poubelle(nom_poubelle)
        for etas in self.transitions:
            for lettre in range(len(self.alphabet)):
                trouvee = 0
                for p in range(len(self.transitions[etas])):
                    if self.alphabet[lettre] == self.transitions[etas][p][0]:
                        trouvee = 1
                
                if trouvee == 0:
                    self.add_transition(etas,self.alphabet[lettre],nom_poubelle)

    def est_deterministe1(self):
        if self.init != None:
            if len(self.init) != 1:
                return False
        return True

    def est_deterministe2(self):
        for etas in self.states:  
            vue = []
            for lettre in range(len(self.transitions[etas])):
                if self.transitions[etas][lettre][0] in vue:
                    return False
                else:
                    vue.append(self.transitions[etas][lettre][0])
     
        return True
        
    def cree_etas_multiple(self,etas): #etas liste
        print(etas)
        nom = ""
        new_trensi = []
        for i in etas:
            nom = nom + i + ","
            for p in range(len(self.transitions[i])):
                if self.transitions[i][p] not in new_trensi : 
                    new_trensi.append(self.transitions[i][p])
        nom = nom.rstrip(nom[1])
        self.add_state(nom)
        self.transitions[nom].append(new_trensi)
            


    def determinisation(self):
        print("deter")
        initial = ""
        if self.est_deterministe1():
            print("super")
            return
        else:
            for i in self.init:
                print(i)
                initial = initial + i
                #self.states.remove(i) #a verifier sur quand les remouve et si il le faut tout cour
            self.add_state(initial,False)
            #fusioner les transition a partir des etas initiaux
            #suprimer les etas intiaux (entien)
            #ajouter le nouvelle etas initial

            #pour toute trensition duplicative d'un meme etas, crée un nouvelle etas de c'est deux trensition
            

    def sauvegarde_ext(self,chose,fichier):
        for i in range(len(chose)):
            if i != len(chose)-1:
                fichier.write(chose[i]+",")
            else:
                fichier.write(chose[i]+"}\n")

    
    def sauvegarde(self,nom_fichier):
        with open(nom_fichier, mode="w") as f:
            f.write("Q = {")
            self.sauvegarde_ext(self.states,f)
            f.write("Epsilon = {")
            self.sauvegarde_ext(self.alphabet,f)
            f.write("F = {")
            self.sauvegarde_ext(self.finals,f)
            f.write("q0 ={")
            self.sauvegarde_ext(self.init,f)
            for etas in self.states:  
                for i in range(len(self.transitions[etas])):
                    f.write("delta("+etas+","+str(self.transitions[etas][i][0])+") = "+str(self.transitions[etas][i][1])+"\n")

    def to_dot(self):
        dot = graphviz.Digraph()
        dot.attr(rankdir="LR")
        for i in range(len(self.states)):
            etas = self.states[i]
            dot.node(etas , shape="circle")
        for i in range(len(self.states)):
            for j in range(len(self.transitions[etas])):
                dot.edge(etas, self.transitions[etas][j][1] , label=self.transitions[etas][j][0])
        print(dot.source)


    def accepte_mot(self,mot):
        etas = self.init[0]
        prochinetas = etas
        for lettre in mot:
            for lettretren in range(len(self.transitions[etas])):
                if lettre == self.transitions[etas][lettretren][0]:
                    prochinetas = self.transitions[etas][lettretren][1]
            etas = prochinetas
        for i in self.finals:
            if etas == i:
                return True
        return False
                



def run(automate, word):
    current_state = automate.init

    for symbol in word:
        next_state = automate.dst_state(current_state, symbol)
        if next_state is None:
            return False

        current_state = next_state
        i = i+1

    if current_state in automate.finals:
        return True
    return False


