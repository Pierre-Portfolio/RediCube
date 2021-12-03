def Visualisation(r):



def Couleur(variable):
    col={'G':vector(0,1,0),'Y':vector(1,1,0),'R':vector(1, 0, 0),'W':vector(1, 1, 1),'O':vector(1,0.6,0),'B':vector(0,0,1)}
    return col(r.cube[int(variable[1:2])].tab[int(variable[3:4])][int(variable[5:6])])
