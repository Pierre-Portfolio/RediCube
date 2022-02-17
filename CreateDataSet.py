import RediCube as rd
import pandas as pd
import time

def ImportCsv():
    df = pd.read_csv('csv/DataSet.csv')
    return df;

def ExportCsv(df):
    df.to_csv('csv/DataSet.csv', index=False, sep=',')
    
"""
Function which generate the file Dataset.csv
"""
def StartGenerateDataSet(nbfois):
    start_time = time.time()
    nbfind = 0
    df = pd.DataFrame(columns=['Pos'])
    r= rd.RediCube()
    while nbfind != nbfois:
        r.Melange(1)
        text = ''
        for j in range(rd.face):
            text += "".join(r.cube[j].__str__().replace('\n',''))
        if text not in df.Pos:
            df = df.append({"Pos":text},ignore_index=True)
            nbfind += 1
            print("Une new valeur ajouté : " , nbfind)
    ExportCsv(df)
    print("--- %s seconds ---" % (time.time() - start_time))