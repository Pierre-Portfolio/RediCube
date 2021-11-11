class Face():
    def __init__(self,couleur=''):
        tab=[]
        if couleur != '':
            tab=[[couleur,couleur,couleur],[couleur,'X',couleur],[couleur,couleur,couleur]]

        self.tab = tab

    def __str__(self):
        res=''
        for i in range(3):
            res+='\n'
            for j in range(3):
                res+=self.tab[i][j]

        return res

class RediCube():
    def __init__(self,cube=[]):
        #if matrice is not define, we return a fully 'finished' cube.
        # color code : R for red, W for white, O for orange, Y for yellow, G for green, B for blue
        if cube == [] :
            for c in ('G','Y','R','W','O','B'):
                cube.append(Face(couleur=c))
        self.cube = cube

    def strFace(self,face):
        res=''
        for i in range(3):
            res+='\n'
            for j in range(3):
                res+=face.tab[i][j]
        return res



        def __str__(self):
            res='     '
            #res+=self.strFace(self.cube[0])
            #res+=self.strFace(self.cube[1])


            return res


r=RediCube()