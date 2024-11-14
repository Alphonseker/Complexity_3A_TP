import matplotlib.pyplot as plt
import time
import random as rd

### Question 1 ---------------------------------------------------------------------------------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------------------------
def CopieListe(L):
# PREND    : liste L
# RETOURNE : une copie de la liste L, indépendante de l'originale.
    COPIE = []
    for i in range(len(L)):
        COPIE.append(L[i])
    return(COPIE)

def Q1_ConstruireCouple(P):
# PREND    : liste P = Pn avec len(P)>=2
# RETOURNE : liste(liste(C[0],C[1],a,b..)) FINAL = liste de tous les (couples + reste des éléments)
    p = len(P)
    INDICES=[]
    FINAL=[]

    # on récupère les indices de tous les couples possibles
    for i1 in range (0, p):
        for i2 in range (i1+1, p):
            INDICES.append( (i1, i2) )
    
    # on met le couple en début de la liste P, et on ajoute cette liste modifiée à FINAL
    for i in range (len(INDICES)):
        TEMP = CopieListe(P)
        TEMP[0], TEMP[INDICES[i][0]] = TEMP[INDICES[i][0]], TEMP[0]
        TEMP[1], TEMP[INDICES[i][1]] = TEMP[INDICES[i][1]], TEMP[1]
        FINAL.append(TEMP)

    return(FINAL)



### Question 2 ---------------------------------------------------------------------------------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------------------------

def f(a,b,C,s):
# PREND    : int a = indice 1 ; int b = indice 2, couple C ; char s = symbole de l'opération
# RETOURNE : char, (C[a] + C[b])

    return( "("+str(C[a]) + s + str(C[b])+")" )

def Q2_CalculsCouple(C):
# PREND    : couple C
# RETOURNE : liste(couple(entier,char)) FINAL = [(somme,"a+b"),(produit,"a*b"),...]
    FINAL=[]

    # addition
    t = C[0] + C[1]
    FINAL.append( (t, f(0,1,C,"+")) )

    # multiplication
    t = C[0] * C[1]
    FINAL.append( (t, f(0,1,C,"*")) )

    # soustraction : on garde le résultat positif
    t = C[0] - C[1]
    if t>0 :
        FINAL.append( (t, f(0,1,C,"-")) )
    else :
        FINAL.append( (-t, f(1,0,C,"-")) )
    
    # division : le résultat doit être entier, 2 cas à considérer,on évite le doublon si C[0]=C[1]
    if (C[0] != 0) and (C[1] % C[0] == 0) :
        t = C[1] // C[0]
        FINAL.append( (t, f(1,0,C,"/")) )

    if (C[1] != 0) and (C[0] % C[1] == 0) and (C[0] != C[1]) :
        t = C[0] // C[1]
        FINAL.append( (t, f(0,1,C,"/")) )

    return(FINAL)
    
def Q2_constructionPn(P):
# PREND    : liste P = Pn
# RETOURNE : liste(couple(liste,char)) FINAL = [(Pn-1,calcul pour obtenir Pn-1),(Pn-1,calcul pour obtenir Pn-1)...]
    FINAL=[]
    L = Q1_ConstruireCouple(P)
    l = len(L)

    for i in range(l):
        C = L[i][0],L[i][1]
        M = Q2_CalculsCouple(C)
        m = len(M)

        for j in range(m):
            # M = [(somme,"a+b"),(produit,"a*b"),...]
            # L[i][:2] est Pn auquel on a enlevé le couple d'élément
            TEMP = ([M[j][0]] + L [i][2:] , M[j][1])
            FINAL.append(TEMP)

    return(FINAL)



### Question 3 ---------------------------------------------------------------------------------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------------------------

