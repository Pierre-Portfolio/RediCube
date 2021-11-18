from RediCube import RediCube
import pandas as pd

def GenerateDataSetRow(r):
    r.Melange(1)
    return r.cube

def GenerateDataSet(nbfois):
    df = pd.DataFrame()
    r=RediCube()
    for i in range(nbfois):
        df = df.append(r)
    return df

r=RediCube()
for i in r.cube:
    print(i)
    print('\n')
    
"""
import csv
with open('csv/DataSet.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
"""

"""
def GenerateDataSetRow():
    r=RediCube()
    r.Melange(4)
"""
    