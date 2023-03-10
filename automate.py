class automate:

    def __init__(self, alphabet):
        self.states = []
        self.transitions = {}
        self.init = None
        self.finals = []
        self.alphabet = ""
        for s in alphabet:
            if s not in self.alphabet:
                self.alphabet += s


    def add_state(self, state, final = False):
        if state in self.states:
            print("error : state '" + state + "' already exists.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)
        return

    def add_state(self, state, final = False):
        if state in self.states:
            print("error : state '" + state + "' already exists.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)



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
            print("error : the symbol '" + symbol + "' is not part of the alphabet.")
            return
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        if dst_state not in self.states:
            print("error : the state '" + dst_state + "' is not an existing state.")
            return
    
        if self.dst_state(src_state, symbol) != None:
            print("error : the transition (" + src_state + ", " + symbol + ", ...) already exists.")
            return
    
        self.transitions[src_state].append((symbol, dst_state))

    def __str__(self):
        ret = "FA :\n"
        ret += "   - alphabet   : '" + self.alphabet + "'\n"
        ret += "   - init       : " + str(self.init) + "\n"
        ret += "   - finals     : " + str(self.finals) + "\n"
        ret += "   - states (%d) :\n" % (len(self.states))
        for state in self.states:
            ret += "       - (%s)" % (state)
            if len(self.transitions[state]) is 0:
                ret += ".\n"
            else:
                ret += ret + ":\n"
                for (sym, dest) in self.transitions[state]:
                    ret += ret + "          --(%s)--> (%s)\n" % (sym, dest)
        return ret

    def __str__(self):
        ret = "FA :\n"
        ret += "   - alphabet   : '" + self.alphabet + "'\n"
        ret += "   - init       : " + str(self.init) + "\n"
        ret += "   - finals     : " + str(self.finals) + "\n"
        ret += "   - states (%d) :\n" % (len(self.states))
        for state in self.states:
            ret += "       - (%s)" % (state)
            if len(self.transitions[state]) is 0:
                ret += ".\n"
            else:
                ret += ret + ":\n"
                for (sym, dest) in self.transitions[state]:
                    ret += ret + "          --(%s)--> (%s)\n" % (sym, dest)
        return ret
    





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


