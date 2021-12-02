# -*- coding: utf-8 -*-

from vpython import * 
import math as m

#Élément de référence (position)

#box1red=box(pos = vector(-1, 1, 0),size = vector(1, 1, 1),color = vector(1, 0, 0))
#box2red=box(pos = vector(1, 1, 0),size = vector(1, 1, 1),color = vector(1, 0, 0))
#box3red=box(pos = vector(-1, -1, 0),size = vector(1, 1, 1),color = vector(1, 0, 0))
#box4red=box(pos = vector(1, -1, 0),size = vector(1, 1, 1),color = vector(1, 0, 0))

#Sommets
#=======

#######################################################################################################################################
############################################    FACE AVANT    #####################################################
#######################################################################################################################################

#Constituants de la première cube à gauche en haut
pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 0, 0))     #ROUGE (face gauche)
pyr2=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 1, 1))     #BLANC (face centrale)
pyr2.rotate(angle=m.pi/2,axis=vector(0,1,0))
pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,1,0))          #VERT  (face haute)
pyr3.rotate(angle=135,axis=vector(0,1,0))

#Constituants de la première cube à droite en haut
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1,0.6,0))     #ORANGE(face droite)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,1,0))          #VERT  (face haute)
#pyr3.rotate(angle=120,axis=vector(0,1,0))

#Constituants de la première cube à gauche en bas
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 0, 0))     #ROUGE (face gauche)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,0,1))          #BLEU  (face basse)
#pyr3.rotate(angle=120,axis=vector(0,1,0))

#Constituants de la première cube à droite en bas
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1,0.6,0))     #ORANGE(face droite)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,0,1))          #BLEU  (face basse)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#######################################################################################################################################
#############################################    FACE ARRIÈRE    ################################################
#######################################################################################################################################

#Constituants de la première cube à gauche en haut
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 0, 0))     #ROUGE (face gauche)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,1,0))          #VERT  (face gauche)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#Constituants de la première cube à droite en haut
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1,0.6,0))     #ORANGE(face droite)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,1,0))          #VERT  (face haute)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#Constituants de la première cube à gauche en bas
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 0, 0))     #ROUGE (face gauche)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,0,1))          #BLEU  (face basse)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#Constituants de la première cube à droite en bas
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1,0.6,0))     #ORANGE(face droite)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,0,1))          #BLEU  (face basse)
#pyr3.rotate(angle=90,axis=vector(0,1,0))




#Arètes
#=======

#######################################################################################################################################
############################################    FACE AVANT    #####################################################
#######################################################################################################################################

#Constituants de l'arête haute
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,1,0))          #VERT  (face haute)
#pyr3.rotate(angle=120,axis=vector(0,1,0))

#Constituants de l'arête gauche 
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 0, 0))     #ROUGE (face gauche)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))

#Constituants de l'arête droite
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1,0.6,0))     #ORANGE(face droite)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))

#Constituants de l'arête basse
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,1))          #BLANC (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,0,1))          #BLEU  (face basse)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#######################################################################################################################################
#############################################    FACE ARRIÈRE    ################################################
#######################################################################################################################################

#Constituants de l'arête haute
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,1,0))          #VERT  (face haute)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#Constituants de l'arête gauche 
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1, 0, 0))     #ROUGE (face gauche)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))

#Constituants de l'arête droite
#pyr1=pyramid(pos = vector(-1, 1, 0),size=vector(0.25,1,1),color = vector(1,0.6,0))     #ORANGE(face droite)
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))

#Constituants de l'arête basse
#pyr2=pyramid(pos = vector(-1,1,0),size=vector(0.25,1,1),color = vector(1,1,0))          #JAUNE (face centrale)
#pyr2.rotate(angle=90,axis=vector(0,1,0))
#pyr3=pyramid(pos = vector(1,1,0),size=vector(0.25,1,1),color = vector(0,0,1))          #BLEU  (face basse)
#pyr3.rotate(angle=90,axis=vector(0,1,0))

#######################################################################################################################################
#############################################   FONCTION DE ROTATION    #############################################
#######################################################################################################################################

