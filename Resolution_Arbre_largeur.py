import RediCube as rd
import Face as f
import pandas as pd
import time
pd.set_option('display.max_columns', 10)
import multiprocessing
import numpy as np

Aretes=pd.read_csv('csv/Aretes.csv',sep=';')
Sommets=pd.read_csv('csv/Sommets.csv',sep=';')

#Nombre correspondant à 5 min de traitement sur ma machine (Owen)
N_sans_elagage=9358
N_elagage1=5452
N_elagage2=3906

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

##Arbre, parcours en largeur
def Resolution_Arbre(r,N=N_sans_elagage):
    start_time = time.time()

    compteur=0
    file=[]
    file.append([r,[]])

    while Cout2(file[0][0]) != 32 and compteur<N:
        compteur+=1
        #print(Cout(file[0]))
        node = file.pop(0)

        for hauteur in ('up','down'):
            for num in range(1,5):
                for sens in (1,-1):
                    L2=[i for i in node[1]]
                    copy_r = node[0].Copy()
                    copy_r.Move(hauteur,num,sens)
                    L2.append({'hauteur':hauteur,'num':num,'sens':sens})
                    #print({'hauteur':hauteur,'num':num,'sens':sens})
                    file.append([copy_r,L2])


    tf=time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    return tf,nb_noeuds,sol


##Arbre, parcours en largeur, elagage top n (cout)
def Resolution_Arbre_elagage1(r,n,N=N_elagage1): #1<n<7
    start_time = time.time()

    compteur=0
    file=[]
    file.append([r,[],Cout(r)])


    while Cout2(file[0][0]) != 32 and compteur<N:
        #print(Cout(file[0]))
        compteur+=1
        node = file.pop(0)

        Ltemp=[]
        for hauteur in ('up','down'):
            for num in range(1,5):
                for sens in (1,-1):
                    L2=[i for i in node[1]]
                    copy_r = node[0].Copy()
                    copy_r.Move(hauteur,num,sens)
                    L2.append({'hauteur':hauteur,'num':num,'sens':sens})
                    #print({'hauteur':hauteur,'num':num,'sens':sens})
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


