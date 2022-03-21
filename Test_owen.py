import RediCube as rd
import pandas as pd
import time
import multiprocessing
import numpy as np
from collections import Counter
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

def Resolution_Arbre_Rollback(r,n,N=N_elagage1,nbBeforeRollback=4): #1<n<7
    start_time = time.time()
    r.lastcoup=tuple()

    compteur=1
    prof=0
    file=[]
    file.append([r,[],Cout3(r)])
    nextfile=[]
    Arbre={}
    All_Redi=[]
    All_Redi.append(r.cube)
    Mauvais_cout=[]
    Couts_rollbacke=[]


    while file[0][2] != 104 and compteur<N:
        print('-----------')
        print('profondeur = ',str(prof))
        print('Cout max = ',file[0][2])
        while file:
            compteur+=1
            node = file.pop(0)
            for coup in (node[0].ListCoups()):
                L2=[i for i in node[1]]
                copy_r = node[0].Copy()

                copy_r.Move(coup[0],coup[1],coup[2])
                cout=Cout3(copy_r)

                if copy_r.cube not in All_Redi and cout not in Mauvais_cout:
                    All_Redi.append(copy_r.cube)
                    L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                    nextfile.append([copy_r,L2,Cout3(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
        Arbre[prof+1] = [[i[0].cube,i[1]] for i in nextfile]
        print('creation arbre niveau : ',prof+1)
        print('remplissage arbre : ',len(nextfile))
        nextfile=nextfile[:n]
        #print(nextfile)
        file.extend(nextfile)
        nextfile=[]

        prof+=1

        #PARTIE ROLLBACK
        if prof - nbBeforeRollback > 0:
            if file[0][2] <= Cout3(rd.RediCube(Arbre[prof-(nbBeforeRollback)][0][0])):
                print('-----------')
                print('profondeur = ',str(prof))
                print('Cout max = ',file[0][2])
                print(file[0][2], ' <= ',Cout3(rd.RediCube(Arbre[prof-(nbBeforeRollback)][0][0])), ' ROLLBACK à ' , prof-(nbBeforeRollback))
                #on blacklist si un cout est apparu au moins 3 fois comme cout max lors des 5 derniers niveaux (actuel compris)
                Last_couts= [Cout3(rd.RediCube(Arbre[a][0][0])) for a in range(prof-nbBeforeRollback,prof+1)]
                occurrences = Counter(Last_couts).most_common(1)
                if occurrences[0][1] >=3:
                    Mauvais_cout.append(occurrences[0][0])
                    print('Cout = ',occurrences[0][0],' sera refusé')
                Couts_rollbacke.append(file[0][2])
                #on blacklist si un cout à mené au rollback plus d'une fois
                if Couts_rollbacke.count(file[0][2])>1:
                    Mauvais_cout.append(file[0][2])
                    print('Cout = ',file[0][2],' sera refusé')
                file=[[rd.RediCube(a[0]),a[1],Cout3(rd.RediCube(a[0]))] for a in (Arbre[prof-(nbBeforeRollback)][n:])]
                print('Len(file) = ',len(file))
                for i in range(prof-nbBeforeRollback,prof+1):
                    print('suppression arbre niveau : ',i)
                    del(Arbre[i])
                print('Recréation arbre niveau : ',prof-nbBeforeRollback)
                Arbre[prof-nbBeforeRollback] = [[i[0].cube,i[1]] for i in file]
                file=file[:n]
                prof-=nbBeforeRollback

    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    print('Resolution en ',len(sol),' coups')
    return tf,nb_noeuds,sol#,Arbre


#Regarde possibilitee de rollback sur 4 coups, mais remonte à 5 coups
def Resolution_Arbre_Rollback_V2(r,n,N=N_elagage1,nbBeforeRollback=4): #1<n<7
    start_time = time.time()
    r.lastcoup=tuple()

    compteur=1
    prof=0
    file=[]
    file.append([r,[],Cout3(r)])
    nextfile=[]
    Arbre={}
    All_Redi=[]
    All_Redi.append(r.cube)
    Mauvais_cout=[]
    Couts_rollbacke=[]


    while file[0][2] != 104 and compteur<N:
        print('-----------')
        print('profondeur = ',str(prof))
        print('Cout max = ',file[0][2])
        while file:
            compteur+=1
            node = file.pop(0)
            for coup in (node[0].ListCoups()):
                L2=[i for i in node[1]]
                copy_r = node[0].Copy()

                copy_r.Move(coup[0],coup[1],coup[2])
                cout=Cout3(copy_r)

                if copy_r.cube not in All_Redi and cout not in Mauvais_cout:
                    All_Redi.append(copy_r.cube)
                    L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                    nextfile.append([copy_r,L2,Cout3(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
        Arbre[prof+1] = [[i[0].cube,i[1]] for i in nextfile]
        print('creation arbre niveau : ',prof+1)
        print('remplissage arbre : ',len(nextfile))
        nextfile=nextfile[:n]
        #print(nextfile)
        file.extend(nextfile)
        nextfile=[]

        prof+=1

        #PARTIE ROLLBACK
        if prof - (nbBeforeRollback+1) > 0:
            if file[0][2] <= Cout3(rd.RediCube(Arbre[prof-(nbBeforeRollback)][0][0])):
                print('-----------')
                print('profondeur = ',str(prof))
                print('Cout max = ',file[0][2])
                print(file[0][2], ' <= ',Cout3(rd.RediCube(Arbre[prof-(nbBeforeRollback)][0][0])), ' ROLLBACK à ' , prof-(nbBeforeRollback+1))
                #on blacklist si un cout est apparu au moins 3 fois comme cout max lors des 5 derniers niveaux (actuel compris)
                Last_couts= [Cout3(rd.RediCube(Arbre[a][0][0])) for a in range(prof-nbBeforeRollback,prof+1)]
                occurrences = Counter(Last_couts).most_common(1)
                if occurrences[0][1] >=3:
                    Mauvais_cout.append(occurrences[0][0])
                    print('Cout = ',occurrences[0][0],' sera refusé')
                Couts_rollbacke.append(file[0][2])
                #on blacklist si un cout à mené au rollback plus d'une fois
                if Couts_rollbacke.count(file[0][2])>1:
                    Mauvais_cout.append(file[0][2])
                    print('Cout = ',file[0][2],' sera refusé')
                file=[[rd.RediCube(a[0]),a[1],Cout3(rd.RediCube(a[0]))] for a in (Arbre[prof-(nbBeforeRollback+1)][n:])]
                #print('Len(file) = ',len(file))
                for i in range(prof-(nbBeforeRollback+1),prof+1):
                    print('suppression arbre niveau : ',i)
                    del(Arbre[i])
                print('Recréation arbre niveau : ',prof-(nbBeforeRollback+1))
                Arbre[prof-(nbBeforeRollback+1)] = [[i[0].cube,i[1]] for i in file]
                print('remplissage arbre : ',len(Arbre[prof-(nbBeforeRollback+1)]))
                file=file[:n]
                prof-=nbBeforeRollback+1

    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    print('Resolution en ',len(sol),' coups')
    return tf,nb_noeuds,sol#,Arbre

#Rollback individuel
def Resolution_Arbre_Rollback_V3(r,n,N=N_elagage1,nbBeforeRollback=4): #1<n<7
    start_time = time.time()
    r.lastcoup=tuple()

    compteur=1#nombre de noeuds parcouru
    prof=0
    file=[]
    file.append([r,[],Cout3(r)])#file = [[redi,[coups],cout],...]
    nextfile=[]#nextfile = [[redi,[coups],cout],...]
    Arbre={}#Arbre = {prodondeur : [[redi.cube,[coups],position du parent dans file],...], ....}
    All_Redi=[]
    All_Redi.append(r.cube)
    Noeuds_par_prof={}#Noeuds_par_prof = {profondeur : nombre de noeuds explorés+1 (len(file),...}


    while file[0][2] != 104 and compteur<N:
        print('-----------')
        print('profondeur = ',str(prof))
        print('Cout max = ',file[0][2])
        position_file=0
        while file:
            compteur+=1
            node = file.pop(0)
            for coup in (node[0].ListCoups()):
                L2=[i for i in node[1]]
                copy_r = node[0].Copy()

                copy_r.Move(coup[0],coup[1],coup[2])
                cout=Cout3(copy_r)

                if copy_r.cube not in All_Redi:
                    All_Redi.append(copy_r.cube)
                    L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                    nextfile.append([copy_r,L2,Cout3(copy_r),position_file])
            position_file+=1

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
        Arbre[prof+1] = [[i[0].cube,i[1],i[3]] for i in nextfile]
        nextfile=[[i[0],i[1],i[2]] for i in nextfile]
        print('creation arbre niveau : ',prof+1)
        print('remplissage arbre : ',len(nextfile))
        #nextfile=nextfile[:n]
        file.extend(Prochain_file(n,nextfile))
        Noeuds_par_prof[prof+1] = len(file)
        #print(nextfile)
        #file.extend(nextfile)
        nextfile=[]

        prof+=1
        position_file=0

        #PARTIE ROLLBACK
        for f in range(len(file)):
            if len(file[f][1]) - nbBeforeRollback > 0:
                pos=f
                for p in range(nbBeforeRollback):
                    pos=Arbre[len(file[f][1])-p][pos][2]
                if file[f][2] <= Cout3(rd.RediCube(Arbre[len(file[f][1])-nbBeforeRollback][pos][0])):
                    #del(Arbre[len(file[f][1])-nbBeforeRollback][pos])
                    nouveau_noeud=Noeuds_par_prof[len(file[f][1])-nbBeforeRollback]
                    print('ROLLBACK ',nouveau_noeud+1, ' eme noeuds, profondeur ',len(file[f][1])-nbBeforeRollback)
                    Noeuds_par_prof[len(file[f][1])-nbBeforeRollback]+=1


                    file[f] = [rd.RediCube(Arbre[len(file[f][1])-nbBeforeRollback][nouveau_noeud][0]),Arbre[len(file[f][1])-nbBeforeRollback][nouveau_noeud][1],Cout3(rd.RediCube(Arbre[len(file[f][1])-nbBeforeRollback][nouveau_noeud][0]))]





                    #print('changement Noeuds_par prof, profondeur = ',len(file[f][1])-nbBeforeRollback,', ',Noeuds_par_prof[len(file[f][1])-nbBeforeRollback], ' eme noeuds')


    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    print('Resolution en ',len(sol),' coups')
    return tf,nb_noeuds,sol#,Arbre

def Prochain_file(n,nextfile):
    L=set(len(i[1]) for i in nextfile)
    nextfile=sorted(nextfile, key=lambda x: len(x[1]), reverse = False)
    D={}
    for i in L:
        Ltemp=[]
        for j in nextfile:
            if len(j[1])==i:
                Ltemp.append(j)
        D[i] = Ltemp

    file=[]
    for k in D.keys():
        print('len(D[k]) = ',len(D[k]))
        D[k]=sorted(D[k], key=lambda x: x[2], reverse = True)
        file.extend(D[k][:int((len(D[k])/len(nextfile))*n)+1])

    print('len(file)= ',len(file))
    return file


def CreateRedicubeToResolve(text):
    listLigne = [text[i:i+3] for i in range(0, len(text), 3)]
    listLigne2 = []
    for i in listLigne:
        l=[]
        for j in i:
            l.append(j)
        listLigne2.append(l)
    listFace=[]
    couleur=0
    for i in range(0,len(listLigne2),3):
      listFace.append(rd.Face(rd.listFaceCouleur[couleur],listLigne2[i:i+3]))
      couleur+=1
    return rd.RediCube(listFace)

def CreateRedicubeToResolveVisua(n):
    df = pd.read_csv('csv/DataSet.csv',sep=';')
    if n >= len(df):
        return ["error","Valeur maximale autorisé : " + str(len(df))]
    text = df.loc[n].Pos
    r = CreateRedicubeToResolve(text)
    return r

def TestDataSet(n):
    for i in range(n):
        start_time = time.time()
        print('-------------------')
        print('REDI NUMERO ',i)
        r=CreateRedicubeToResolveVisua(i)
        Resolution_Arbre_Rollback_V2(r,10)
    print('--------------')
    print(time.time() - start_time,' secondes.')


##Fonction permettant de calculer le temps pris pour un N noeuds
def Comparaison_vitesse_fonctions(nb_noeuds=1000):
    df=gd.rd.pd.DataFrame(columns=['temps resolution elagage 1 n=2','temps resolution elagage 1 n=3',
    'temps resolution elagage 1 n=4','temps resolution elagage 1 n=5','temps resolution elagage 1 n=6',
    'temps resolution elagage 2 n=1','temps resolution elagage 2 n=2','temps resolution elagage 2 n=3',
    'temps resolution elagage 2 n=4','temps resolution elagage 2 n=5'])

    for redi in range(5):
        r=gd.rd.RediCube()
        r.Melange(10)

        t2=Resolution_Arbre_Rollback_Owen(r,2,N=nb_noeuds)[0]
        t3=Resolution_Arbre_Rollback_Owen(r,3,N=nb_noeuds)[0]
        t4=Resolution_Arbre_Rollback_Owen(r,4,N=nb_noeuds)[0]
        t5=Resolution_Arbre_Rollback_Owen(r,5,N=nb_noeuds)[0]
        t6=Resolution_Arbre_Rollback_Owen(r,6,N=nb_noeuds)[0]

        t7=Resolution_Arbre_Pierre(r,1,N=nb_noeuds)[0]
        t8=Resolution_Arbre_Pierre(r,2,N=nb_noeuds)[0]
        t9=Resolution_Arbre_Pierre(r,3,N=nb_noeuds)[0]
        t10=Resolution_Arbre_Pierre(r,4,N=nb_noeuds)[0]
        t11=Resolution_Arbre_Pierre(r,5,N=nb_noeuds)[0]

        df=df.append({'temps resolution elagage 1 n=2':t2,
        'temps resolution elagage 1 n=3':t3,'temps resolution elagage 1 n=4':t4,'temps resolution elagage 1 n=5':t5,
        'temps resolution elagage 1 n=6':t6,'temps resolution elagage 2 n=1':t7,'temps resolution elagage 2 n=2':t8,
        'temps resolution elagage 2 n=3':t9,'temps resolution elagage 2 n=4':t10,
        'temps resolution elagage 2 n=5':t11},ignore_index=True)

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\Comparaison_temps_fonctions.csv',';',index=False,mode='w')


##Constante indiquant les fonctions à testet
D={'sans_elagage':True,
'elagage1_n=2':True,'elagage1_n=3':True,'elagage1_n=4':True,'elagage1_n=5':True,'elagage1_n=6':True,
'elagage2_n=1':True,'elagage2_n=2':True,'elagage2_n=3':True,'elagage2_n=4':True,'elagage2_n=5':True}

##Comparaison des differentes fonctions en fonction d'une liste de redi
def Comparaison_resolutions_fonction(D,L):
    columns=['Cout']
    for keys,values in D.items():
        if values==True:
            columns.append(keys+'_noeuds')
            columns.append(keys+'_nbCoups')

    df=gd.rd.pd.DataFrame(columns=columns)

    compteur=0
    for r in L:
        compteur+=1
        print('---------------')
        print(str(compteur) + '/' + str(len(L)))
        Ligne=[compteur]

        if D['elagage1_n=2']==True:
            t2,n2,s2=Resolution_Arbre_Pierre(r,2)
            Ligne.extend([n2,len(s2)])
        if D['elagage1_n=3']==True:
            t3,n3,s3=Resolution_Arbre_Pierre(r,3)
            Ligne.extend([n3,len(s3)])
        if D['elagage1_n=4']==True:
            t4,n4,s4=Resolution_Arbre_Pierre(r,4)
            Ligne.extend([n4,len(s4)])
        if D['elagage1_n=5']==True:
            t5,n5,s5=Resolution_Arbre_Pierre(r,5)
            Ligne.extend([n5,len(s5)])
        if D['elagage1_n=6']==True:
            t6,n6,s6=Resolution_Arbre_Pierre(r,6)
            Ligne.extend([n6,len(s6)])

        if D['elagage2_n=1']==True:
            t7,n7,s7=Resolution_Arbre_Rollback_Owen(r,1)
            Ligne.extend([n7,len(s7)])
        if D['elagage2_n=2']==True:
            t8,n8,s8=Resolution_Arbre_Rollback_Owen(r,2)
            Ligne.extend([n8,len(s8)])
        if D['elagage2_n=3']==True:
            t9,n9,s9=Resolution_Arbre_Rollback_Owen(r,3)
            Ligne.extend([n9,len(s9)])
        if D['elagage2_n=4']==True:
            t10,n10,s10=Resolution_Arbre_Rollback_Owen(r,4)
            Ligne.extend([n10,len(s10)])
        if D['elagage2_n=5']==True:
            t11,n11,s11=Resolution_Arbre_Rollback_Owen(r,5)
            Ligne.extend([n11,len(s11)])
        df.loc[len(df)]=Ligne
        df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test_Owen.csv',';',index=False,mode='w')







