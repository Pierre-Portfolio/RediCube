# Import
import RediCube as rd

"""
Function which generates the file Dataset.csv
"""
def StartGenerateDataSet(nbfois):
    start_time = rd.time.time()
    nbfind = 0
    df = rd.pd.DataFrame(columns=['Pos'])
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
    df.to_csv('csv/DataSet.csv', index=False, sep=';')
    print("--- %s seconds ---" % (rd.time.time() - start_time))
    
'''
Function which generates redicube from a string
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
      listFace.append(rd.Face(rd.listFaceCouleur[couleur],listLigne2[i:i+3]))
      couleur+=1
    return rd.RediCube(listFace)

'''
Function which generates a redicube from the visualisation
'''
def CreateRedicubeToResolveVisua(n):
    df = rd.pd.read_csv('csv/DataSet.csv',sep=';')
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
    rd.vi.Visualisation(r)
    return r