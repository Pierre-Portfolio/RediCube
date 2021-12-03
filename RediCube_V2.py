import numpy as np
import pandas as pd
import random as rd
import time
from Face import Face

Moves=pd.read_csv('Moves.csv',sep=';')

class RediCube():
    def __init__(self,L=[]):
        #if matrice is not define, we return a fully 'finished' cube.
        # color code : R for red, W for white, O for orange, Y for yellow, G for green, B for blue
        cube = []
        if L == [] :
            for c in ('G','Y','R','W','O','B'):
                cube.append(Face(couleur=c))
            self.cube = cube

        else:
            self.cube = L

    def Copy(self):
        r=RediCube()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    r.cube[i].tab[j][k] = self.cube[i].tab[j][k]

        return r


    def __str__(self):
        res='     '
        l0=self.cube[0].__str__()
        res+=l0[0:3] + '\n     ' + l0[4:7] + '\n     ' + l0[8:11]


        r1=self.Copy()
        r1.cube[1].tab=np.array(r1.cube[1].tab)#matrice
        r1.cube[1].tab=r1.cube[1].tab.T#transposee matrice
        r1.cube[1].tab=np.fliplr(r1.cube[1].tab)#inversion 1ere et derniere ligne


        r3=self.Copy()
        r3.cube[3].tab=np.array(r3.cube[3].tab)
        r3.cube[3].tab=r3.cube[3].tab.T
        r3.cube[3].tab=np.flipud(r3.cube[3].tab)#inversion 1ere et derniere colonne




        l1 = r1.cube[1].__str__()[0:3] + '  ' + self.cube[2].__str__()[0:3] + '  ' + r3.cube[3].__str__()[0:3] + '  ' + self.cube[4].__str__()[0:3] + '  '

        l2 = r1.cube[1].__str__()[4:7] + '  ' + self.cube[2].__str__()[4:7] + '  ' + r3.cube[3].__str__()[4:7] + '  ' + self.cube[4].__str__()[4:7] + '  '

        l3 = r1.cube[1].__str__()[8:11] + '  ' + self.cube[2].__str__()[8:11] + '  ' + r3.cube[3].__str__()[8:11] + '  ' + self.cube[4].__str__()[8:11] + '  '



        res += '\n\n' + l1 + '\n' + l2 + '\n' + l3

        l4 = self.cube[5].__str__()
        res+= '\n\n     ' + l4[0:3] + '\n     ' + l4[4:7] + '\n     ' + l4[8:11]



        return res


    def Affichage_chiffres(self):
        x=0
        r=RediCube()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    r.cube[i].tab[j][k] = str(x)
                    x+=1
        return r

    def Corner(self,numFace,numCorner):
        if numCorner == 1:
            sommet = self.cube[numFace].tab[0][0]
            arreteHori = self.cube[numFace].tab[0][1]
            arreteVert = self.cube[numFace].tab[1][0]

        elif numCorner == 2:
            sommet = self.cube[numFace].tab[0][2]
            arreteHori = self.cube[numFace].tab[0][1]
            arreteVert = self.cube[numFace].tab[1][2]

        elif numCorner == 3:
            sommet = self.cube[numFace].tab[2][0]
            arreteHori = self.cube[numFace].tab[2][1]
            arreteVert = self.cube[numFace].tab[1][0]

        elif numCorner == 4:
            sommet = self.cube[numFace].tab[2][2]
            arreteHori = self.cube[numFace].tab[2][1]
            arreteVert = self.cube[numFace].tab[1][2]

        return sommet,arreteHori,arreteVert

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

    def RotationCorners(self,numFace1,numCorner1,numFace2,numCorner2,numFace3,numCorner3,sens):
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




    def Move(self,hauteur,num,sens):
        [numFace1,numFace2,numFace3] = Moves[(Moves['hauteur']==hauteur) & (Moves['numero']==num)]['numero de face'].to_list()
        [numCorner1,numCorner2,numCorner3] = Moves[(Moves['hauteur']==hauteur) & (Moves['numero']==num)]['numero de corner'].to_list()

        self.RotationCorners(numFace1,numCorner1,numFace2,numCorner2,numFace3,numCorner3,sens)

        #print([numFace1,numFace2,numFace3])
        #print([numCorner1,numCorner2,numCorner3])

        print('\n')
        print(self)

    def Melange(self,nb):
        for i in range(nb):
            NumMouv=rd.randint(0,7)
            sens=rd.randint(0,1)
            if sens == 0:
                sens =-1
            Mouv=Moves.drop_duplicates(subset=['hauteur','numero']).iloc[NumMouv]
            if sens == 1:
                print('\nhauteur :',Mouv['hauteur'],', numéro de rotation: ',Mouv['numero'],', rotation sens horaire')
            else:
                print('\nhauteur :',Mouv['hauteur'],', numéro de rotation :',Mouv['numero'],', rotation sens anti-horaire')

            time.sleep(1)
            self.Move(Mouv['hauteur'],Mouv['numero'],sens)



r=RediCube()
#r.Move('up',1,1)
print(r)