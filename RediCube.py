# Import lib
from Face import Face
import numpy as np
import pandas as pd
import random
import time


# Import Csv
Aretes=pd.read_csv('csv/Aretes.csv',sep=';')
Sommets=pd.read_csv('csv/Sommets.csv',sep=';')
Moves=pd.read_csv('csv/Moves.csv',sep=';')
correction_moves = pd.read_csv('csv/Correction_moves.csv',sep=';')
dfNeighbor = pd.read_csv('csv/FaceNeighbor.csv',sep=';')


#Constante
face = 6
listFaceCouleur = ['G','Y','R','W','O','B']
listEdge = [0,[0,1],[1,0],[1,2],[2,1]]
listAllCoup = [("up",1,-1), ("up",1,1), ("up",2,-1), ("up",2,1), ("up",3,-1), ("up",3,1), ("up",4,-1) , ("up",4,1), ("down",1,-1), ("down",1,1), ("down",2,-1), ("down",2,1), ("down",3,-1), ("down",3,1), ("down",4,-1) , ("down",4,1)]
ListCoinFace = [[("down",2,1),("down",1,1),("up",1,1),("up",2,1),("down",2,-1),("down",1,-1),("up",1,-1),("up",2,-1)], 
                [("down",2,1),("down",4,1),("up",1,1),("up",3,1),("down",2,-1),("down",4,-1),("up",1,-1),("up",3,-1)], 
                [("up",1,1),("up",2,1),("up",3,1),("up",4,1),("up",1,-1),("up",2,-1),("up",3,-1),("up",4,-1)],
                [("down",1,1),("down",3,1),("up",2,1),("up",4,1),("down",1,-1),("down",3,-1),("up",2,-1),("up",4,-1)],
                [("down",2,1),("down",1,1),("down",4,1),("down",3,1),("down",2,-1),("down",1,-1),("down",4,-1),("down",3,-1)],
                [("down",4,1),("down",3,1),("up",3,1),("up",4,1),("down",4,-1),("down",3,-1),("up",3,-1),("up",4,-1)]]

