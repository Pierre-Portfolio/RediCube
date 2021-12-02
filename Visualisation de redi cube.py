# -*- coding: utf-8 -*-

#Imports de librairies
from vpython import * 
import math as m

#Visualisation du Redi Cube
                                                            #Sommets
                                                            #=======

#######################################################################################################################################
############################################    FACE AVANT    #####################################################
#######################################################################################################################################

#Constituants de la première cube à gauche en haut
avpyrgh1=pyramid(pos = vector(-1.5, 1, 0),size=vector(0.25,.9,.9),color = vector(1, 0, 0))     #ROUGE (face gauche)
avpyrgh2=pyramid(pos = vector(-1, 1, 0.5),size=vector(0.25,.9,.9),color = vector(1, 1, 1))     #BLANC (face centrale)
avpyrgh2.rotate(angle=m.pi/2,axis=vector(0,1,0))
avpyrgh3=pyramid(pos = vector(-1,1.5,0),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
avpyrgh3.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

#Constituants de la première cube à droite en haut
avpyrdh1=pyramid(pos = vector(1.5, 1, 0),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
avpyrdh1.rotate(angle=m.pi,axis=vector(0,1,0))
avpyrdh2=pyramid(pos = vector(1,1,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
avpyrdh2.rotate(angle=m.pi/2,axis=vector(0,1,0))
avpyrdh3=pyramid(pos = vector(1,1.5,0),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
avpyrdh3.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

#Constituants de la première cube à gauche en bas
avpyrgb1=pyramid(pos = vector(-1.5, -1, 0),size=vector(0.25,.9,.9),color = vector(1, 0, 0))     #ROUGE (face gauche)
avpyrgb2=pyramid(pos = vector(-1,-1,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
avpyrgb2.rotate(angle=m.pi/2,axis=vector(0,1,0))
avpyrgb3=pyramid(pos = vector(-1,-1.5,0),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
avpyrgb3.rotate(angle=m.pi/2,axis=vector(0,0,1))

#Constituants de la première cube à droite en bas
avpyrdb1=pyramid(pos = vector(1.5, -1, 0),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
avpyrdb1.rotate(angle=m.pi,axis=vector(0,1,0))
avpyrdb2=pyramid(pos = vector(1,-1,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
avpyrdb2.rotate(angle=m.pi/2,axis=vector(0,1,0))
avpyrdb3=pyramid(pos = vector(1,-1.5,0),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
avpyrdb3.rotate(angle=m.pi/2,axis=vector(0,0,1))


#######################################################################################################################################
#############################################    FACE ARRIÈRE    ################################################
#######################################################################################################################################

#Constituants de la première cube à gauche en haut
arpyrgh1=pyramid(pos = vector(-1.5, 1, -2),size=vector(0.25,.9,.9),color = vector(1, 0, 0))     #ROUGE (face gauche)
arpyrgh2=pyramid(pos = vector(-1, 1, -2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))     #JAUNE (face centrale)
arpyrgh2.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
arpyrgh3=pyramid(pos = vector(-1,1.5,-2),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
arpyrgh3.rotate(angle=3*m.pi/2,axis=vector(0,0,1))


#Constituants de la première cube à droite en haut
arpyrdh1=pyramid(pos = vector(1.5, 1, -2),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
arpyrdh1.rotate(angle=m.pi,axis=vector(0,1,0))
arpyrdh2=pyramid(pos = vector(1,1,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
arpyrdh2.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
arpyrdh3=pyramid(pos = vector(1,1.5,-2),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
arpyrdh3.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

#Constituants de la première cube à gauche en bas
arpyrgb1=pyramid(pos = vector(-1.5, -1, -2),size=vector(0.25,.9,.9),color = vector(1, 0, 0))     #ROUGE (face gauche)
arpyrgb2=pyramid(pos = vector(-1,-1,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
arpyrgb2.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
arpyrgb3=pyramid(pos = vector(-1,-1.5,-2),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
arpyrgb3.rotate(angle=m.pi/2,axis=vector(0,0,1))


#Constituants de la première cube à droite en bas
arpyrdb1=pyramid(pos = vector(1.5, -1, -2),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
arpyrdb1.rotate(angle=m.pi,axis=vector(0,1,0))
arpyrdb2=pyramid(pos = vector(1,-1,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
arpyrdb2.rotate(angle=3*m.pi/2,axis=vector(0,1,0))
arpyrdb3=pyramid(pos = vector(1,-1.5,-2),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
arpyrdb3.rotate(angle=m.pi/2,axis=vector(0,0,1))



                                                            #Arêtes
                                                            #=======

#######################################################################################################################################
############################################    FACE AVANT    #####################################################
#######################################################################################################################################

#Constituants de l'arête haute
aretepyrhblanc=pyramid(pos = vector(0,1,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
aretepyrhblanc.rotate(angle=m.pi/2,axis=vector(0,1,0))
aretepyrhvert=pyramid(pos = vector(0,1.5,0),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
aretepyrhvert.rotate(angle=3*m.pi/2,axis=vector(0,0,1))
aretepyrhvert.rotate(angle=m.pi/2,axis=vector(0,1,0))
a1=vertex(pos=vector(-0.45,.55,0.5))
a2=vertex(pos=vector(0.45,.55,0.5))
a3=vertex(pos=vector(0,0.1,0.5))
ta1=triangle(v0=a1,v1=a2,v2=a3)

#Constituants de l'arête gauche 
aretepyrrougegauche=pyramid(pos = vector(-1.5, 0, 0),size=vector(0.25,.9,.9),color = vector(1, 0, 0))     #ROUGE (face gauche)
aretepyrblancgauche=pyramid(pos = vector(-1,0,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
aretepyrblancgauche.rotate(angle=m.pi/2,axis=vector(0,1,0))
b1=vertex(pos=vector(-0.55,.45,0.5))
b2=vertex(pos=vector(-0.55,-.45,0.5))
b3=vertex(pos=vector(-0.1,0,0.5))
tb1=triangle(v0=b1,v1=b2,v2=b3)

#Constituants de l'arête droite
aretepyrorangedroite=pyramid(pos = vector(1.5, 0, 0),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
aretepyrorangedroite.rotate(angle=m.pi,axis=vector(0,1,0))
aretepyrblancdroite=pyramid(pos = vector(1,0,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
aretepyrblancdroite.rotate(angle=m.pi/2,axis=vector(0,1,0))
c1=vertex(pos=vector(0.55,.45,0.5))
c2=vertex(pos=vector(0.55,-.45,0.5))
c3=vertex(pos=vector(0.1,0,0.5))
tc1=triangle(v0=c1,v1=c2,v2=c3)

#Constituants de l'arête basse
aretepyrbblanc=pyramid(pos = vector(0,-1,0.5),size=vector(0.25,.9,.9),color = vector(1,1,1))          #BLANC (face centrale)
aretepyrbblanc.rotate(angle=m.pi/2,axis=vector(0,1,0))
aretepyrbbleu=pyramid(pos = vector(0,-1.5,0),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
aretepyrbbleu.rotate(angle=m.pi/2,axis=vector(0,0,1))
aretepyrbbleu.rotate(angle=m.pi/2,axis=vector(0,1,0))
d1=vertex(pos=vector(-0.45,-.55,0.5))
d2=vertex(pos=vector(0.45,-.55,0.5))
d3=vertex(pos=vector(0,-0.1,0.5))
td1=triangle(v0=d1,v1=d2,v2=d3)

#######################################################################################################################################
#############################################    FACE ARRIÈRE    ################################################
#######################################################################################################################################

#Constituants de l'arête haute
araretejauneh=pyramid(pos = vector(0,1,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
araretejauneh.rotate(angle=-m.pi/2,axis=vector(0,1,0))
araretepyrhvert=pyramid(pos = vector(0,1.5,-2),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
araretepyrhvert.rotate(angle=3*m.pi/2,axis=vector(0,0,1))
araretepyrhvert.rotate(angle=m.pi/2,axis=vector(0,1,0))
e1=vertex(pos=vector(-0.45,.55,-2.5),color=vector(1,1,0))
e2=vertex(pos=vector(0.45,.55,-2.5),color=vector(1,1,0))
e3=vertex(pos=vector(0,0.1,-2.5),color=vector(1,1,0))
te1=triangle(v0=e1,v1=e2,v2=e3)


#Constituants de l'arête gauche 
araretepyrrougeg=pyramid(pos = vector(-1.5, 0, -2),size=vector(0.25,.9,.9),color = vector(1, 0, 0))     #ROUGE (face gauche)
araretepyrjauneg=pyramid(pos = vector(-1,0,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
araretepyrjauneg.rotate(angle=-m.pi/2,axis=vector(0,1,0))
f1=vertex(pos=vector(-0.55,.45,-2.5),color=vector(1,1,0))
f2=vertex(pos=vector(-0.55,-.45,-2.5),color=vector(1,1,0))
f3=vertex(pos=vector(-0.1,0,-2.5),color=vector(1,1,0))
tf1=triangle(v0=f1,v1=f2,v2=f3)

#Constituants de l'arête droite
araretepyroranged=pyramid(pos = vector(1.5, 0, -2),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
araretepyroranged.rotate(angle=m.pi,axis=vector(0,1,0))
araretepyrjauned=pyramid(pos = vector(1,0,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
araretepyrjauned.rotate(angle=-m.pi/2,axis=vector(0,1,0))
g1=vertex(pos=vector(0.55,.45,-2.5),color=vector(1,1,0))
g2=vertex(pos=vector(0.55,-.45,-2.5),color=vector(1,1,0))
g3=vertex(pos=vector(0.1,0,-2.5),color=vector(1,1,0))
tg1=triangle(v0=g1,v1=g2,v2=g3)

#Constituants de l'arête basse
araretepyrbjaune=pyramid(pos = vector(0,-1,-2.5),size=vector(0.25,.9,.9),color = vector(1,1,0))          #JAUNE (face centrale)
araretepyrbjaune.rotate(angle=-m.pi/2,axis=vector(0,1,0))
araretepyrbbleu=pyramid(pos = vector(0,-1.5,-2),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
araretepyrbbleu.rotate(angle=m.pi/2,axis=vector(0,0,1))
araretepyrbbleu.rotate(angle=m.pi/2,axis=vector(0,1,0))
h1=vertex(pos=vector(-0.45,-.55,-2.5),color=vector(1,1,0))
h2=vertex(pos=vector(0.45,-.55,-2.5),color=vector(1,1,0))
h3=vertex(pos=vector(0,-0.1,-2.5),color=vector(1,1,0))
th1=triangle(v0=h1,v1=h2,v2=h3)

#######################################################################################################################################
#############################################       MILIEU      ##################################################
#######################################################################################################################################

#Constituants de l'arête haut gauche
amhg=pyramid(pos = vector(-1.5,1,-1),size=vector(0.25,.9,.9),color = vector(1,0,0))          #ROUGE (face centrale)
amhgvert=pyramid(pos = vector(-1,1.5,-1),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
amhgvert.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

#Constituants de l'arête bas gauche
ambg=pyramid(pos = vector(-1.5,-1,-1),size=vector(0.25,.9,.9),color = vector(1,0,0))          #ROUGE (face centrale)
ambgbleu=pyramid(pos = vector(-1,-1.5,-1),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
ambgbleu.rotate(angle=m.pi/2,axis=vector(0,0,1))



#Constituants de l'arête haut droite
amhd=pyramid(pos = vector(1.5, 1, -1),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
amhd.rotate(angle=m.pi,axis=vector(0,1,0))
amhdvert=pyramid(pos = vector(1,1.5,-1),size=vector(0.25,.9,.9),color = vector(0,1,0))          #VERT  (face haute)
amhdvert.rotate(angle=3*m.pi/2,axis=vector(0,0,1))

#Constituants de l'arête bas droite
ambd=pyramid(pos = vector(1.5, -1, -1),size=vector(0.25,.9,.9),color = vector(1,0.6,0))     #ORANGE(face droite)
ambd.rotate(angle=m.pi,axis=vector(0,1,0))
ambdbleu=pyramid(pos = vector(1,-1.5,-1),size=vector(0.25,.9,.9),color = vector(0,0,1))          #BLEU  (face basse)
ambdbleu.rotate(angle=m.pi/2,axis=vector(0,0,1))


#Triangles

#Gauche
ga1=vertex(pos=vector(-1.5,.55,-1.45),color=vector(1,0,0))
ga2=vertex(pos=vector(-1.5,.55,-0.55),color=vector(1,0,0))
ga3=vertex(pos=vector(-1.5,0.1,-1),color=vector(1,0,0))
tga1=triangle(v0=ga1,v1=ga2,v2=ga3)

gba1=vertex(pos=vector(-1.5,-.55,-1.45),color=vector(1,0,0))
gba2=vertex(pos=vector(-1.5,-.55,-0.55),color=vector(1,0,0))
gba3=vertex(pos=vector(-1.5,-0.1,-1),color=vector(1,0,0))
tgba1=triangle(v0=gba1,v1=gba2,v2=gba3)

gg1=vertex(pos=vector(-1.5,.45,-1.6),color=vector(1,0,0))
gg2=vertex(pos=vector(-1.5,-.45,-1.6),color=vector(1,0,0))
gg3=vertex(pos=vector(-1.5,0,-1.1),color=vector(1,0,0))
tgg1=triangle(v0=gg1,v1=gg2,v2=gg3)

gd1=vertex(pos=vector(-1.5,.45,-0.4),color=vector(1,0,0))
gd2=vertex(pos=vector(-1.5,-.45,-0.4),color=vector(1,0,0))
gd3=vertex(pos=vector(-1.5,0,-.9),color=vector(1,0,0))
tgd1=triangle(v0=gd1,v1=gd2,v2=gd3)

#Droite
da1=vertex(pos=vector(1.5,.55,-1.45),color = vector(1,0.6,0))
da2=vertex(pos=vector(1.5,.55,-0.55),color = vector(1,0.6,0))
da3=vertex(pos=vector(1.5,0.1,-1),color = vector(1,0.6,0))
tda1=triangle(v0=da1,v1=da2,v2=da3)

dba1=vertex(pos=vector(1.5,-.55,-1.45),color = vector(1,0.6,0))
dba2=vertex(pos=vector(1.5,-.55,-0.55),color = vector(1,0.6,0))
dba3=vertex(pos=vector(1.5,-0.1,-1),color = vector(1,0.6,0))
tdba1=triangle(v0=dba1,v1=dba2,v2=dba3)

dg1=vertex(pos=vector(1.5,.45,-1.6),color = vector(1,0.6,0))
dg2=vertex(pos=vector(1.5,-.45,-1.6),color = vector(1,0.6,0))
dg3=vertex(pos=vector(1.5,0,-1.1),color = vector(1,0.6,0))
tdg1=triangle(v0=dg1,v1=dg2,v2=dg3)

dd1=vertex(pos=vector(1.5,.45,-0.4),color = vector(1,0.6,0))
dd2=vertex(pos=vector(1.5,-.45,-0.4),color = vector(1,0.6,0))
dd3=vertex(pos=vector(1.5,0,-.9),color = vector(1,0.6,0))
tdd1=triangle(v0=dd1,v1=dd2,v2=dd3)

#Haut
hha1=vertex(pos=vector(-.45,1.5,-1.6),color = vector(0,1,0))
hha2=vertex(pos=vector(0.45,1.5,-1.6),color = vector(0,1,0))
hha3=vertex(pos=vector(0,1.5,-1.1),color = vector(0,1,0))
thha1=triangle(v0=hha1,v1=hha2,v2=hha3)

hba1=vertex(pos=vector(-.45,1.5,-.4),color = vector(0,1,0))
hba2=vertex(pos=vector(0.45,1.5,-.4),color = vector(0,1,0))
hba3=vertex(pos=vector(0,1.5,-.9),color = vector(0,1,0))
thba1=triangle(v0=hba1,v1=hba2,v2=hba3)

hga1=vertex(pos=vector(-.55,1.5,-.55),color = vector(0,1,0))
hga2=vertex(pos=vector(-.55,1.5,-1.45),color = vector(0,1,0))
hga3=vertex(pos=vector(-.1,1.5,-1),color = vector(0,1,0))
thga1=triangle(v0=hga1,v1=hga2,v2=hga3)

hda1=vertex(pos=vector(.55,1.5,-.55),color = vector(0,1,0))
hda2=vertex(pos=vector(.55,1.5,-1.45),color = vector(0,1,0))
hda3=vertex(pos=vector(.1,1.5,-1),color = vector(0,1,0))
thda1=triangle(v0=hda1,v1=hda2,v2=hda3)

#Bas
bha1=vertex(pos=vector(-.45,-1.5,-1.6),color = vector(0,0,1))
bha2=vertex(pos=vector(0.45,-1.5,-1.6),color = vector(0,0,1))
bha3=vertex(pos=vector(0,-1.5,-1.1),color = vector(0,0,1))
tbha1=triangle(v0=bha1,v1=bha2,v2=bha3)

bba1=vertex(pos=vector(-.45,-1.5,-.4),color = vector(0,0,1))
bba2=vertex(pos=vector(0.45,-1.5,-.4),color = vector(0,0,1))
bba3=vertex(pos=vector(0,-1.5,-.9),color = vector(0,0,1))
tbba1=triangle(v0=bba1,v1=bba2,v2=bba3)

bga1=vertex(pos=vector(-.55,-1.5,-.55),color = vector(0,0,1))
bga2=vertex(pos=vector(-.55,-1.5,-1.45),color = vector(0,0,1))
bga3=vertex(pos=vector(-.1,-1.5,-1),color = vector(0,0,1))
tbga1=triangle(v0=bga1,v1=bga2,v2=bga3)

bda1=vertex(pos=vector(.55,-1.5,-.55),color = vector(0,0,1))
bda2=vertex(pos=vector(.55,-1.5,-1.45),color = vector(0,0,1))
bda3=vertex(pos=vector(.1,-1.5,-1),color = vector(0,0,1))
tbda1=triangle(v0=bda1,v1=bda2,v2=bda3)