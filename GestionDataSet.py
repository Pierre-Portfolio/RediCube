# Import
import RediCube as rd
ScoreRediMax = rd.RediCube().Cout()

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
def CreateRedicubeToResolveVisua(n, lien = 'csv/DataSet.csv'):
    df = rd.pd.read_csv(lien,sep=';')
    if n >= len(df):
        return ["error","Valeur maximale autorisé : " + str(len(df))]
    text = df.loc[n].Pos
    r = CreateRedicubeToResolve(text)
    return r

"""
Function which generates a redicubes from dataset or the visualisation
"""
def CreateRedicubeToResolveInputVisua(textinput):
    if isinstance(textinput, int):
        return CreateRedicubeToResolveVisua(textinput)
    else:
        if textinput.count('X') == 6 and len(textinput) == 54:
            return CreateRedicubeToResolve(textinput)
        else:
            return ["error", "Impossible de créer un RediCube"]
        
      
"""
Function which generate a dataset with a difficulty choose by the user
"""
def GenerateDifficultyDataSet(difficulte, nbRedicube):
    if difficulte <= 2 and difficulte >= 0:
        print("Generatation en cours...")
        df = rd.pd.DataFrame(columns=['Pos'])
        ListDifficulté = [(0, int(ScoreRediMax* 0.2),"Difficile"), 
                          (int(ScoreRediMax * 0.2), int(ScoreRediMax * 0.4), "Moyen"),
                          (int(ScoreRediMax * 0.4), int(ScoreRediMax * 0.7), "Facile")]
        
        for i in range(nbRedicube):
            text = ''
            r = rd.RediCube()
            r.Recherche_cout(ListDifficulté[difficulte][0], ListDifficulté[difficulte][1])
            for j in range(rd.face):
                text += "".join(r.cube[j].__str__().replace('\n','')) 
            if text not in df.Pos:
                df = df.append({"Pos":text},ignore_index=True)
                
        df.to_csv('csv/RediGenerate/' + ListDifficulté[difficulte][2]  + '.csv', index=False, sep=';')
        print("Generate Done...")
    else:
        print("Veillez saisir un nombre entre 0 et 2")