import RediCube as rd
import pandas as pd
import time
import multiprocessing
import numpy as np
#import ResolutionClassic
pd.set_option('display.max_columns', 10)



Aretes=pd.read_csv('csv/Aretes.csv',sep=';')
Sommets=pd.read_csv('csv/Sommets.csv',sep=';')

#Nombre correspondant à 5 min de traitement sur ma machine (Owen)
N_sans_elagage=9358
N_elagage1=5452
N_elagage2=3906

'''
#30mins
N_elagage1=82000
N_elagage2=60000
'''

def Cout(r):
    rd_resolu = rd.RediCube()
    res=0
    for index,row in Aretes.iterrows():
        if (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
            res+=1

    for index,row in Sommets.iterrows():
        if (r.cube[row['Face']].tab[row['Ligne']][row['Colonne']] == rd_resolu.cube[row['Face']].tab[row['Ligne']][row['Colonne']]):
            res+=1

    return res

def Cout2(r):
    rd_resolu = rd.RediCube()
    res=0
    for index,row in Aretes.iterrows():
        if (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
            res+=2

    for index,row in Sommets.iterrows():
        if (r.cube[row['Face']].tab[row['Ligne']][row['Colonne']] == rd_resolu.cube[row['Face']].tab[row['Ligne']][row['Colonne']]):
            res+=1

    return res

'''
arretes voisines, si elle est à l'une de ses coordonées
regarder s'il y a un sommet voisin de la même couleur
'''
def Cout3(r):
    rd_resolu = rd.RediCube()
    res=0
    for index,row in Aretes.iterrows():
        #Arete mise
        if (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):

            s1,s2 = SommetsVoisins(row['Ligne1'],row['Colonne1'])
            #Arete mise collée à un sommet
            if (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == r.cube[row['Face1']].tab[s1[0]][s1[1]]) or (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == r.cube[row['Face1']].tab[s2[0]][s2[1]]):

                #Arete mise collée à 2 sommets
                if r.cube[row['Face1']].tab[s1[0]][s1[1]] == r.cube[row['Face1']].tab[s2[0]][s2[1]]:
                    res+=8

                #Arete mise collée à un sommet
                else:
                    res += 6

            #Arete mise
            else:
                res+=5


        else:#Arrete a un coup
            #Arretes voisines
            AretesVoisines=Aretes[(Aretes['hauteur move 1']==row['hauteur move 1']) & (Aretes['numero move 1']==row['numero move 1'])]
            AretesVoisines=AretesVoisines.append(Aretes[(Aretes['hauteur move 2']==row['hauteur move 1']) & (Aretes['numero move 2']==row['numero move 1'])])
            #print(AretesVoisines)

            AretesVoisines=AretesVoisines.append(Aretes[(Aretes['hauteur move 1']==row['hauteur move 2']) & (Aretes['numero move 1']==row['numero move 2'])])
            AretesVoisines=AretesVoisines.append(Aretes[(Aretes['hauteur move 2']==row['hauteur move 2']) & (Aretes['numero move 2']==row['numero move 2'])])

            for index2,row2 in AretesVoisines.iterrows():
                #Arete placée à un coup#
                if (r.cube[row2['Face1']].tab[row2['Ligne1']][row2['Colonne1']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row2['Face2']].tab[row2['Ligne2']][row2['Colonne2']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
                    s1,s2 = SommetsVoisins(row2['Ligne1'],row2['Colonne1'])
                    #Arete collée au sommet
                    if (r.cube[row2['Face1']].tab[s1[0]][s1[1]] == r.cube[row2['Face1']].tab[row2['Ligne1']][row2['Colonne1']]) or (r.cube[row2['Face1']].tab[s2[0]][s2[1]] == r.cube[row2['Face1']].tab[row2['Ligne1']][row2['Colonne1']]):

                        #Arete collé à 2 sommets
                        if r.cube[row['Face1']].tab[s1[0]][s1[1]] == r.cube[row['Face1']].tab[s2[0]][s2[1]]:

                        #Arete et 2 sommet à un coup d'être mis = 2 points
                            res+=4

                        #Arete collée à 1 sommet, à un coup d'être mis
                        else:
                            res+=3

                #Arete placée à un coup#
                elif (r.cube[row2['Face2']].tab[row2['Ligne2']][row2['Colonne2']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row2['Face1']].tab[row2['Ligne1']][row2['Colonne1']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
                    s1,s2 = SommetsVoisins(row2['Ligne1'],row2['Colonne1'])
                    #Arete collée au sommet
                    if (r.cube[row2['Face1']].tab[s1[0]][s1[1]] == r.cube[row2['Face1']].tab[row2['Ligne1']][row2['Colonne1']]) or (r.cube[row2['Face1']].tab[s2[0]][s2[1]] == r.cube[row2['Face1']].tab[row2['Ligne1']][row2['Colonne1']]):

                        #Arete collé à 2 sommets
                        if r.cube[row['Face1']].tab[s1[0]][s1[1]] == r.cube[row['Face1']].tab[s2[0]][s2[1]]:

                        #Arete et 2 sommet à un coup d'être mis = 2 points
                            res+=4

                        #Arete collée à 1 sommet, à un coup d'être mis
                        else:
                            res+=3

    for index,row in Sommets.iterrows():
        if (r.cube[row['Face']].tab[row['Ligne']][row['Colonne']] == rd_resolu.cube[row['Face']].tab[row['Ligne']][row['Colonne']]):

            #Sommet mis = 1 point
            res+=1

    return res

#Retourne les coordonnées des 2 sommets voisins, pour les coordonnées d'une arete
def SommetsVoisins(ligne,colonne):
    if ligne in (0,2):
        s1=(ligne,colonne-1)
        s2=(ligne,colonne+1)

    elif ligne==1:
        s1=(ligne-1,colonne)
        s2=(ligne+1,colonne)

    return s1,s2

##Arbre, parcours en largeur, elagage top n (cout)
def Resolution_Arbre_elagage1(r,n,N=N_elagage1): #1<n<7
    start_time = time.time()
    r.lastcoup=tuple()

    compteur=0
    file=[]
    file.append([r,[],Cout3(r)])
    cube=rd.RediCube().cube


    while Cout3(file[0][0]) != 104 and compteur<N:
        compteur+=1
        node = file.pop(0)
        Ltemp=[]

        for coup in (r.ListCoups()):
            L2=[i for i in node[1]]
            copy_r = node[0].Copy()

            copy_r.Move(coup[0],coup[1],coup[2])
            L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
            #print({'hauteur':hauteur,'num':num,'sens':sens})
            Ltemp.append([copy_r,L2,Cout3(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=Ltemp[:n]
        #print(Ltemp)
        file.extend(Ltemp)

    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    return tf,nb_noeuds,sol


def Resolution_Arbre_elagage1_V2(r,n,N=N_elagage1): #1<n<7
    start_time = time.time()
    r.lastcoup=tuple()

    compteur=0
    file=[]
    file.append([r,[],Cout2(r)])
    cube=rd.RediCube().cube
    All_Redi=[]
    All_Redi.append(r.cube)

    while file[0][0].cube != cube and compteur<N:
        compteur+=1
        node = file.pop(0)
        Ltemp=[]

        for coup in (r.ListCoups()):
            L2=[i for i in node[1]]
            copy_r = node[0].Copy()
            copy_r.Move(coup[0],coup[1],coup[2])
            #print({'hauteur':hauteur,'num':num,'sens':sens})
            if copy_r.cube not in All_Redi:
                All_Redi.append(copy_r.cube)
                L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                Ltemp.append([copy_r,L2,Cout2(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=Ltemp[:n]
        #print(Ltemp)
        file.extend(Ltemp)

    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    return tf,nb_noeuds,sol

def Resolution_Arbre_Rollback(r,n,N=N_elagage1,nbBeforeRollback=3): #1<n<7
    start_time = time.time()
    r.lastcoup=tuple()

    compteur=0
    prof=0
    file=[]
    file.append([r,[],Cout3(r)])
    nextfile=[]
    Arbre={}


    while Cout3(file[0][0]) != 104 and compteur<N:
        print(Cout3(file[0][0]))
        prof+=1
        print('profondeur = ',str(prof))
        while file:
            compteur+=1
            node = file.pop(0)
            for coup in (r.ListCoups()):
                L2=[i for i in node[1]]
                copy_r = node[0].Copy()

                copy_r.Move(coup[0],coup[1],coup[2])
                L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                #print({'hauteur':hauteur,'num':num,'sens':sens})
                nextfile.append([copy_r,L2,Cout3(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
        print('remplissage arbre : ',len(nextfile))
        Arbre[prof] = [i[0].cube for i in nextfile]
        nextfile=nextfile[:n]
        #print(nextfile)
        file.extend(nextfile)
        nextfile=[]

        #PARTIE ROLLBACK
        if prof > nbBeforeRollback:
            if file[0][2] <= Cout3(rd.RediCube(Arbre[prof-nbBeforeRollback][0])):
                print('ROLLBACK')
                file=[rd.RediCube(a) for a in (Arbre[prof-nbBeforeRollback][:n])]
                for i in range(prof-nbBeforeRollback,prof+1):
                    del(Arbre[i])
                prof=prof-nbBeforeRollback


    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    return tf,nb_noeuds,sol,Arbre



def Resolution_Arbre_Pierre(r,n,nbBeforeRollback): #1<n
    start_time = time.time()
    r.lastcoup=tuple()
    compteurnbNoeud = 0
    #nbDeCoup = 0
    file=[]
    file.append([r,[],Cout3(r)])
    nextfile=[]
    trouver = False

    #variable Rollback
    nextfileRollBack=file
    nextfileBestCount = file[0][2]
    nbIncBeforeRollBack = nbBeforeRollback
    nbDeCoupBeforeRollBack = nbDeCoup

    #TANT QUE PAS RESOLU
    while not trouver:
        if Cout(file[0][0]) == 44:
            trouver = True
        #SI PAS RESOLU
        else:
            #TANT QUE FILE NON VIDE
            while file:
                print("score noeud suivante : " + str(Cout(file[0][0])))
                compteurnbNoeud+=1
                node = file.pop(0)

                for coup in (r.ListCoups()):
                    L2=[i for i in node[1]]
                    copy_r = node[0].Copy()
                    copy_r.Move(coup[0],coup[1],coup[2])
                    L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                    #print({'hauteur':hauteur,'num':num,'sens':sens})

                    nextfile.append([copy_r,L2,Cout(copy_r)])


            #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
            nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
            file = nextfile[:n]

            if nextfile[0][2] > nextfileBestCount:
                nextfileRollBack=nextfile
                nextfileBestCount = nextfile[0][2]
                nbIncBeforeRollBack = nbBeforeRollback
                nbDeCoup += 1
                nbDeCoupBeforeRollBack = nbDeCoup
                print("profondeur suivante avec pour nombre de dieu : " + str(nbDeCoup))
            else:
                nbIncBeforeRollBack = nbIncBeforeRollBack - 1
                if nbIncBeforeRollBack == 0:
                    nbIncBeforeRollBack = nbBeforeRollback
                    file = nextfileRollBack[:n]
                    nextfileBestCount = file[0][2]
                    nextfileRollBack = nextfileRollBack[n:]
                    nbDeCoup = nbDeCoupBeforeRollBack
                    print("Rollback")
                else:
                    nbDeCoup += 1
                    print("profondeur suivante avec pour nombre de dieu : " + str(nbDeCoup))
            #reset
            nextfile=[]

        tf=round(time.time() - start_time,2)
        sol=file[0][1]
        #Temps de resolution, nombre de noeuds parcouru, solution
        return sol,tf,nbDeCoup,compteurnbNoeud