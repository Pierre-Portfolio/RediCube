#from RediCube import RediCube

import csv
with open('csv/DataSet.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


"""
def GenerateDataSetRow():
    r=RediCube()
    r.Melange(4)
"""
    