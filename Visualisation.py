# -*- coding: utf-8 -*-

#Imports de librairies
from vpython import *
import math as m
import RediCube as rd

def Couleur(r,variable):
    col={'G':vector(0,1,0),'Y':vector(1,1,0),'R':vector(1, 0, 0),'W':vector(1, 1, 1),'O':vector(1,0.2,0),'B':vector(0,0,1)}
    return col[r.cube[int(variable[1:2])].tab[int(variable[3:4])][int(variable[5:6])]]

def Visualisation(r):
    #Lumières
    distant_light(direction=vector(2,0,0), color=color.white)
    distant_light(direction=vector(-2,0,0), color=color.white)
    distant_light(direction=vector(0,2,0), color=color.white)
    distant_light(direction=vector(0,-2,0), color=color.white)
    distant_light(direction=vector(0,0,-2), color=color.white)
    distant_light(direction=vector(0,0,2), color=color.white)

    #Flèches
    ar_x=arrow(pos=vector(-4,0,0),axis=vector(1,0,0),color=color.red)
    ar_y=arrow(pos=vector(-4,0,0),axis=vector(0,1,0),color=color.green)
    ar_z=arrow(pos=vector(-4,0,0),axis=vector(0,0,1),color=color.blue)
    
    #Noms des axes
    text(text="x",pos=vector(-3,-0.1,0),height=.2)
    text(text="y",pos=vector(-4,1.1,0),height=.2)
    text(text="z",pos=vector(-4,-.1,1.2),height=.2,axis=vector(0,0,-1))

    #Visualisation du Redi Cube
                                                                #Sommets
                                                                #=======

    #######################################################################################################################################
    ############################################    FACE AVANT    #####################################################
    #######################################################################################################################################
    # Nommage:
    #typedecube: {'sommet','arête'}
    #orientation: {'gauche','haut','bas','droite'}
    #face: {'avant','arriere','milieud','milieug','haut','bas'}

    #facelignecolonneh
    #Constituants de la première cube à gauche en haut
    f2l0c2=pyramid(pos = vector(-1.5, 1, 0),size=vector(0.25,.9,.9),color = Couleur(r,'f2l0c2'))     #ROUGE (face gauche)
    f3l0c0=pyramid(pos = vector(-1, 1, 0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l0c0'))     #BLANC (face centrale)
    f3l0c0.rotate(angle=m.pi/2,axis=vector(0,1,0))
    f0l2c2=pyramid(pos = vector(-1,1.5,0),size=vector(0.25,.9,.9),color = Couleur(r,'f0l2c2'))          #VERT  (face haute)
    f0l2c2.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

    #Constituants de la première cube à droite en haut
    f4l0c0=pyramid(pos = vector(1.5, 1, 0),size=vector(0.25,.9,.9),color = Couleur(r,'f4l0c0'))     #ORANGE(face droite)
    f4l0c0.rotate(angle=m.pi,axis=vector(0,1,0))
    f3l0c2=pyramid(pos = vector(1,1,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l0c2'))          #BLANC (face centrale)
    f3l0c2.rotate(angle=m.pi/2,axis=vector(0,1,0))
    f0l0c2=pyramid(pos = vector(1,1.5,0),size=vector(0.25,.9,.9),color = Couleur(r,'f0l0c2'))          #VERT  (face haute)
    f0l0c2.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

    #Constituants de la première cube à gauche en bas
    f2l2c2=pyramid(pos = vector(-1.5, -1, 0),size=vector(0.25,.9,.9),color = Couleur(r,'f2l2c2'))     #ROUGE (face gauche)
    f3l2c0=pyramid(pos = vector(-1,-1,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l2c0'))          #BLANC (face centrale)
    f3l2c0.rotate(angle=m.pi/2,axis=vector(0,1,0))
    f5l0c2=pyramid(pos = vector(-1,-1.5,0),size=vector(0.25,.9,.9),color = Couleur(r,'f5l0c2'))          #BLEU  (face basse)
    f5l0c2.rotate(angle=m.pi/2,axis=vector(0,0,1))

    #Constituants de la première cube à droite en bas
    f4l2c0=pyramid(pos = vector(1.5, -1, 0),size=vector(0.25,.9,.9),color = Couleur(r,'f4l2c0'))     #ORANGE(face droite)
    f4l2c0.rotate(angle=m.pi,axis=vector(0,1,0))
    f3l2c2=pyramid(pos = vector(1,-1,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l2c2'))          #BLANC (face centrale)
    f3l2c2.rotate(angle=m.pi/2,axis=vector(0,1,0))
    f5l2c2=pyramid(pos = vector(1,-1.5,0),size=vector(0.25,.9,.9),color = Couleur(r,'f5l2c2'))          #BLEU  (face basse)
    f5l2c2.rotate(angle=m.pi/2,axis=vector(0,0,1))


    #######################################################################################################################################
    #############################################    FACE ARRIÈRE    ################################################
    #######################################################################################################################################

    #Constituants de la première cube à gauche en haut
    f2l0c0=pyramid(pos = vector(-1.5, 1, -2),size=vector(0.25,.9,.9),color = Couleur(r,'f2l0c0'))     #ROUGE (face gauche)
    f1l0c2=pyramid(pos = vector(-1, 1, -2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l0c2'))     #JAUNE (face centrale)
    f1l0c2.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
    f0l2c0=pyramid(pos = vector(-1,1.5,-2),size=vector(0.25,.9,.9),color = Couleur(r,'f0l2c0'))          #VERT  (face haute)
    f0l2c0.rotate(angle=3*m.pi/2,axis=vector(0,0,1))


    #Constituants de la première cube à droite en haut
    f4l0c2=pyramid(pos = vector(1.5, 1, -2),size=vector(0.25,.9,.9),color = Couleur(r,'f4l0c2'))     #ORANGE(face droite)
    f4l0c2.rotate(angle=m.pi,axis=vector(0,1,0))
    f1l0c0=pyramid(pos = vector(1,1,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l0c0'))          #JAUNE (face centrale)
    f1l0c0.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
    f0l0c0=pyramid(pos = vector(1,1.5,-2),size=vector(0.25,.9,.9),color = Couleur(r,'f0l0c0'))          #VERT  (face haute)
    f0l0c0.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

    #Constituants de la première cube à gauche en bas
    f2l2c0=pyramid(pos = vector(-1.5, -1, -2),size=vector(0.25,.9,.9),color = Couleur(r,'f2l2c0'))     #ROUGE (face gauche)
    f1l2c2=pyramid(pos = vector(-1,-1,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l2c2'))          #JAUNE (face centrale)
    f1l2c2.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
    f5l0c0=pyramid(pos = vector(-1,-1.5,-2),size=vector(0.25,.9,.9),color = Couleur(r,'f5l0c0'))          #BLEU  (face basse)
    f5l0c0.rotate(angle=m.pi/2,axis=vector(0,0,1))


    #Constituants de la première cube à droite en bas
    f4l2c2=pyramid(pos = vector(1.5, -1, -2),size=vector(0.25,.9,.9),color = Couleur(r,'f4l2c2'))     #ORANGE(face droite)
    f4l2c2.rotate(angle=m.pi,axis=vector(0,1,0))
    f1l2c0=pyramid(pos = vector(1,-1,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l2c0'))          #JAUNE (face centrale)
    f1l2c0.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
    f5l2c0=pyramid(pos = vector(1,-1.5,-2),size=vector(0.25,.9,.9),color = Couleur(r,'f5l2c0'))          #BLEU  (face basse)
    f5l2c0.rotate(angle=m.pi/2,axis=vector(0,0,1))



                                                                #Arêtes
                                                                #=======

    #######################################################################################################################################
    ############################################    FACE AVANT    #####################################################
    #######################################################################################################################################

    #Constituants de l'arête haute
    f3l0c1=pyramid(pos = vector(0,1,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l0c1'))          #BLANC (face centrale)
    f3l0c1.rotate(angle=m.pi/2,axis=vector(0,1,0))
    f0l1c2=pyramid(pos = vector(0,1.5,0),size=vector(0.25,.9,.9),color = Couleur(r,'f0l1c2'))          #VERT  (face haute)
    f0l1c2.rotate(angle=3*m.pi/2,axis=vector(0,0,1))
    f0l1c2.rotate(angle=m.pi/2,axis=vector(0,1,0))




    #Constituants de l'arête gauche
    f2l1c2=pyramid(pos = vector(-1.5, 0, 0),size=vector(0.25,.9,.9),color = Couleur(r,'f2l1c2'))     #ROUGE (face gauche)
    f3l1c0=pyramid(pos = vector(-1,0,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l1c0'))          #BLANC (face centrale)
    f3l1c0.rotate(angle=m.pi/2,axis=vector(0,1,0))



    #Constituants de l'arête droite
    f4l1c0=pyramid(pos = vector(1.5, 0, 0),size=vector(0.25,.9,.9),color = Couleur(r,'f4l1c0'))     #ORANGE(face droite)
    f4l1c0.rotate(angle=m.pi,axis=vector(0,1,0))
    f3l1c2=pyramid(pos = vector(1,0,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l1c2'))          #BLANC (face centrale)
    f3l1c2.rotate(angle=m.pi/2,axis=vector(0,1,0))




    #Constituants de l'arête basse
    f3l2c1=pyramid(pos = vector(0,-1,0.5),size=vector(0.25,.9,.9),color = Couleur(r,'f3l2c1'))          #BLANC (face centrale)
    f3l2c1.rotate(angle=m.pi/2,axis=vector(0,1,0))
    f5l1c2=pyramid(pos = vector(0,-1.5,0),size=vector(0.25,.9,.9),color = Couleur(r,'f5l1c2'))          #BLEU  (face basse)
    f5l1c2.rotate(angle=m.pi/2,axis=vector(0,0,1))
    f5l1c2.rotate(angle=m.pi/2,axis=vector(0,1,0))




    #######################################################################################################################################
    #############################################    FACE ARRIÈRE    ################################################
    #######################################################################################################################################

    #Constituants de l'arête haute
    f1l0c1=pyramid(pos = vector(0,1,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l0c1'))          #JAUNE (face centrale)
    f1l0c1.rotate(angle=-m.pi/2,axis=vector(0,1,0))
    f0l1c0=pyramid(pos = vector(0,1.5,-2),size=vector(0.25,.9,.9),color = Couleur(r,'f0l1c0'))          #VERT  (face haute)
    f0l1c0.rotate(angle=3*m.pi/2,axis=vector(0,0,1))
    f0l1c0.rotate(angle=m.pi/2,axis=vector(0,1,0))





    #Constituants de l'arête gauche
    f2l1c0=pyramid(pos = vector(-1.5, 0, -2),size=vector(0.25,.9,.9),color = Couleur(r,'f2l1c0'))     #ROUGE (face gauche)
    f1l1c2=pyramid(pos = vector(-1,0,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l1c2'))          #JAUNE (face centrale)
    f1l1c2.rotate(angle=-m.pi/2,axis=vector(0,1,0))



    #Constituants de l'arête droite
    f4l1c2=pyramid(pos = vector(1.5, 0, -2),size=vector(0.25,.9,.9),color = Couleur(r,'f4l1c2'))     #ORANGE(face droite)
    f4l1c2.rotate(angle=m.pi,axis=vector(0,1,0))
    f1l1c0=pyramid(pos = vector(1,0,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l1c0'))          #JAUNE (face centrale)
    f1l1c0.rotate(angle=-m.pi/2,axis=vector(0,1,0))




    #Constituants de l'arête basse
    f1l2c1=pyramid(pos = vector(0,-1,-2.5),size=vector(0.25,.9,.9),color = Couleur(r,'f1l2c1'))          #JAUNE (face centrale)
    f1l2c1.rotate(angle=-m.pi/2,axis=vector(0,1,0))
    f5l1c0=pyramid(pos = vector(0,-1.5,-2),size=vector(0.25,.9,.9),color = Couleur(r,'f5l1c0'))          #BLEU  (face basse)
    f5l1c0.rotate(angle=m.pi/2,axis=vector(0,0,1))
    f5l1c0.rotate(angle=m.pi/2,axis=vector(0,1,0))



    #######################################################################################################################################
    #############################################       MILIEU      ##################################################
    #######################################################################################################################################

    #Constituants de l'arête haut gauche
    f2l0c1=pyramid(pos = vector(-1.5,1,-1),size=vector(0.25,.9,.9),color = Couleur(r,'f2l0c1'))          #ROUGE (face centrale)
    f0l2c1=pyramid(pos = vector(-1,1.5,-1),size=vector(0.25,.9,.9),color = Couleur(r,'f0l2c1'))          #VERT  (face haute)
    f0l2c1.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

    #Constituants de l'arête bas gauche
    f2l2c1=pyramid(pos = vector(-1.5,-1,-1),size=vector(0.25,.9,.9),color = Couleur(r,'f2l2c1'))          #ROUGE (face centrale)
    f5l0c1=pyramid(pos = vector(-1,-1.5,-1),size=vector(0.25,.9,.9),color = Couleur(r,'f5l0c1'))          #BLEU  (face basse)
    f5l0c1.rotate(angle=m.pi/2,axis=vector(0,0,1))



    #Constituants de l'arête haut droite
    f4l0c1=pyramid(pos = vector(1.5, 1, -1),size=vector(0.25,.9,.9),color = Couleur(r,'f4l0c1'))     #ORANGE(face droite)
    f4l0c1.rotate(angle=m.pi,axis=vector(0,1,0))
    f0l0c1=pyramid(pos = vector(1,1.5,-1),size=vector(0.25,.9,.9),color = Couleur(r,'f0l0c1'))          #VERT  (face haute)
    f0l0c1.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

    #Constituants de l'arête bas droite
    f4l2c1=pyramid(pos = vector(1.5, -1, -1),size=vector(0.25,.9,.9),color = Couleur(r,'f4l2c1'))     #ORANGE(face droite)
    f4l2c1.rotate(angle=m.pi,axis=vector(0,1,0))
    f5l2c1=pyramid(pos = vector(1,-1.5,-1),size=vector(0.25,.9,.9),color = Couleur(r,'f5l2c1'))          #BLEU  (face basse)
    f5l2c1.rotate(angle=m.pi/2,axis=vector(0,0,1))


    #Triangles

    a1=vertex(pos=vector(-0.45,.55,0.5),color=Couleur(r,'f3l0c1'))
    a2=vertex(pos=vector(0.45,.55,0.5),color=Couleur(r,'f3l0c1'))
    a3=vertex(pos=vector(0,0.1,0.5),color=Couleur(r,'f3l0c1'))
    tf3l0c1=triangle(v0=a1,v1=a2,v2=a3)

    b1=vertex(pos=vector(-0.55,.45,0.5),color=Couleur(r,'f3l1c0'))
    b2=vertex(pos=vector(-0.55,-.45,0.5),color=Couleur(r,'f3l1c0'))
    b3=vertex(pos=vector(-0.1,0,0.5),color=Couleur(r,'f3l1c0'))
    tf3l1c0=triangle(v0=b1,v1=b2,v2=b3)


    c1=vertex(pos=vector(0.55,.45,0.5),color=Couleur(r,'f3l1c2'))
    c2=vertex(pos=vector(0.55,-.45,0.5),color=Couleur(r,'f3l1c2'))
    c3=vertex(pos=vector(0.1,0,0.5),color=Couleur(r,'f3l1c2'))
    tf3l1c2=triangle(v0=c1,v1=c2,v2=c3)

    d1=vertex(pos=vector(-0.45,-.55,0.5),color=Couleur(r,'f3l2c1'))
    d2=vertex(pos=vector(0.45,-.55,0.5),color=Couleur(r,'f3l2c1'))
    d3=vertex(pos=vector(0,-0.1,0.5),color=Couleur(r,'f3l2c1'))
    tf3l2c1=triangle(v0=d1,v1=d2,v2=d3)

    e1=vertex(pos=vector(-0.45,.55,-2.5),color=Couleur(r,'f1l0c1'))
    e2=vertex(pos=vector(0.45,.55,-2.5),color=Couleur(r,'f1l0c1'))
    e3=vertex(pos=vector(0,0.1,-2.5),color=Couleur(r,'f1l0c1'))
    tf1l0c1=triangle(v0=e1,v1=e2,v2=e3)

    f1=vertex(pos=vector(-0.55,.45,-2.5),color=Couleur(r,'f1l1c2'))
    f2=vertex(pos=vector(-0.55,-.45,-2.5),color=Couleur(r,'f1l1c2'))
    f3=vertex(pos=vector(-0.1,0,-2.5),color=Couleur(r,'f1l1c2'))
    tf1l1c2=triangle(v0=f1,v1=f2,v2=f3)


    g1=vertex(pos=vector(0.55,.45,-2.5),color=Couleur(r,'f1l1c0'))
    g2=vertex(pos=vector(0.55,-.45,-2.5),color=Couleur(r,'f1l1c0'))
    g3=vertex(pos=vector(0.1,0,-2.5),color=Couleur(r,'f1l1c0'))
    tf1l1c0=triangle(v0=g1,v1=g2,v2=g3)

    h1=vertex(pos=vector(-0.45,-.55,-2.5),color=Couleur(r,'f1l2c1'))
    h2=vertex(pos=vector(0.45,-.55,-2.5),color=Couleur(r,'f1l2c1'))
    h3=vertex(pos=vector(0,-0.1,-2.5),color=Couleur(r,'f1l2c1'))
    tf1l2c1=triangle(v0=h1,v1=h2,v2=h3)


    #Gauche
    ga1=vertex(pos=vector(-1.5,.55,-1.45),color=Couleur(r,'f2l0c1'))
    ga2=vertex(pos=vector(-1.5,.55,-0.55),color=Couleur(r,'f2l0c1'))
    ga3=vertex(pos=vector(-1.5,0.1,-1),color=Couleur(r,'f2l0c1'))
    tf2l0c1=triangle(v0=ga1,v1=ga2,v2=ga3)

    gba1=vertex(pos=vector(-1.5,-.55,-1.45),color=Couleur(r,'f2c2c1'))
    gba2=vertex(pos=vector(-1.5,-.55,-0.55),color=Couleur(r,'f2c2c1'))
    gba3=vertex(pos=vector(-1.5,-0.1,-1),color=Couleur(r,'f2c2c1'))
    tf2c2c1=triangle(v0=gba1,v1=gba2,v2=gba3)

    gg1=vertex(pos=vector(-1.5,.45,-1.6),color=Couleur(r,'f2l1c0'))
    gg2=vertex(pos=vector(-1.5,-.45,-1.6),color=Couleur(r,'f2l1c0'))
    gg3=vertex(pos=vector(-1.5,0,-1.1),color=Couleur(r,'f2l1c0'))
    tf2l1c0=triangle(v0=gg1,v1=gg2,v2=gg3)

    gd1=vertex(pos=vector(-1.5,.45,-0.4),color=Couleur(r,'f2l1c2'))
    gd2=vertex(pos=vector(-1.5,-.45,-0.4),color=Couleur(r,'f2l1c2'))
    gd3=vertex(pos=vector(-1.5,0,-.9),color=Couleur(r,'f2l1c2'))
    tf2l1c2=triangle(v0=gd1,v1=gd2,v2=gd3)

    #Droite
    da1=vertex(pos=vector(1.5,.55,-1.45),color = Couleur(r,'f4l0c1'))
    da2=vertex(pos=vector(1.5,.55,-0.55),color = Couleur(r,'f4l0c1'))
    da3=vertex(pos=vector(1.5,0.1,-1),color = Couleur(r,'f4l0c1'))
    tf4l0c1=triangle(v0=da1,v1=da2,v2=da3)

    dba1=vertex(pos=vector(1.5,-.55,-1.45),color = Couleur(r,'f4l2c1'))
    dba2=vertex(pos=vector(1.5,-.55,-0.55),color = Couleur(r,'f4l2c1'))
    dba3=vertex(pos=vector(1.5,-0.1,-1),color = Couleur(r,'f4l2c1'))
    tf4l2c1=triangle(v0=dba1,v1=dba2,v2=dba3)

    dg1=vertex(pos=vector(1.5,.45,-1.6),color = Couleur(r,'f4l1c2'))
    dg2=vertex(pos=vector(1.5,-.45,-1.6),color = Couleur(r,'f4l1c2'))
    dg3=vertex(pos=vector(1.5,0,-1.1),color = Couleur(r,'f4l1c2'))
    tf4l1c2=triangle(v0=dg1,v1=dg2,v2=dg3)

    dd1=vertex(pos=vector(1.5,.45,-0.4),color = Couleur(r,'f4l1c0'))
    dd2=vertex(pos=vector(1.5,-.45,-0.4),color = Couleur(r,'f4l1c0'))
    dd3=vertex(pos=vector(1.5,0,-.9),color = Couleur(r,'f4l1c0'))
    tf4l1c0=triangle(v0=dd1,v1=dd2,v2=dd3)

    #Haut
    hha1=vertex(pos=vector(-.45,1.5,-1.6),color = Couleur(r,'f0l1c0'))
    hha2=vertex(pos=vector(0.45,1.5,-1.6),color = Couleur(r,'f0l1c0'))
    hha3=vertex(pos=vector(0,1.5,-1.1),color = Couleur(r,'f0l1c0'))
    tf0l1c0=triangle(v0=hha1,v1=hha2,v2=hha3)

    hba1=vertex(pos=vector(-.45,1.5,-.4),color = Couleur(r,'f0l1c2'))
    hba2=vertex(pos=vector(0.45,1.5,-.4),color = Couleur(r,'f0l1c2'))
    hba3=vertex(pos=vector(0,1.5,-.9),color = Couleur(r,'f0l1c2'))
    tf0l1c2=triangle(v0=hba1,v1=hba2,v2=hba3)

    hga1=vertex(pos=vector(-.55,1.5,-.55),color = Couleur(r,'f0l2c1'))
    hga2=vertex(pos=vector(-.55,1.5,-1.45),color = Couleur(r,'f0l2c1'))
    hga3=vertex(pos=vector(-.1,1.5,-1),color = Couleur(r,'f0l2c1'))
    tf0l2c1=triangle(v0=hga1,v1=hga2,v2=hga3)

    hda1=vertex(pos=vector(.55,1.5,-.55),color = Couleur(r,'f0l0c1'))
    hda2=vertex(pos=vector(.55,1.5,-1.45),color = Couleur(r,'f0l0c1'))
    hda3=vertex(pos=vector(.1,1.5,-1),color = Couleur(r,'f0l0c1'))
    tf0l0c1=triangle(v0=hda1,v1=hda2,v2=hda3)

    #Bas
    bha1=vertex(pos=vector(-.45,-1.5,-1.6),color = Couleur(r,'f5l1c0'))
    bha2=vertex(pos=vector(0.45,-1.5,-1.6),color = Couleur(r,'f5l1c0'))
    bha3=vertex(pos=vector(0,-1.5,-1.1),color = Couleur(r,'f5l1c0'))
    tf5l1c0=triangle(v0=bha1,v1=bha2,v2=bha3)

    bba1=vertex(pos=vector(-.45,-1.5,-.4),color = Couleur(r,'f5l1c2'))
    bba2=vertex(pos=vector(0.45,-1.5,-.4),color = Couleur(r,'f5l1c2'))
    bba3=vertex(pos=vector(0,-1.5,-.9),color = Couleur(r,'f5l1c2'))
    tf5l1c2=triangle(v0=bba1,v1=bba2,v2=bba3)

    bga1=vertex(pos=vector(-.55,-1.5,-.55),color = Couleur(r,'f5l0c1'))
    bga2=vertex(pos=vector(-.55,-1.5,-1.45),color = Couleur(r,'f5l0c1'))
    bga3=vertex(pos=vector(-.1,-1.5,-1),color = Couleur(r,'f5l0c1'))
    tf5l0c1=triangle(v0=bga1,v1=bga2,v2=bga3)

    bda1=vertex(pos=vector(.55,-1.5,-.55),color = Couleur(r,'f5l2c1'))
    bda2=vertex(pos=vector(.55,-1.5,-1.45),color = Couleur(r,'f5l2c1'))
    bda3=vertex(pos=vector(.1,-1.5,-1),color = Couleur(r,'f5l2c1'))
    tf5l2c1=triangle(v0=bda1,v1=bda2,v2=bda3)
    
    my_label=label()
    def B(d):
        print("The button said this: ", d.text)
    def C(d):
        print("The button said this: ", d.text)
    def D(wi):
        print("The button said this: ", d.text)
    wtext(text="\n\n")
    winput(width=600,bind=D)
    wtext(text="\n\n                                        ")
    button( bind=B, text='Valider' )
    wtext(text="            ")
    button(bind=C ,text="Résoudre")
    
    
