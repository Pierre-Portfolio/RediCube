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

    #return rd.RediCube(listFace)
    return listFace

#def ResolveRediCube(r,):
#def FindFirstFace(r):
