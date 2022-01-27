import RediCube as rd
import Face as f
import pandas as pd
import time
pd.set_option('display.max_columns', 10)
import multiprocessing

Aretes=pd.read_csv('csv/Aretes.csv',sep=';')
Sommets=pd.read_csv('csv/Sommets.csv',sep=';')

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

##Arbre, parcours en largeur
def Resolution_Arbre(r):
    start_time = time.time()

    compteur=0
    file=[]
    file.append([r,[]])

    while Cout(file[0][0]) != 20 and compteur<6000:
        compteur+1
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

    T=-1
    if compteur<6000:
        T=round(time.time() - start_time,2)

    return T

    '''
    print('Redi FAIT')
    print(Cout(file[0][0]))
    print(file[0][0])
    print(file[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))
    '''

##Arbre, parcours en largeur, elagage top n (cout)
def Resolution_Arbre_elagage1(r,n): #1<n<7
    start_time = time.time()

    compteur=0
    file=[]
    file.append([r,[],Cout(r)])


    while Cout(file[0][0]) != 20 and compteur<6000:
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
                    Ltemp.append([copy_r,L2,Cout(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=Ltemp[:n]
        #print(Ltemp)
        file.extend(Ltemp)

    T=-1
    if compteur<6000:
        T=round(time.time() - start_time,2)

    return T

    '''
    print('Redi FAIT')
    print(Cout(file[0][0]))
    print(file[0][0])
    print(file[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))
    '''

##Arbre, parcours en largeur, elagage palier n de difference de cout avec le rd d'origine
def Resolution_Arbre_elagage2(r,n): #1<n
    start_time = time.time()

    compteur=0
    file=[]
    file.append([r,[],Cout(r)])

    while Cout(file[0][0]) != 20 and compteur<6000:
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
                    Ltemp.append([copy_r,L2,Cout(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=[i for i in Ltemp if i[2]>=(Cout(node[0])-n)]
        #print(Ltemp)
        file.extend(Ltemp)

    T=-1
    if compteur<6000:
        T=round(time.time() - start_time,2)

    return T

    '''
    print('Redi FAIT')
    print(Cout(file[0][0]))
    print(file[0][0])
    print(file[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))
    '''


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

    df.to_csv(r'C:\Users\owen9\OneDrive\Documents\GitHub\RediCube\csv\test.csv',';',index=False,mode='w')#enregistrement des données
    #return df



