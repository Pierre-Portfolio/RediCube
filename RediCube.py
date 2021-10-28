import numpy as np
import random


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


r=RediCube()