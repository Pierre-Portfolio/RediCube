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

def Cout(r):
    rd_resolu = rd.RediCube()
    res=0
    for f in range(rd.face):
        for l in range(3):
            for c in range(3):
                if r.cube[f].tab[l][c] == rd_resolu.cube[f].tab[l][c]:
                    res+=1

    return res

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

##ERREUR, fini par bloquer, cycle sans fin, répétition de coups



def FonctionPierre(numFace,numCorner):
        hauteur = rd.Moves[(rd.Moves['numero de face']==numFace) & (rd.Moves['numero de corner']==numCorner)]['hauteur'].tolist()[0]
        numMove = rd.Moves[(rd.Moves['numero de face']==numFace) & (rd.Moves['numero de corner']==numCorner)]['numero'].tolist()[0]

        return hauteur,numMove