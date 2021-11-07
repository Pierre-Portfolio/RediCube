##PAS FINI


import numpy as np
import random

#positions du cube concernees pour chaque mouvements possibles
angles={'up':{1:[[14,16,17],[21,24,25],[45,46,48]],2:[[23,25,26],[30,33,34],[46,47,50]],3:[[3,6,7],[18,19,21],[10,11,14]], 4:[[5,7,8],[27,28,30],[19,20,23]]},
'down':{1:[[12,15,16],[41,43,44],[48,51,52]],2:[[32,34,35],[39,42,43],[50,52,53]],3:[[0,1,3],[9,10,12],[37,38,41]], 4:[[1,2,5],[28,29,32],[36,37,39]]}}
#Pas encore range dans l'ordre por les down, dans le sens horaire de rotation de gauche à droite


class RediCube():
    def __init__(self,cube=0):
        #if matrice is not define, we return a fully 'finished' cube.
        # color code : R for red, W for white, O for orange, Y for yellow, G for green, B for blue
        if cube == 0 :
            cube = []
            for i in ('G','Y','R','W','O','B'):
                cube.append([[i,i,i],[i,'X',i],[i,i,i]])
        self.cube = cube

    def __str__(self):
        res=''
        res+='     '+self.cube[0][0][0]+self.cube[0][0][1]+self.cube[0][0][2]
        res+='\n'
        res+='     '+self.cube[0][1][0]+self.cube[0][1][1]+self.cube[0][1][2]
        res+='\n'
        res+='     '+self.cube[0][2][0]+self.cube[0][2][1]+self.cube[0][2][2]
        res+='\n'

        res+='\n'
        res+=self.cube[1][0][0]+self.cube[1][0][1]+self.cube[1][0][2] + '  '
        res+=self.cube[2][0][0]+self.cube[2][0][1]+self.cube[2][0][2] + '  '
        res+=self.cube[3][0][0]+self.cube[3][0][1]+self.cube[3][0][2] + '  '
        res+=self.cube[4][0][0]+self.cube[4][0][1]+self.cube[4][0][2] + '  '

        res+='\n'
        res+=self.cube[1][1][0]+self.cube[1][1][1]+self.cube[1][1][2] + '  '
        res+=self.cube[2][1][0]+self.cube[2][1][1]+self.cube[2][1][2] + '  '
        res+=self.cube[3][1][0]+self.cube[3][1][1]+self.cube[3][1][2] + '  '
        res+=self.cube[4][1][0]+self.cube[4][1][1]+self.cube[4][1][2] + '  '

        res+='\n'
        res+=self.cube[1][2][0]+self.cube[1][2][1]+self.cube[1][2][2] + '  '
        res+=self.cube[2][2][0]+self.cube[2][2][1]+self.cube[2][2][2] + '  '
        res+=self.cube[3][2][0]+self.cube[3][2][1]+self.cube[3][2][2] + '  '
        res+=self.cube[4][2][0]+self.cube[4][2][1]+self.cube[4][2][2] + '  '

        res+='\n\n'
        res+='     '+self.cube[5][0][0]+self.cube[5][0][1]+self.cube[5][0][2]
        res+='\n'
        res+='     '+self.cube[5][1][0]+self.cube[5][1][1]+self.cube[5][1][2]
        res+='\n'
        res+='     '+self.cube[5][2][0]+self.cube[5][2][1]+self.cube[5][2][2]
        res+='\n'

        return res

    def Copy(self):
        r=RediCube()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    r.cube[i][j][k] = self.cube[i][j][k]

        return r

    def Affichage_chiffres(self):
        x=0
        r=RediCube()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    r.cube[i][j][k] = ' ' +str(x) +' '
                    x+=1
        print(r)

    def Index_chiffres(self,index):
        x=0
        r=RediCube()
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    r.cube[i][j][k] = x

                    if x==index:
                        return {'face':i,'ligne':j,'colonne':k}

                    x+=1



    '''
    hauteur : up,down
    num : angle 1,2,3 ou 4
    sens : 1-sens horaire ou -1 sens antihoraire
    '''

    def Move(self,hauteur,num,sens):


        if hauteur == 'up':
            if num == 1:
                if sens == 1:

                    angle=angles['up'][1]#angle concerne
                    matrice_coordonnes=dict()#matrice qui contiendra les coordonnees de toutes les orientations de l'angle

                    for i in range(len(angle)):
                        for j in range(len(angle[0])):
                            matrice_coordonnes[angle[i][j]] = r.Index_chiffres(angle[i][j])#passage de la position a un chiffre au [face][ligne][colonne]

                    #print(d)
                    self.Echanges(matrice_coordonnes,sens)




                    #r.cube[d[3][face],d[3][ligne],d[3][colonne]],r.cube[d[3][face],d[3][ligne],d[3][colonne]],r.cube[d[3][face],d[3][ligne],d[3][colonne]]

    def Echanges(self,matrice_coordonnes,sens):
        if sens == 1:#sens horaire : rotation de gauche à droite
            keys = [i for i in matrice_coordonnes]

            self.cube[matrice_coordonnes[keys[0]]['face']][matrice_coordonnes[keys[0]]['ligne']][matrice_coordonnes[keys[0]]['colonne']],self.cube[matrice_coordonnes[keys[1]]['face']][matrice_coordonnes[keys[1]]['ligne']][matrice_coordonnes[keys[1]]['colonne']],self.cube[matrice_coordonnes[keys[2]]['face']][matrice_coordonnes[keys[2]]['ligne']][matrice_coordonnes[keys[2]]['colonne']],self.cube[matrice_coordonnes[keys[3]]['face']][matrice_coordonnes[keys[3]]['ligne']][matrice_coordonnes[keys[3]]['colonne']],self.cube[matrice_coordonnes[keys[4]]['face']][matrice_coordonnes[keys[4]]['ligne']][matrice_coordonnes[keys[4]]['colonne']],self.cube[matrice_coordonnes[keys[5]]['face']][matrice_coordonnes[keys[5]]['ligne']][matrice_coordonnes[keys[5]]['colonne']],self.cube[matrice_coordonnes[keys[6]]['face']][matrice_coordonnes[keys[6]]['ligne']][matrice_coordonnes[keys[6]]['colonne']],self.cube[matrice_coordonnes[keys[7]]['face']][matrice_coordonnes[keys[7]]['ligne']][matrice_coordonnes[keys[7]]['colonne']],self.cube[matrice_coordonnes[keys[8]]['face']][matrice_coordonnes[keys[8]]['ligne']][matrice_coordonnes[keys[8]]['colonne']]=self.cube[matrice_coordonnes[keys[6]]['face']][matrice_coordonnes[keys[6]]['ligne']][matrice_coordonnes[keys[6]]['colonne']],self.cube[matrice_coordonnes[keys[7]]['face']][matrice_coordonnes[keys[7]]['ligne']][matrice_coordonnes[keys[7]]['colonne']],self.cube[matrice_coordonnes[keys[8]]['face']][matrice_coordonnes[keys[8]]['ligne']][matrice_coordonnes[keys[8]]['colonne']],self.cube[matrice_coordonnes[keys[0]]['face']][matrice_coordonnes[keys[0]]['ligne']][matrice_coordonnes[keys[0]]['colonne']],self.cube[matrice_coordonnes[keys[1]]['face']][matrice_coordonnes[keys[1]]['ligne']][matrice_coordonnes[keys[1]]['colonne']],self.cube[matrice_coordonnes[keys[2]]['face']][matrice_coordonnes[keys[2]]['ligne']][matrice_coordonnes[keys[2]]['colonne']],self.cube[matrice_coordonnes[keys[3]]['face']][matrice_coordonnes[keys[3]]['ligne']][matrice_coordonnes[keys[3]]['colonne']],self.cube[matrice_coordonnes[keys[4]]['face']][matrice_coordonnes[keys[4]]['ligne']][matrice_coordonnes[keys[4]]['colonne']],self.cube[matrice_coordonnes[keys[5]]['face']][matrice_coordonnes[keys[5]]['ligne']][matrice_coordonnes[keys[5]]['colonne']]

        elif sens == -1:#sens antihoraire : rotation de doite à gauche



r=RediCube()
#print(r)
r.Move('up',1,1)
#print(r)