def Q3_ResultatAtteignable(P,R):
# PREND    : liste P = la liste d'origine ; entier R = résulat à atteindre
# RETOURNE : char calculs = tous les calculs effectués

 # Cas particulier
    if R in P :
        return("R est déjà dans la liste")

 # Initialisation
    # on creer nos fichier text de stockage
    Stockage_Pn = open("Complexite_TP3_Stockage1.txt", "w")
    Stockage_Pn_1 = open("Complexite_TP3_Stockage2.txt", "w")

    # on ajoute P au bon format dans Stockage1.txt
    Stockage_Pn.write(str((P,""))+"\n")
    Stockage_Pn.write("end")
    
    # on ferme nos fichier
    Stockage_Pn.close()
    Stockage_Pn_1.close()
    

 # Algorithme
    # on veut s'arrêter quand les Pn sont de tailles 1. on effectue donc N-1 fois l'algorithme
    N = len (P)
    for i in range (1,N):
        # on ouvre les fichiers
        if (i%2==0) :
            Stockage_Pn = open("Complexite_TP3_Stockage2.txt", "r")
            Stockage_Pn_1 = open("Complexite_TP3_Stockage1.txt", "w")
        else :
            Stockage_Pn = open("Complexite_TP3_Stockage1.txt", "r")
            Stockage_Pn_1 = open("Complexite_TP3_Stockage2.txt", "w")

        # on lit Stockage_Pn ligne par ligne
        ligne_texte = Stockage_Pn.readline()
        while ligne_texte != "end" :
            ligne_eval = eval(ligne_texte) # = couple(Liste = Pn, char = calculs)
            ligne_texte = Stockage_Pn.readline()

            # On profite de la lecture pour tester si R est trouvé
            if R in ligne_eval[0]:
                return(ligne_eval[1])
            
            # On construit et stock les Pn-1 dans le deuxième fichier text
            Constr_Pn_ligne = Q2_constructionPn(ligne_eval[0]) # = liste(couple(liste,char))
            a = len(Constr_Pn_ligne)
            # On met à jour la chaine de caractère des différentes opérations effectuées
            for j in range(a):
                couple_temp = (Constr_Pn_ligne[j][0], ligne_eval[1] + Constr_Pn_ligne[j][1])
                Stockage_Pn_1.write(str(couple_temp)+"\n")

        Stockage_Pn.close()
        Stockage_Pn_1.write("end")
        Stockage_Pn_1.close()

 # Vérification finale pour savoir si R est dans les P1
    # on ouvre Stockage_Pn_1 en mode lecture
    if (i%2==0) :
        Stockage_Pn_1 = open("Complexite_TP3_Stockage1.txt", "r")
    else :
        Stockage_Pn_1 = open("Complexite_TP3_Stockage2.txt", "r")

    # on parcourt les P1 à la recherche de R
    ligne_texte = Stockage_Pn_1.readline()
    while ligne_texte != "end" :
        ligne_eval = eval(ligne_texte)
        ligne_texte = Stockage_Pn_1.readline()
        if ligne_eval[0][0] == R :
            return(ligne_eval[1])
    
    Stockage_Pn_1.close()

    # si R n'est pas trouvé à cette dernière étape alors
    return("R ne peut pas être atteint")



### Question 5 ---------------------------------------------------------------------------------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------------------------

def Q5_CreerPlaque():
# RETOURNE : liste L = les plaques à utiliser
    L=[]
    for i in range(1, 11):
        L.append(i)
        L.append(i)
    for i in range (1,5):
        L.append(i*25)
        L.append(i*25)
    return(L)

def Q5_Plaques_R():
    INDICES = []
    P = []
    L = Q5_CreerPlaque()
    l = len(L)

    
    while len(INDICES)<6 :
        a = rd.randint(0,l-1)
        if a not in INDICES :
            INDICES.append(a)
            P.append(L[a])
    
    R = rd.randint(100,999)
    
    return(P,R)



### Tests --------------------------------------------------------------------------------------------------------------------------------------
### --------------------------------------------------------------------------------------------------------------------------------------------

#Listes utilisées pour tracer le graphique
X=[]
Y=[]
n = 1000

for i in range(n) :
    P,R = Q5_Plaques_R()
    
    timer = time.process_time()
    TEMP = Q3_ResultatAtteignable(P,R)
    print(i, TEMP)
    timer = (time.process_time() - timer)
    
    X.append(i)
    Y.append(timer)

# Moyenne
print(Y)

somme = 0
for i in range(n):
    somme += Y[i]
moyenne = (somme/n)
print ("\nLa moyenne de temps d'exécution est",moyenne)

# Affichage de la courbe
plt.plot(X,Y)
plt.xlabel("n")
plt.ylabel("temps d'exécution en s")
plt.show()