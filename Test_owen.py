import RediCube as rd
import Face as f
import pandas as pd
import time

Aretes=pd.read_csv('csv/Aretes.csv',sep=';')
Sommets=pd.read_csv('csv/Sommets.csv',sep=';')


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

def Cout4(r):
    rd_resolu = rd.RediCube()
    res=0
    for index,row in Aretes.iterrows():
        if (r.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == rd_resolu.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (r.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']] == rd_resolu.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
            res+=1

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

##Arbre profondeur 4
#Fonctionne avec cout 2
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

#Focntionne avec Cout4
def BestCoup4(r):
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

                if Cout4(copy_r) == 20:
                    L.extend(L1)
                    L.append(Cout4(copy_r))
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

                            if Cout4(copy_r) == 20:
                                L.extend(L1)
                                L.extend(L2)
                                L.append(Cout4(copy_r))
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

                                        if Cout4(copy_r) == 20:
                                            L.extend(L1)
                                            L.extend(L2)
                                            L.extend(L3)
                                            L.append(Cout4(copy_r))
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
                                                    L.append(Cout4(copy_r))

                                                    List_Coups.append(L)





    List_Coups=sorted(List_Coups, key=lambda x: x[-1], reverse = True)
    print("--- %s seconds ---" % (time.time() - start_time))
    return List_Coups

##Arbre, parcours en profondeur, Trop d'appels
def BestCoup5(r,L=[],n=0):
    if Cout4(r) == 20:
        print('REDI FAIT!')
        return L,n

    #elif n==5:
        #print('5 coups atteints')
    else:
        for hauteur in ('up','down'):
            for num in range(1,5):
                for sens in (1,-1):
                    print({'hauteur':hauteur,'num':num,'sens':sens})
                    L2=[i for i in L]
                    n2=n+1
                    copy_r = r.Copy()
                    copy_r.Move(hauteur,num,sens)
                    #print(Cout4(copy_r))
                    L2.append({'hauteur':hauteur,'num':num,'sens':sens})
                    return BestCoup5(copy_r,L2,n2)

##Arbre, parcours en largeur
def BestCoup6(r,L=[]):
    start_time = time.time()

    file=[]
    file.append([r,L])

    while Cout4(file[0][0]) != 20:
        #print(Cout4(file[0]))
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


    print('Redi FAIT')
    print(Cout4(file[0][0]))
    print(file[0][0])
    print(file[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))

##Arbre, parcours en largeur, elagage top n (cout)
def BestCoup7(r,n):
    start_time = time.time()

    file=[]
    file.append([r,[],Cout4(r)])

    while Cout4(file[0][0]) != 20:
        #print(Cout4(file[0]))
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
                    Ltemp.append([copy_r,L2,Cout4(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=Ltemp[:n]
        #print(Ltemp)
        file.extend(Ltemp)


    print('Redi FAIT')
    print(Cout4(file[0][0]))
    print(file[0][0])
    print(file[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))

##Arbre, parcours en largeur, elagage palier n de difference de cout avec le rd d'origine
def BestCoup8(r,n):
    start_time = time.time()

    file=[]
    file.append([r,[],Cout4(r)])

    while Cout4(file[0][0]) != 20:
        #print(Cout4(file[0]))
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
                    Ltemp.append([copy_r,L2,Cout4(copy_r)])

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        Ltemp=sorted(Ltemp, key=lambda x: x[2], reverse = True)
        Ltemp=[i for i in Ltemp if i[2]>=(Cout4(node[0])-n)]
        #print(Ltemp)
        file.extend(Ltemp)


    print('Redi FAIT')
    print(Cout4(file[0][0]))
    print(file[0][0])
    print(file[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))


def Play_moves(r,M):
    for i in range(len(M)-1):
        r.Move(M[i]['hauteur'],M[i]['num'],M[i]['sens'])

