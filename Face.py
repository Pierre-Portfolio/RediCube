class Face():
    def __init__(self,couleur=''):
        tab=[]
        if couleur != '':
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