#Class and Function
class RediCube():
    #if matrice is not define, we return a fully 'finished' cube.
    # color code : R for red, W for white, O for orange, Y for yellow, G for green, B for blue
    def __init__(self,L=[]):
        cube = []
        self.faceprincipal = -1
        self.nbCoups = 0
        self.lastcoup = tuple()
        if L == [] :
            for c in listFaceCouleur:
                cube.append(Face(couleur=c))
            self.cube = cube
        else:
            self.cube = L

    '''
    Return a copy of a RediCube
    '''
    def Copy(self):
        r=RediCube()
        for i in range(face):
            for j in range(3):
                for k in range(3):
                    r.cube[i].tab[j][k] = self.cube[i].tab[j][k]
        r.lastcoup=self.lastcoup
        return r


    '''
    Override of ToString
    '''
    def __str__(self):
        res='     '
        l0=self.cube[0].__str__()
        res+=l0[0:3] + '\n     ' + l0[4:7] + '\n     ' + l0[8:11]

        l1 = self.cube[1].__str__()[0:3] + '  ' + self.cube[2].__str__()[0:3] + '  ' + self.cube[3].__str__()[0:3] + '  ' + self.cube[4].__str__()[0:3] + '  '
        l2 = self.cube[1].__str__()[4:7] + '  ' + self.cube[2].__str__()[4:7] + '  ' + self.cube[3].__str__()[4:7] + '  ' + self.cube[4].__str__()[4:7] + '  '
        l3 = self.cube[1].__str__()[8:11] + '  ' + self.cube[2].__str__()[8:11] + '  ' + self.cube[3].__str__()[8:11] + '  ' + self.cube[4].__str__()[8:11] + '  '

        res += '\n\n' + l1 + '\n' + l2 + '\n' + l3

        l4 = self.cube[5].__str__()
        res+= '\n\n     ' + l4[0:3] + '\n     ' + l4[4:7] + '\n     ' + l4[8:11]

        return res
    

    '''
    Return a Tuple of coordinate containing a row and columns with two parameters : angle(1:4), face(0:5)
    '''
    def CornerCoordonnees(self,numFace,numCorner):
        if numCorner == 1:
            sommet = (0,0)#ligne, colonne
            arreteHori = (0,1)
            arreteVert = (1,0)

        elif numCorner == 2:
            sommet = (0,2)
            arreteHori = (0,1)
            arreteVert = (1,2)

        elif numCorner == 3:
            sommet = (2,0)
            arreteHori = (2,1)
            arreteVert = (1,0)

        elif numCorner == 4:
            sommet = (2,2)
            arreteHori = (2,1)
            arreteVert = (1,2)

        return sommet,arreteHori,arreteVert
    
    
    def InversionArretes(self,numFace,arreteHori,arreteVert):
        self.cube[numFace].tab[arreteHori[0]][arreteHori[1]],self.cube[numFace].tab[arreteVert[0]][arreteVert[1]] = self.cube[numFace].tab[arreteVert[0]][arreteVert[1]],self.cube[numFace].tab[arreteHori[0]][arreteHori[1]]


    '''
    Its a procedure to perform a rotation of the RediCube
    parameters: numéro de chaque face(3), et numéro de chaque angle(3) concerné, sens de rotation
    Fonction qui ne renvoie rien, effectue le mouvement du RediCube, self.cube est modifié
    '''
    def RotationCorners(self,numFace1,numCorner1,numFace2,numCorner2,numFace3,numCorner3,hauteur,num,sens):
        sommet1,arreteHori1,arreteVert1 = self.CornerCoordonnees(numFace1,numCorner1)
        sommet2,arreteHori2,arreteVert2 = self.CornerCoordonnees(numFace2,numCorner2)
        sommet3,arreteHori3,arreteVert3 = self.CornerCoordonnees(numFace3,numCorner3)

        if sens == 1:#rotation sens horaire
            #translation des 3 sommets, s1,s2,s3 = s3,s1,s2
            self.cube[numFace1].tab[sommet1[0]][sommet1[1]],self.cube[numFace2].tab[sommet2[0]][sommet2[1]],self.cube[numFace3].tab[sommet3[0]][sommet3[1]] = self.cube[numFace3].tab[sommet3[0]][sommet3[1]],self.cube[numFace1].tab[sommet1[0]][sommet1[1]],self.cube[numFace2].tab[sommet2[0]][sommet2[1]]

            #translation et inversion arrete Horizontales/ arretes verticales
            #h1,v1, h2,v2, h3,v3, = v3,h3, v1,h1, v2,h2
            self.cube[numFace1].tab[arreteHori1[0]][arreteHori1[1]],self.cube[numFace1].tab[arreteVert1[0]][arreteVert1[1]],self.cube[numFace2].tab[arreteHori2[0]][arreteHori2[1]],self.cube[numFace2].tab[arreteVert2[0]][arreteVert2[1]],self.cube[numFace3].tab[arreteHori3[0]][arreteHori3[1]],self.cube[numFace3].tab[arreteVert3[0]][arreteVert3[1]] = self.cube[numFace3].tab[arreteVert3[0]][arreteVert3[1]],self.cube[numFace3].tab[arreteHori3[0]][arreteHori3[1]],self.cube[numFace1].tab[arreteVert1[0]][arreteVert1[1]],self.cube[numFace1].tab[arreteHori1[0]][arreteHori1[1]],self.cube[numFace2].tab[arreteVert2[0]][arreteVert2[1]],self.cube[numFace2].tab[arreteHori2[0]][arreteHori2[1]]

        elif sens == -1:#rotation anti-horaire
            #translation des 3 sommets, s1,s2,s3 = s2,s3,s1
            self.cube[numFace1].tab[sommet1[0]][sommet1[1]],self.cube[numFace2].tab[sommet2[0]][sommet2[1]],self.cube[numFace3].tab[sommet3[0]][sommet3[1]] = self.cube[numFace2].tab[sommet2[0]][sommet2[1]],self.cube[numFace3].tab[sommet3[0]][sommet3[1]],self.cube[numFace1].tab[sommet1[0]][sommet1[1]]

            #translation et inversion arrete Horizontales/ arretes verticales
            #h1,v1, h2,v2, h3,v3, = v2,h2, v3,h3, v1,h1
            self.cube[numFace1].tab[arreteHori1[0]][arreteHori1[1]],self.cube[numFace1].tab[arreteVert1[0]][arreteVert1[1]],self.cube[numFace2].tab[arreteHori2[0]][arreteHori2[1]],self.cube[numFace2].tab[arreteVert2[0]][arreteVert2[1]],self.cube[numFace3].tab[arreteHori3[0]][arreteHori3[1]],self.cube[numFace3].tab[arreteVert3[0]][arreteVert3[1]] = self.cube[numFace2].tab[arreteVert2[0]][arreteVert2[1]],self.cube[numFace2].tab[arreteHori2[0]][arreteHori2[1]],self.cube[numFace3].tab[arreteVert3[0]][arreteVert3[1]],self.cube[numFace3].tab[arreteHori3[0]][arreteHori3[1]],self.cube[numFace1].tab[arreteVert1[0]][arreteVert1[1]],self.cube[numFace1].tab[arreteHori1[0]][arreteHori1[1]]


        ###CORRECTION###
        #inversion arretes horizontale et verticale sur une face pour chaque mouvement
        numFaceCorrection = correction_moves[(correction_moves['hauteur']==hauteur) & (correction_moves['numero']==num) & (correction_moves['sens']==sens)]['numero de face'].to_list()[0]

        if numFaceCorrection == numFace1:
            self.InversionArretes(numFace1,arreteHori1,arreteVert1)
        elif numFaceCorrection == numFace2:
            self.InversionArretes(numFace2,arreteHori2,arreteVert2)
        else:
            self.InversionArretes(numFace3,arreteHori3,arreteVert3)

    '''
    Fonction qui effectue une rotation du RediCube
    parametres: hauteur du mouvement(up,down), numéro du mouvement(1:4), sens(1:horaire, -1:anti-horaire)
    Fonction qui ne renvoie rien, effectue le mouvement du RediCube, self.cube est modifié
    Fonction qui fais appelle à RotationCorners, convertie hauteur, num et sens en coordonnées pour la fonction RotationCorners
    Utilise le csv Moves pour la conversion
    '''
    def Move(self,hauteur,num,sens):
        [numFace1,numFace2,numFace3] = Moves[(Moves['hauteur']==hauteur) & (Moves['numero']==num)]['numero de face'].to_list()
        [numCorner1,numCorner2,numCorner3] = Moves[(Moves['hauteur']==hauteur) & (Moves['numero']==num)]['numero de corner'].to_list()

        self.RotationCorners(numFace1,numCorner1,numFace2,numCorner2,numFace3,numCorner3,hauteur,num,sens)
        self.lastcoup = (hauteur,num,sens)
        

    '''
    Fonction qui mélange le RediCube en prenant en paramètre le nombre de coup effectués pour le mélange
    Fonction qui ne renvoie rien, les mouvements sont effectués sur le RediCube, self.cube est modifié
    '''
    def Melange(self,nb,afficher=True):
        (NumMouv0,sens0) = (-1,2)
        for i in range(nb):
            NumMouv=random.randint(0,7)
            sens=random.randint(0,1)
            while (NumMouv==NumMouv0) and (sens!=sens0):
                NumMouv=random.randint(0,7)
                sens=random.randint(0,1)

            (NumMouv0,sens0) = (NumMouv,sens)

            if sens == 0:
                sens =-1
            Mouv=Moves.drop_duplicates(subset=['hauteur','numero']).iloc[NumMouv]
            if afficher==True:
                if sens == 1:
                    print('\nhauteur :',Mouv['hauteur'],', numéro de rotation: ',Mouv['numero'],', rotation sens horaire')
                else:
                    print('\nhauteur :',Mouv['hauteur'],', numéro de rotation :',Mouv['numero'],', rotation sens anti-horaire')
            self.Move(Mouv['hauteur'],Mouv['numero'],sens)
            

    '''
    Return the cost search of a RediCube
    '''
    def Recherche_cout(self,c_inf,c_max,melange_min=-1):
        compteur=0
        while((self.Cout() not in (range(c_inf,c_max+1))) or compteur<melange_min):
            compteur+=1
            self.Melange(1)


    '''
    Return the type : Corner or Edge
    '''
    def Type(self,ligne,colonne):
        if [ligne,colonne] in ([0,0],[0,2],[2,0],[2,2]):
            return 'sommet'
        return 'arrete'
    

    '''
    Return the movement and the high of a face and corner parameter
    '''
    def InverseMove(self,numFace,numCorner):
        hauteur = Moves[(Moves['numero de face']==numFace) & (Moves['numero de corner']==numCorner)]['hauteur'].tolist()[0]
        numMove = Moves[(Moves['numero de face']==numFace) & (Moves['numero de corner']==numCorner)]['numero'].tolist()[0]
        return hauteur,numMove

    '''
    Return the Cost of the RediCube
    '''
    def Cout(self):
        res=0
        for index,row in Aretes.iterrows():
            if (self.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']] == self.cube[row['Face1']].tab[row['Ligne1']][row['Colonne1']]) and (self.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']] == self.cube[row['Face2']].tab[row['Ligne2']][row['Colonne2']]):
                res+=2

        for index,row in Sommets.iterrows():
            if (self.cube[row['Face']].tab[row['Ligne']][row['Colonne']] == self.cube[row['Face']].tab[row['Ligne']][row['Colonne']]):
                res+=1
        return res


    '''
    List the edges of on face who are not placed
    '''
    def ListBadEdgeOnFace(self,numFace):
        edgeDone = []
        #for each edge
        for i in range(1,5):
            if(self.cube[numFace].tab[listEdge[i][0]][listEdge[i][1]] == self.cube[numFace].couleur):
                #Save the numface and the edge
                numFaceNeighbor = dfNeighbor[(dfNeighbor['face']==numFace) & (dfNeighbor['direction']==i)]['neighbor'].to_list()
                numEdge = dfNeighbor[(dfNeighbor['face']==numFace) & (dfNeighbor['direction']==i)]['edge'].to_list()
                #check the edge dependence
                if(self.cube[ numFaceNeighbor[0] ].tab[ listEdge[numEdge[0]][0] ][ listEdge[numEdge[0]][1] ] == self.cube[numFaceNeighbor[0]].couleur):
                    edgeDone.append(i)
    
        return list(set([1,2,3,4]) - set(edgeDone))
    
    '''
    Return boolean witch return the value of the principale face after checked it was finished
    '''
    def FirstCouronne(self):
        for i in range(face):
            color = self.cube[i].couleur
            goodface = [[color,color,color],[color,'X',color],[color,color,color]]
            if goodface == self.cube[i].tab:
                
                #We know of coin is good so we check edge 
                if len(self.ListBadEdgeOnFace(i)) == 0:
                    self.faceprincipal = i
            
            #We leave the function
            if(self.faceprincipal != -1):
                break
        return self.faceprincipal


#---------------------     EN COURS DE DEV PAR PIERRE    -------------------------------------
    '''
    Return the List of Coup
    '''
    def ListCoups(self):
        #ListCoupRestant = [i for i in listAllCoup]
        ListCoupDelete = []
        
        #Si premiere face resolu on bloque ses coins
        #if self.faceprincipal != -1:
            #ListCoupDelete = ListCoinFace[self.faceprincipal]
        #elif self.firstFaceFinish() == True:
            #print("Premiere face terminé !")    
            
        if self.lastcoup != ():
            #On empeche de revenir ou arriere ou de faire 2 fois le meme coup
            ListCoupDelete.append((self.lastcoup[0], self.lastcoup[1], -1))
            ListCoupDelete.append((self.lastcoup[0], self.lastcoup[1], 1))
        
        return list(set(listAllCoup) - set(ListCoupDelete))


    '''
    Return bool witch said if the first face is finished
    '''
    def firstFaceFinish(self):
        for i in face:
            print("Test");
            self.cube(i)
        return False;