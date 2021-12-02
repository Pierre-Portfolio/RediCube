import RediCube as rd
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
    listFace = []
    for i in range(rd.face):
        listLigne = []
        for j in range(3):
            listLigne.append(text[j])
        text = text[3:]
        listFace.append(listLigne[0])
    r = rd.RediCube(listFace)
    return r

#def ResolveRediCube(r,):   
#def FindFirstFace(r):
    