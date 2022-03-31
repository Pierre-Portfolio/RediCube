"""
Class which creates a face of a redicube
One face is composed of three lists of 3 char corresponding to a color
"""
class Face():
    def __init__(self,couleur,tab=[]):
        self.couleur = couleur
        if tab == []:
            tab=[[couleur,couleur,couleur],[couleur,'X',couleur],[couleur,couleur,couleur]]
        self.tab = tab

    def __str__(self):
        res=''
        for i in range(3):
            if i == 1 or i == 2:
                res+='\n'
            for j in range(3):
                res+=self.tab[i][j]
        return res