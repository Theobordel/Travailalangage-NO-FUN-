import random

def affiche_tableau(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            print(tableau[i][j], end=" ")
        print()

def calcul_score(tableau):
    score = 0
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] == "X":
                score = 0
            if tableau[i][j] == "O":
                score = 0
    return score



with open('automate.txt') as f:
    lines = f.readlines()


def stockage():
    n=0
    tableau = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(" ")
        tableau.append(ligne)
    return tableau


f.close


