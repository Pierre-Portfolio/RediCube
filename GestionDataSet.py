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
    df.to_csv('csv/RediGenerate/Random.csv', index=False, sep=';')
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
def CreateRedicubeToResolveVisua(n, lien = 'csv/RediGenerate/Random.csv'):
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
        df = rd.pd.DataFrame(columns=['Pos','Cout'])
        ListDifficulte = [(0, int(ScoreRediMax* 0.2),"Difficile"), 
                          (int(ScoreRediMax * 0.2), int(ScoreRediMax * 0.4), "Moyen"),
                          (int(ScoreRediMax * 0.4), int(ScoreRediMax * 0.7), "Facile")]
        
        for i in range(nbRedicube):
            text = ''
            r = rd.RediCube()
            r.Recherche_cout(ListDifficulte[difficulte][0], ListDifficulte[difficulte][1])
            for j in range(rd.face):
                text += "".join(r.cube[j].__str__().replace('\n','')) 
            if text not in df.Pos:
                df = df.append({"Pos":text,"Cout":r.Cout()},ignore_index=True)
                
        df.to_csv('csv/RediGenerate/' + ListDifficulte[difficulte][2]  + '.csv', index=False, sep=';')
        print("Generate Done...")
    else:
        print("Veillez saisir un nombre entre 0 et 2")
        
"""
Function which analyse the dataset choosen by the user
"""
def AnalyseDataset(difficulte):
    if difficulte <= 2 and difficulte >= 0:
        #Create the data set
        NameDificulte = ["Difficile","Moyen","Facile"]
        lien = "csv//RediGenerate//" + NameDificulte[difficulte] + ".csv"
        df = rd.pd.read_csv(lien,sep=';')
        df = df[df['Temps'].notna()]
        nbRediAnalyse = len(df)
        df = df.dropna()
        nbRediAnalyseFinish = len(df)
        nbNaNFinish = nbRediAnalyse - nbRediAnalyseFinish
        TempMoyen = 0
        CoupMoyen = 0
        CoupMax = 0
        df = df[['Solution',"Temps"]]

        for i in range(len(df)):
            Coup = df.iloc[i].Solution.count('(')
            CoupMoyen += Coup
            
            Temps = df.iloc[i].Temps
            TempMoyen += Temps
            if(Coup > CoupMax):
                CoupMax = Coup
                
        CoupMoyen = CoupMoyen / nbRediAnalyseFinish
        TempMoyen = TempMoyen / nbRediAnalyseFinish
        return nbRediAnalyse, nbNaNFinish, CoupMax, CoupMoyen, TempMoyen
    else:
        print("Veillez saisir un nombre entre 0 et 2")