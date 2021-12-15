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
Function who generate a redicube since a dataset
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
        for j in range(3):
            #on ne cherche que les coins pour le moment
            if(j != 1):
                if(r.cube[i].tab[j][0] == r.cube[i].couleur):
                    newscoreface = newscoreface + 1
                if(r.cube[i].tab[j][2] == r.cube[i].couleur):
                    newscoreface = newscoreface + 1
        if(newscoreface > bestscoreface):
            bestface = i
            bestscoreface = newscoreface
    print(bestface)
    r.faceprincipal = bestface
    

'''
To place the coin of an face of the redicube
'''
def PlaceCoins(r,numFace,coinDone):
    nbCoup = 0
    
    for i in range(len(coinDone)):
        print(i)
    
    return r,nbCoup;

#def ResolveRediCube(n):

