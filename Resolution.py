import RediCube as rd
import Face as f
import pandas as pd
import time

def ImportCsv():
    df = pd.read_csv('csv/DataSet.csv')
    return df;

def ExportCsv(df):
    df.to_csv('csv/DataSet.csv', index=False, sep=',')

'''
Function which generates a redicube from a dataset
'''
def CreateRedicubeToResolve(n):
    df = ImportCsv()
    text = df.loc[n].Pos
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

'''
Find the best face for starting the resolve of redicube
'''
def FindFirstFace(r):
    bestface = 0
    bestscoreface = 0
    coinDone = []

    for i in range(rd.face):
        newface=0
        newscoreface = 0
        newcoinDone = []
        for j in [0,2]:
            if(r.cube[i].tab[j][0] == r.cube[i].couleur):
                newscoreface = newscoreface + 1
                if(j==0):
                    newcoinDone.append(1)
                else:
                    newcoinDone.append(3)
            if(r.cube[i].tab[j][2] == r.cube[i].couleur):
                newscoreface = newscoreface + 1
                if(j==0):
                    newcoinDone.append(2)
                else:
                    newcoinDone.append(4)
        if(newscoreface > bestscoreface):
            bestface = i
            bestscoreface = newscoreface
            coinDone = newcoinDone
    r.faceprincipal = bestface
    return list(set([1,2,3,4]) - set(coinDone))

'''
To place the coin of an face of the redicube
'''
def PlaceAllCoins(r,numFace,coinToComplete):
    tabL = [0,0,0,2,2]
    tabC = [0,0,2,0,2]
    for i in coinToComplete:
        hauteur,numMove = r.InverseMove(numFace,i)
        newR = r.Copy()
        newR.Move(hauteur,numMove,1)
        print(newR)
        print(newR.cube[numFace].tab[tabL[i]][tabC[i]])
        print(newR.cube[numFace].couleur)
        if(newR.cube[numFace].tab[tabL[i]][tabC[i]] == newR.cube[numFace].couleur):
            print("here")
            r.Move(hauteur,numMove,1)
        else:
            print("not here")
            r.Move(hauteur,numMove,-1)
    #redi,nbCoup
    return r;

def ResolveRediCube(n):
    r = CreateRedicubeToResolve(n)
    listface = FindFirstFace(r)
    r.nbCoup = len(listface)
    r = PlaceAllCoins(r,r.faceprincipal,listface)
    return r