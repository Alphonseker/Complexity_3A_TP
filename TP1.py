import time
import matplotlib.pyplot as plt
import numpy as np
import math

################## TP1 ########################

''' ----- Tours de Hanoi --------------------------------------------------------------------------------------------------------------------------------------'''

# Fonction pour résoudre une tour de Hanoi de n disques
def hanoi(n, A, B, C):
    if (n == 1):
        # print(f"Transférer de {A} à {C}")
        return
    else:
        hanoi(n - 1, A, C, B)
        # print(f"Transférer {n} de {A} à {C}")
        hanoi(n - 1, B, A, C)

# Fonction pour tracer le graphique de l'ex 1
def plot_temps(temps, n):
    N = list(range(1, n+1)) 
    plt.plot(N, temps, marker='o', color='b', linestyle='-')
    plt.title(f'Temps d\'exécution des tours de Hanoï pour n allant de 1 à {n}')
    plt.xlabel('Nombre de disques (n)')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.grid(True)
    plt.show()

def TP1_Ex1():
    Temps=[]
    n = int(input("Entrez un nombre entier : "))


    for i in range(1,n+1,1):
        # Mesure du temps de début
        start_time = time.time()

        # Résolution des tours de Hanoï
        hanoi(i, 'A', 'B', 'C')

        # Mesure du temps de fin
        end_time = time.time()

        # Calcul du temps écoulé en secondes
        Temps.append(end_time - start_time)

        # Afficher le temps d'exécution
        print(f"Temps d'exécution pour {i} disques : {Temps[i-1]:.10f} secondes") #On affiche 10 chiffres significatifs

    plot_temps(Temps, n) #Affiche le graphique du temps d'exécution en fonction du nombre de disques