##Arbre, parcours en largeur, elagage palier n de difference de cout avec le rd d'origine
def Resolution_Arbre_elagage2(r,n,N=N_elagage2): #1<n
    start_time = time.time()

    compteur=0
    file=[]
    file.append([r,[],Cout(r)])

    while Cout2(file[0][0]) != 32 and compteur<N:
        compteur+=1
        #print(Cout(file[0]))
        node = file.pop(0)

        Ltemp=[]
        for hauteur in ('up','down'):
            for num in range(1,5):
                for sens in (1,-1):
                    L2=[i for i in node[1]]
                    copy_r = node[0].Copy()
                    copy_r.Move(hauteur,num,sens)
                    L2.append({'hauteur':hauteur,'num':num,'sens':sens})
                    #print({'hauteur':hauteur,'num':num,'sens':sens})
                    Ltemp.append([copy_r,L2,Cout2(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=[i for i in Ltemp if i[2]>=(Cout2(node[0])-n)]
        #print(Ltemp)
        file.extend(Ltemp)

    tf=round(time.time() - start_time,2)
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]


    #Temps de resolution, nombre de noeuds parcouru, solution
    return tf,nb_noeuds,sol


def Comparaison_vitesse_fonctions(nb_noeuds=1000):
    df=pd.DataFrame(columns=['temps resolution elagage 1 n=2','temps resolution elagage 1 n=3',
    'temps resolution elagage 1 n=4','temps resolution elagage 1 n=5','temps resolution elagage 1 n=6',
    'temps resolution elagage 2 n=1','temps resolution elagage 2 n=2','temps resolution elagage 2 n=3',
    'temps resolution elagage 2 n=4','temps resolution elagage 2 n=5'])

    for redi in range(5):
        r=rd.RediCube()
        r.Melange(10)

        t1=Resolution_Arbre(r,N=nb_noeuds)[0]

        t2=Resolution_Arbre_elagage1(r,2,N=nb_noeuds)[0]
        t3=Resolution_Arbre_elagage1(r,3,N=nb_noeuds)[0]
        t4=Resolution_Arbre_elagage1(r,4,N=nb_noeuds)[0]
        t5=Resolution_Arbre_elagage1(r,5,N=nb_noeuds)[0]
        t6=Resolution_Arbre_elagage1(r,6,N=nb_noeuds)[0]

        t7=Resolution_Arbre_elagage2(r,1,N=nb_noeuds)[0]
        t8=Resolution_Arbre_elagage2(r,2,N=nb_noeuds)[0]
        t9=Resolution_Arbre_elagage2(r,3,N=nb_noeuds)[0]
        t10=Resolution_Arbre_elagage2(r,4,N=nb_noeuds)[0]
        t11=Resolution_Arbre_elagage2(r,5,N=nb_noeuds)[0]

        df=df.append({'temps resolution arbre':t1,'temps resolution elagage 1 n=2':t2,
        'temps resolution elagage 1 n=3':t3,'temps resolution elagage 1 n=4':t4,'temps resolution elagage 1 n=5':t5,
        'temps resolution elagage 1 n=6':t6,'temps resolution elagage 2 n=1':t7,'temps resolution elagage 2 n=2':t8,
        'temps resolution elagage 2 n=3':t9,'temps resolution elagage 2 n=4':t10,
        'temps resolution elagage 2 n=5':t11},ignore_index=True)

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\Comparaison_temps_fonctions.csv',';',index=False,mode='w')

D={'sans_elagage':True,
'elagage1_n=2':True,'elagage1_n=3':True,'elagage1_n=4':True,'elagage1_n=5':True,'elagage1_n=6':True,
'elagage2_n=1':True,'elagage2_n=2':True,'elagage2_n=3':True,'elagage2_n=4':True,'elagage2_n=5':True}

##Comparaison des differentes fonctions en fonction de plusieurs mélanges
def Comparaison_resolutions_fonction(D,melange_min,melange_max,n):
    columns=['melange']
    for keys,values in D.items():
        if values==True:
            columns.append(keys+'_noeuds')
            columns.append(keys+'_nbCoups')

    df=pd.DataFrame(columns=columns)

    for melange in range(melange_min,melange_max+1):
        for redi in range(n):
            r=rd.RediCube()
            r.Melange(melange)
            Ligne=[melange]

            if D['sans_elagage']==True:
                t1,n1,s1=Resolution_Arbre(r)
                Ligne.extend([n1,len(s1)])

            if D['elagage1_n=2']==True:
                t2,n2,s2=Resolution_Arbre_elagage1(r,2)
                Ligne.extend([n2,len(s2)])
            if D['elagage1_n=3']==True:
                t3,n3,s3=Resolution_Arbre_elagage1(r,3)
                Ligne.extend([n3,len(s3)])
            if D['elagage1_n=4']==True:
                t4,n4,s4=Resolution_Arbre_elagage1(r,4)
                Ligne.extend([n4,len(s4)])
            if D['elagage1_n=5']==True:
                t5,n5,s5=Resolution_Arbre_elagage1(r,5)
                Ligne.extend([n5,len(s5)])
            if D['elagage1_n=6']==True:
                t6,n6,s6=Resolution_Arbre_elagage1(r,6)
                Ligne.extend([n6,len(s6)])

            if D['elagage2_n=1']==True:
                t7,n7,s7=Resolution_Arbre_elagage2(r,1)
                Ligne.extend([n7,len(s7)])
            if D['elagage2_n=2']==True:
                t8,n8,s8=Resolution_Arbre_elagage2(r,2)
                Ligne.extend([n8,len(s8)])
            if D['elagage2_n=3']==True:
                t9,n9,s9=Resolution_Arbre_elagage2(r,3)
                Ligne.extend([n9,len(s9)])
            if D['elagage2_n=4']==True:
                t10,n10,s10=Resolution_Arbre_elagage2(r,4)
                Ligne.extend([n10,len(s10)])
            if D['elagage2_n=5']==True:
                t11,n11,s11=Resolution_Arbre_elagage2(r,5)
                Ligne.extend([n11,len(s11)])

            df.loc[len(df)]=Ligne

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test_Owen.csv',';',index=False,mode='w')

##Comparaison des differentes fonctions en fonction de plusieurs couts
def Comparaison_resolutions_fonction2(D,cout_min,cout_max,n):
    columns=['Cout']
    for keys,values in D.items():
        if values==True:
            columns.append(keys+'_noeuds')
            columns.append(keys+'_nbCoups')

    df=pd.DataFrame(columns=columns)

    for redi in range(n):
        print('---------------')
        print(str(redi+1) + '/' + str(n))
        r=rd.RediCube()
        r.Recherche_cout(cout_min,cout_max)
        Ligne=[Cout2(r)]

        if D['sans_elagage']==True:
            t1,n1,s1=Resolution_Arbre(r)
            Ligne.extend([n1,len(s1)])

        if D['elagage1_n=2']==True:
            t2,n2,s2=Resolution_Arbre_elagage1(r,2)
            Ligne.extend([n2,len(s2)])
        if D['elagage1_n=3']==True:
            t3,n3,s3=Resolution_Arbre_elagage1(r,3)
            Ligne.extend([n3,len(s3)])
        if D['elagage1_n=4']==True:
            t4,n4,s4=Resolution_Arbre_elagage1(r,4)
            Ligne.extend([n4,len(s4)])
        if D['elagage1_n=5']==True:
            t5,n5,s5=Resolution_Arbre_elagage1(r,5)
            Ligne.extend([n5,len(s5)])
        if D['elagage1_n=6']==True:
            t6,n6,s6=Resolution_Arbre_elagage1(r,6)
            Ligne.extend([n6,len(s6)])

        if D['elagage2_n=1']==True:
            t7,n7,s7=Resolution_Arbre_elagage2(r,1)
            Ligne.extend([n7,len(s7)])
        if D['elagage2_n=2']==True:
            t8,n8,s8=Resolution_Arbre_elagage2(r,2)
            Ligne.extend([n8,len(s8)])
        if D['elagage2_n=3']==True:
            t9,n9,s9=Resolution_Arbre_elagage2(r,3)
            Ligne.extend([n9,len(s9)])
        if D['elagage2_n=4']==True:
            t10,n10,s10=Resolution_Arbre_elagage2(r,4)
            Ligne.extend([n10,len(s10)])
        if D['elagage2_n=5']==True:
            t11,n11,s11=Resolution_Arbre_elagage2(r,5)
            Ligne.extend([n11,len(s11)])

        df.loc[len(df)]=Ligne

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test_Owen.csv',';',index=False,mode='w')


def Test_Resolution(n):
    df=pd.DataFrame(columns=['melange','temps resolution arbre',
    'temps resolution elagage 1 n=2','temps resolution elagage 1 n=3','temps resolution elagage 1 n=4','temps resolution elagage 1 n=5','temps resolution elagage 1 n=6',
    'temps resolution elagage 2 n=1','temps resolution elagage 2 n=2','temps resolution elagage 2 n=3','temps resolution elagage 2 n=4','temps resolution elagage 2 n=5'])
    for melange in range(1,4):
        for redi in range(n):
            r=rd.RediCube()
            r.Melange(melange)

            t1=Resolution_Arbre(r)

            t2=Resolution_Arbre_elagage1(r,2)
            t3=Resolution_Arbre_elagage1(r,3)
            t4=Resolution_Arbre_elagage1(r,4)
            t5=Resolution_Arbre_elagage1(r,5)
            t6=Resolution_Arbre_elagage1(r,6)

            t7=Resolution_Arbre_elagage2(r,1)
            t8=Resolution_Arbre_elagage2(r,2)
            t9=Resolution_Arbre_elagage2(r,3)
            t10=Resolution_Arbre_elagage2(r,4)
            t11=Resolution_Arbre_elagage2(r,5)

            df=df.append({'melange':int(melange),'melange':melange,'temps resolution arbre':t1,
            'temps resolution elagage 1 n=2':t2,'temps resolution elagage 1 n=3':t3,'temps resolution elagage 1 n=4':t4,'temps resolution elagage 1 n=5':t5,'temps resolution elagage 1 n=6':t6,
            'temps resolution elagage 2 n=1':t7,'temps resolution elagage 2 n=2':t8,'temps resolution elagage 2 n=3':t9,'temps resolution elagage 2 n=4':t10,'temps resolution elagage 2 n=5':t11},ignore_index=True)

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test_Owen.csv',';',index=False,mode='w')#enregistrement des données
    #return df

def Test_Resolution2(n):
    df=pd.DataFrame(columns=['melange',
    'temps resolution elagage 1 n=2','temps resolution elagage 1 n=3','temps resolution elagage 1 n=4','temps resolution elagage 1 n=5','temps resolution elagage 1 n=6',
    'temps resolution elagage 2 n=1','temps resolution elagage 2 n=2'])
    for melange in range(3,6):
        for redi in range(n):
            r=rd.RediCube()
            r.Melange(melange)

            #t1=Resolution_Arbre(r)

            t2=Resolution_Arbre_elagage1(r,2)
            t3=Resolution_Arbre_elagage1(r,3)
            t4=Resolution_Arbre_elagage1(r,4)
            t5=Resolution_Arbre_elagage1(r,5)
            t6=Resolution_Arbre_elagage1(r,6)

            t7=Resolution_Arbre_elagage2(r,1)
            t8=Resolution_Arbre_elagage2(r,2)
            #t9=Resolution_Arbre_elagage2(r,3)
            #t10=Resolution_Arbre_elagage2(r,4)
            #t11=Resolution_Arbre_elagage2(r,5)

            df=df.append({'melange':int(melange),'melange':melange,
            'temps resolution elagage 1 n=2':t2,'temps resolution elagage 1 n=3':t3,'temps resolution elagage 1 n=4':t4,'temps resolution elagage 1 n=5':t5,'temps resolution elagage 1 n=6':t6,
            'temps resolution elagage 2 n=1':t7,'temps resolution elagage 2 n=2':t8},ignore_index=True)

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test2_Owen.csv',';',index=False,mode='w')

def Test_Resolution3(n):
    df=pd.DataFrame(columns=['melange','temps resolution elagage 1 n=3','temps resolution elagage 1 n=4',
    'temps resolution elagage 1 n=5'])
    for melange in range(5,8):
        for redi in range(n):
            r=rd.RediCube()
            r.Melange(melange)

            #t1=Resolution_Arbre(r)

            #t2=Resolution_Arbre_elagage1(r,2)
            t3=Resolution_Arbre_elagage1(r,3)
            t4=Resolution_Arbre_elagage1(r,4)
            t5=Resolution_Arbre_elagage1(r,5)
            #t6=Resolution_Arbre_elagage1(r,6)

            #t7=Resolution_Arbre_elagage2(r,1)
            #t8=Resolution_Arbre_elagage2(r,2)
            #t9=Resolution_Arbre_elagage2(r,3)
            #t10=Resolution_Arbre_elagage2(r,4)
            #t11=Resolution_Arbre_elagage2(r,5)

            df=df.append({'melange':int(melange),'melange':melange,'temps resolution elagage 1 n=3':t3,
            'temps resolution elagage 1 n=4':t4,'temps resolution elagage 1 n=5':t5},ignore_index=True)

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test2_Owen.csv',';',index=False,mode='w')



