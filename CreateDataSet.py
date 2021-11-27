import RediCube as rd
import pandas as pd

def GenerateDataSetRow(r):
    r.Melange(1)
    return r

def ImportCsv():
    df = pd.read_csv('csv/DataSet.csv')
    return df;

def ExportCsv(df):
    df.to_csv(index=False, sep=',')
    
def StartGenerateDataSet(nbfois):
    df = pd.DataFrame(columns=['Pos'])
    r= rd.RediCube()
    for i in range(nbfois):
        r=GenerateDataSetRow(r)
        text = ''
        for j in range(rd.face):
            text += "".join(r.cube[j].__str__().replace('\n',''))
        if text in df.Pos:
            df = df.append(text);
            print("Une new valeur ajouté")
    ExportCsv(df)