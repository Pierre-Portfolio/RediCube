import RediCube as rd
import Face as f
import pandas as pd
import time

def ImportCsv(csv):
    df = pd.read_csv(csv,sep=';');
    return df

def ExportCsv(df):
    df.to_csv('csv/DataSet.csv', index=False, sep=';');
    
dfNeighbor = ImportCsv('csv/FaceNeighbor.csv')

#Constante
listEdge = [0,[0,1],[1,0],[1,2],[2,1]]


'''
Function which generate redicube from a string
'''
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
      listFace.append(f.Face(rd.listFaceCouleur[couleur],listLigne2[i:i+3]))
      couleur+=1
    return rd.RediCube(listFace)

'''
Function which generate a redicube from the visualisation
'''
def CreateRedicubeToResolveVisua(text):
    r = CreateRedicubeToResolve(text)
    rd.vi.Visualisation(r,text)
    
'''
Function which generate a redicube from the visualisation
'''
def CreateRedicubeToResolveVisua2(n):
    df = ImportCsv('csv/DataSet.csv')
    text = df.loc[n].Pos
    r = CreateRedicubeToResolve(text)
    rd.vi.Visualisation(r,text)
    return r
    
'''
Function which generates a redicube from the dataset
'''
def CreateRedicubeToResolveDataSet(n):
    df = ImportCsv('csv/DataSet.csv')
    text = df.loc[n].Pos
    return CreateRedicubeToResolve(text)

'''
Find the best face for starting the resolve of redicube & send list of bad coin
'''
def FindBadCoin(r):
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
        if(newR.cube[numFace].tab[tabL[i]][tabC[i]] == newR.cube[numFace].couleur):
            r.Move(hauteur,numMove,1)
        else:
            r.Move(hauteur,numMove,-1)
    return r;

'''
List the edges of on face who are not placed
'''
def ListBadEdgeOnFace(r,numFace):
    edgeDone = []
    
    #for each edge
    for i in range(1,5):
        if(r.cube[numFace].tab[listEdge[i][0]][listEdge[i][1]] == r.cube[numFace].couleur):
            #Save the numface and the edge
            numFaceNeighbor = dfNeighbor[(dfNeighbor['face']==numFace) & (dfNeighbor['direction']==i)]['neighbor'].to_list()
            numEdge = dfNeighbor[(dfNeighbor['face']==numFace) & (dfNeighbor['direction']==i)]['edge'].to_list()
            
            #check the edge dependence
            if(r.cube[ numFaceNeighbor[0] ].tab[ listEdge[numEdge[0]][0] ][ listEdge[numEdge[0]][1] ] == r.cube[numFaceNeighbor[0]].couleur):
                edgeDone.append(i)   
                
    return list(set([1,2,3,4]) - set(edgeDone))