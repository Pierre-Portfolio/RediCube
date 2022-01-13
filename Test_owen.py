import RediCube as rd
import Face as f
import pandas as pd
import time


def FindRedicubeToResolve(n):
    df = ImportCsv()
    text = df.loc[0].Pos
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
      listFace.append(f.Face(rd.listFaceCouleur[couleur],listLigne2[i:i+3]))
      couleur+=1

    return rd.RediCube(listFace)

#1 pour chaque piece de la bonne couleur
def Cout(r):
    rd_resolu = rd.RediCube()
    res=0
    for f in range(rd.face):
        for l in range(3):
            for c in range(3):
                if r.cube[f].tab[l][c] == rd_resolu.cube[f].tab[l][c]:
                    res+=1

    return res

#2 points pour les sommets
def Cout2(r):
    rd_resolu = rd.RediCube()
    res=0
    for f in range(rd.face):
        for l in range(3):
            for c in range(3):
                if r.cube[f].tab[l][c] == rd_resolu.cube[f].tab[l][c]:
                    if r.Type(l,c) == 'sommet':#double valeur pour les sommets
                        res+=2
                    else:
                        res+=1

    return res

def Cout3(r):
    Aretes=pd.read_csv('csv/Aretes.csv',sep=';')
    rd_resolu = rd.RediCube()
    res=0
    for index,row in Aretes.iterrows():
        if (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
            res+=1

    Sommets=pd.read_csv('csv/Sommets.csv',sep=';')
    for index,row in Sommets.iterrows():
        if (r.cube[row['Face']].tab[row['Ligne']][row['Colonne']] == rd_resolu.cube[row['Face']].tab[row['Ligne']][row['Colonne']]):
            res+=1

    return res




def BestCoup(r):
    List_Coups=[]
    for hauteur in ('up','down'):
        for num in range(1,5):
            for sens in (1,-1):
                copy_r = r.Copy()
                copy_r.Move(hauteur,num,sens)
                List_Coups.append([{'hauteur':hauteur,'num':num,'sens':sens},Cout(copy_r)])

    List_Coups=sorted(List_Coups, key=lambda x: x[1], reverse = True)
    return List_Coups

def BestCoup2(r):
    List_Coups=[]
    for hauteur in ('up','down'):
        for num in range(1,5):
            for sens in (1,-1):
                copy_r = r.Copy()
                copy_r.Move(hauteur,num,sens)
                List_Coups.append([{'hauteur':hauteur,'num':num,'sens':sens},Cout2(copy_r)])

    List_Coups=sorted(List_Coups, key=lambda x: x[1], reverse = True)
    return List_Coups

#Arbre profondeur 4
def BestCoup3(r):
    start_time = time.time()

    List_Coups=[]
    L=[]
    for hauteur1 in ('up','down'):
        print('HAUTEUR',hauteur1)
        for num1 in range(1,5):
            print('NUMERO',str(num1))
            for sens1 in (1,-1):
                L=[]
                print('SENS')
                copy_r = r.Copy()
                L1=[]
                copy_r.Move(hauteur1,num1,sens1)
                L1.append({'hauteur':hauteur1,'num':num1,'sens':sens1})

                if Cout2(copy_r) == 78:
                    L.extend(L1)
                    L.append(Cout2(copy_r))
                    List_Coups.append(L)
                    break
                for hauteur2 in ('up','down'):
                    for num2 in range(1,5):
                        for sens2 in (1,-1):
                            copy_r = r.Copy()
                            copy_r.Move(L1[0]['hauteur'],L1[0]['num'],L1[0]['sens'])

                            copy_r.Move(hauteur2,num2,sens2)
                            L2=[]
                            L2.append({'hauteur':hauteur2,'num':num2,'sens':sens2})

                            if Cout2(copy_r) == 78:
                                L.extend(L1)
                                L.extend(L2)
                                L.append(Cout2(copy_r))
                                List_Coups.append(L)
                                break

                            for hauteur3 in ('up','down'):
                                for num3 in range(1,5):
                                    for sens3 in (1,-1):
                                        copy_r = r.Copy()
                                        copy_r.Move(L1[0]['hauteur'],L1[0]['num'],L1[0]['sens'])
                                        copy_r.Move(L2[0]['hauteur'],L2[0]['num'],L2[0]['sens'])

                                        copy_r.Move(hauteur3,num3,sens3)
                                        L3=[]
                                        L3.append({'hauteur':hauteur3,'num':num3,'sens':sens3})

                                        if Cout2(copy_r) == 78:
                                            L.extend(L1)
                                            L.extend(L2)
                                            L.extend(L3)
                                            L.append(Cout2(copy_r))
                                            List_Coups.append(L)
                                            break

                                        for hauteur4 in ('up','down'):
                                            for num4 in range(1,5):
                                                for sens4 in (1,-1):
                                                    L=[]
                                                    copy_r = r.Copy()
                                                    copy_r.Move(L1[0]['hauteur'],L1[0]['num'],L1[0]['sens'])
                                                    copy_r.Move(L2[0]['hauteur'],L2[0]['num'],L2[0]['sens'])
                                                    copy_r.Move(L3[0]['hauteur'],L3[0]['num'],L3[0]['sens'])

                                                    L4=[]
                                                    copy_r.Move(hauteur4,num4,sens4)
                                                    L4.append({'hauteur':hauteur4,'num':num4,'sens':sens4})

                                                    L.extend(L1)
                                                    L.extend(L2)
                                                    L.extend(L3)
                                                    L.extend(L4)
                                                    L.append(Cout2(copy_r))

                                                    List_Coups.append(L)





    List_Coups=sorted(List_Coups, key=lambda x: x[-1], reverse = True)
    print("--- %s seconds ---" % (time.time() - start_time))
    return List_Coups

def Play_moves(r,M):
    for i in range(len(M)-1):
        r.Move(M[i]['hauteur'],M[i]['num'],M[i]['sens'])


##ERREUR, fini par bloquer, cycle sans fin, répétition de coups


def FindFirstFace(r):
    bestface = 0
    bestscoreface = 0
    coinDone = []

    for f in range(rd.face):
        newface=0

        for l in [0,2]:
            for c in [0,2]:
                newscoreface = 0
                newcoinDone = []
                if r.cube[f].tab[l][c] == r.cube[f].couleur:
                    newscoreface = newscoreface + 1

                    if l==0 and c==0:
                        newcoinDone.append(1)
                    elif l==0 and c==2:
                        newcoinDone.append(2)
                    elif l==2 and c==0:
                        newcoinDone.append(3)
                    else:
                        newcoinDone.append(4)


                if(newscoreface > bestscoreface):
                    bestface = f
                    bestscoreface = newscoreface
                    coinDone = [coin for coin in newcoinDone]
    r.faceprincipal = bestface
    print(coinDone)
    return list(set([1,2,3,4]) - set(coinDone))