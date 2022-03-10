import RediCube as rd
import Face as f
import pandas as pd
import time
import Resolution_Arbre_largeur
import Visualisation as vi

def ImportCsv(csv):
    df = pd.read_csv(csv,sep=';')
    return df

def ExportCsv(df):
    df.to_csv('csv/DataSet.csv', index=False, sep=';')

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
def CreateRedicubeToResolveVisua(n):
    df = ImportCsv('csv/DataSet.csv')
    text = df.loc[n].Pos
    r = CreateRedicubeToResolve(text)
    return r

"""
Function which generates a redicubes from dataset or the visualisation
"""
def CreateRedicubeToResolveInputVisua(textinput):
    r = rd.RediCube()
    if isinstance(textinput, int):
        r = CreateRedicubeToResolveVisua(textinput)
    else:
        if textinput.count('X') == 6:
            r = CreateRedicubeToResolve(textinput)
    vi.Visualisation(r)
    return r

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
        if(newscoreface >= bestscoreface):
            bestface = i
            bestscoreface = newscoreface
            coinDone = newcoinDone
    r.faceprincipal = bestface
    return list(set([1,2,3,4]) - set(coinDone))

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

'''
Return boolean for said if the first face is finished
'''
def FirstCouronne():
    return 0

'''
Avant premiere face:
    on analyse face par face et effectuons le scoring suivant:
        1 point: coin bien placé
        2 point: arette bien placé
        3 points: coin & son arette
        4 points: une ligne
        5 points: 1 coint et ses 2 arettes
            
    -> Une fois la premiere face faite on reset le roolback a cet instant T
    -> Blocage du nbr de coup a 4
    
    -> Changement Potentielle ( a tester ) du scoring suivant ci-dessous :
    Scoring poentielle suivant:
        1point: coin bien placé
        2point: coin & son arette
        3points: une ligne
        5points: 1 coint et ses 2 arettes
'''
def CoutPierre():
    return 0