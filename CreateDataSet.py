from RediCube import RediCube
import pandas as pd
import csv

def GenerateDataSetRow(r):
    r.Melange(1)
    return r.cube

def ImportCsv():
    df = pd.DataFrame()
    return df;

def ExportCsv(df):
    with open('csv/DataSet.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(df.count()):
            spamwriter.writerow(df[i])
    

def StartGenerateDataSet(nbfois):
    df = ImportCsv()
    r=RediCube()
    for i in range(nbfois):
        r=GenerateDataSetRow(r)
        if(False):
            print("deja dedans")
        else:
            print("pas dedans")
            df.append(r);
    ExportCsv(df)