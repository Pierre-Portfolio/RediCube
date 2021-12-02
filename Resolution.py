import RediCube as rd
import Face as f
import pandas as pd
import time

def ImportCsv():
    df = pd.read_csv('csv/DataSet.csv')
    return df;

def ExportCsv(df):
    df.to_csv('csv/DataSet.csv', index=False, sep=',')
    
def FindRedicubeToResolve(n):
    df = ImportCsv()
    text = df.loc[0].Pos
    listLigne = [text[i:i+3] for i in range(0, len(text), 3)]    
    listFace = []
    for i in range(0,len(listLigne),3):
        listFace.append(f.Face(rd.listFaceCouleur[i],listLigne[i,i+3]))
    r = rd.RediCube(listFace)
    return r

#def ResolveRediCube(r,):   
#def FindFirstFace(r):
    