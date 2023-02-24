nom_etas = ('toto','tata')

def créesScelette(nb_etas,nom_etas):
    automate = [[]]
    for i in range(nb_etas):
        automate[0].append(nom_etas)
    print(automate)
    return automate
    
créesScelette(2,nom_etas)