''' ----- Fibonacci --------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Fonction qui exécute la presque suite de fibonacci en récursif
def presque_fibo_recursif(n):
    if((n == 0) or (n == 1)):
        return(1)
    else:
        return(presque_fibo_recursif(n-1) + presque_fibo_recursif(n-2))

#Fonction qui exécute la presque suite de fibonacci en itértif
def presque_fibo_itératif(n):
    if n<0 :
        return("erreur")

    #intialisation de la suite
    if (n==1) or (n==0):
        return(1)

    #terme général de la suite
    else :
        (u, u_1, u_2) = (0,1,1)
        for i in range(n-1):
            u = u_1+u_2
            (u_1, u_2) = (u, u_1)
        return(u)

# effectue le produit matricile entre 2 matrice de taille 2*2
def produit_2x2(MA,MB):
    a,b,c,d = MA[0],MA[1],MA[2],MA[3]
    e,f,g,h = MB[0],MB[1],MB[2],MB[3]

    M = [a*e + b*g,
         a*f + b*h,
         c*e + d*g,
         c*f + d*h]
    return(M)

# fonction d'exponentiation rapide matricielle
def power_2x2(M,n):
    if n==1:
        return(M)
    elif n%2==0:
        return(power_2x2(produit_2x2(M,M), n/2))
    else:
        return(produit_2x2(M,power_2x2(produit_2x2(M,M),(n-1)/2)))

# [1 1]^n       [F_n+1   F_n  ]
# [1 0]     =   [F_n     F_n-1]
def presque_fibo_log(n):
    M=[1,1,1,0]
    K=power_2x2(M,n)
    return(K[0])

# Affichage du graphique
def plot_temps2(temps,n):
    N = list(range(1, n+1))
    print(f"{len(N)} ---- {len(temps)}")
    plt.plot(N, temps, marker='o', color='b')
    plt.title('Temps d\'exécution de presque fibo')
    plt.xlabel('Valeur de n/10000')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.grid(True)
    plt.show()


# Fonctions de traçage des exécutions des trois versions de la siute de Fibonacci, en fonction du temps
def TP1_Ex2_1(n):
    Temps=[]
    pas = int(n/100)
    for i in range(1,n+1,pas):
        # Mesure du temps de début
        start_time = time.time()

        # Résolution des tours de Hanoï
        # print(f"{presque_fibo_itératif(i)}")
        presque_fibo_itératif(i)
        print(i)
        # Mesure du temps de fin
        end_time = time.time()

        # Calcul du temps écoulé en secondes
        Temps.append(end_time - start_time)

        # Afficher le temps d'exécution
        # print(f"Temps d'exécution pour la suite {i} est de : {Temps[(int(i/pas)-1)]:.10f} secondes") #On affiche 10 chiffres significatifs
    
    plot_temps2(Temps,int(n/pas)) #Affiche le graphique du temps d'exécution en fonction de n

def TP1_Ex2_2(n):
    Temps=[]
    # pas = int(n/100)
    for i in range(1,n+1,1):
        # Mesure du temps de début
        start_time = time.time()

        # Résolution des tours de Hanoï
        # print(f"{presque_fibo_recursif(i)}")
        presque_fibo_recursif(i)
        print(i)
        # Mesure du temps de fin
        end_time = time.time()

        # Calcul du temps écoulé en secondes
        Temps.append(end_time - start_time)

        # Afficher le temps d'exécution
        #print(f"Temps d'exécution pour la suite {i} est de : {Temps[(int(i/pas)-1)]:.10f} secondes") #On affiche 10 chiffres significatifs

    plot_temps2(Temps,n) #Affiche le graphique du temps d'exécution en fonction de n

def TP1_Ex2_3(n):
    Temps=[]
    pas = int(n/100)
    for i in range(1,n+1,pas):
        # Mesure du temps de début
        start_time = time.time()

        # Résolution des tours de Hanoï
        # print(f"{presque_fibo_log(n)}")
        presque_fibo_log(n)
        print(i)
        # Mesure du temps de fin
        end_time = time.time()

        # Calcul du temps écoulé en secondes
        Temps.append(end_time - start_time)

        # Afficher le temps d'exécution
        # print(f"Temps d'exécution pour la suite {i} est de : {Temps[(int(i/pas)-1)]:.10f} secondes") #On affiche 10 chiffres significatifs

    plot_temps2(Temps,int(n/pas)) #Affiche le graphique du temps d'exécution en fonction de n 

def TP1_Ex2():
    valid = False
    while(valid==False):
        print("Veuillez choisir la version d'exécution de la suite de Fibonacci en entrant l'un des chiffres suivant:")
        print("1:   Version itérative")
        print("2:   Version récursive")
        print("3:   Version logarithmique")
        print("4:   Annuler")
        choix = int(input("Entrez un chiffre :"))
        n = int(input("Entrez un nombre entier, pour la suite de Fibonacci: "))

        if choix==1:
            TP1_Ex2_1(n)
            valid = True
        if choix==2:
            TP1_Ex2_2(n)
            valid = True
        if choix==3:
            TP1_Ex2_3(n)
            valid = True
        if choix==4:
            valid = True


''' ----- Eratosthène -----------------------------------------------------------------------------------------------------------------------------------------------'''

def Eratosthène(n):
    # On constitue notre liste, 0=non_criblé, 1=criblé
    # dans le programme, L[i] représente l'entier i, l'entier 0 sera supprimé à la fin.
    L=[]
    for i in range(n+1):
        L.append(0)
    # On crible 0 et 1
    L[0],L[1]=1,1
    
    # On parcourt la liste et on crible
    for i in range(range(2, int(math.sqrt(n)) + 1)):

        # si l'entier i n'est pas criblé 
        if (L[i]==0):
           
           # on regarde si l'entier i divise un entier j entre i+1 et N
            for j in range (i+1, n+1):
                if (j%i==0):
                    L[j]=1
    del L[0]
    return(L)

def affichage_Eratosthène(n, nombre_element_par_lignes):

    print("Les 0 sont les nombres premiers")
    M=Eratosthène(n)
    for i in range(n):
        print("(",i+1,":",M[i],") ", end="")
        if ((i+1) % nombre_element_par_lignes==0) :
            print("")

def TP1_Ex3():
    n = int(input("Entrez un nombre entier, pour la résolution du crible d'Eratosthène: "))
    nombre_element_par_lignes = int(input("Entrez un nombre entier, pour le nombre d'éléments que vous voulez voir affiché par ligne: "))
    affichage_Eratosthène(n, nombre_element_par_lignes)

''' ----- Programme principal ----- '''

def programme_principal():
    valid = False
    while(valid == False):
        print("1: Exercice 1 (Hanoi)")
        print("2: Exercice 2 (Presque Fibonacci)")
        print("3: Exercice 3 (Crible d'Eratosthène)")
        print("4: Quitter")
        choix = int(input("Entrez votre choix: "))

        if choix == 1:
            TP1_Ex1()
            valid = True
        elif choix == 2:
            TP1_Ex2()
            valid = True
        elif choix == 3:
            TP1_Ex3()
            valid = True
        elif choix == 4:
            valid = True

##########################
programme_principal()  ###
##########################