#Import
import GestionDataSet as gd

#import csv
gd.rd.pd.set_option('display.max_columns', 10)
Aretes= gd.rd.pd.read_csv('csv/Aretes.csv',sep=';')
Sommets= gd.rd.pd.read_csv('csv/Sommets.csv',sep=';')

#Constante
rd_resolu = gd.rd.RediCube()
CoutRediCubeFinish = rd_resolu.Cout()

#Test Elagage
#5min
N_sans_elagage=9358
N_elagage1=5452
N_elagage2=3906
#30min
#N_elagage1=82000
#N_elagage2=60000

##Arbre, parcours en largeur, elagage palier n de difference de cout avec le rd d'origine


def Prochain_file(n,nextfile):
    L=set(len(i[1]) for i in nextfile)
    nextfile=sorted(nextfile, key=lambda x: len(x[1]), reverse = False)
    D={}
    for i in L:
        Ltemp=[]
        for j in nextfile:
            if len(j[1])==i:
                Ltemp.append(j)
        D[i] = Ltemp

    file=[]
    for k in D.keys():
        D[k]=sorted(D[k], key=lambda x: x[2], reverse = True)
        file.extend(D[k][:int((len(D[k])/len(nextfile))*n)+1])

    return file

def Resolution_Arbre_Rollback_Complexe(r,n,N=N_elagage1,nbBeforeRollback=4): #1<n<7
    start_time = gd.rd.time.time()
    r.lastcoup=tuple()

    compteur=1#nombre de noeuds parcouru
    prof=0
    file=[]
    file.append([r,[],r.Cout()])#file = [[redi,[coups],cout],...]
    nextfile=[]#nextfile = [[redi,[coups],cout],...]
    Arbre={}#Arbre = {prodondeur : [[redi.cube,[coups],position du parent dans file],...], ....}
    All_Redi=[]
    All_Redi.append(r.cube)
    Noeuds_par_prof={}#Noeuds_par_prof = {profondeur : nombre de noeuds explorés+1 (len(file),...}


    while file[0][2] != 104 and compteur<N:
        #print('-----------')
        #print('profondeur = ',prof)
        #print('file = ',[len(i[1]) for i in file])
        #print('Cout max = ',file[0][2])
        position_file=0
        while file:
            compteur+=1
            node = file.pop(0)
            for coup in (node[0].ListCoups()):
                L2=[i for i in node[1]]
                copy_r = node[0].Copy()

                copy_r.Move(coup[0],coup[1],coup[2])
                cout=copy_r.Cout()

                if copy_r.cube not in All_Redi:
                    All_Redi.append(copy_r.cube)
                    L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                    nextfile.append([copy_r,L2,copy_r.Cout(),position_file])
            position_file+=1

        #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
        nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
        Arbre[prof+1] = [[i[0].cube,i[1],i[3]] for i in nextfile]
        nextfile=[[i[0],i[1],i[2]] for i in nextfile]
        #print('creation arbre niveau : ',prof+1)
        #print('remplissage arbre : ',len(nextfile))
        #nextfile=nextfile[:n]
        file.extend(Prochain_file(n,nextfile))
        Noeuds_par_prof[prof+1] = len([len(i[1]) for i in file if len(i[1]) == prof+1])
        #print(nextfile)
        #file.extend(nextfile)
        nextfile=[]

        prof+=1
        position_file=0

        #PARTIE ROLLBACK
        for f in range(len(file)):
            if len(file[f][1]) - nbBeforeRollback > 0:
                pos=f
                for p in range(nbBeforeRollback):
                    pos=Arbre[len(file[f][1])-p][pos][2]
                if file[f][2] <= (gd.rd.RediCube(Arbre[len(file[f][1])-nbBeforeRollback][pos][0])).Cout():
                    #del(Arbre[len(file[f][1])-nbBeforeRollback][pos])
                    nouveau_noeud=Noeuds_par_prof[len(file[f][1])-nbBeforeRollback]
                    #print('ROLLBACK ',nouveau_noeud+1, ' eme noeuds, profondeur ',len(file[f][1])-nbBeforeRollback)
                    Noeuds_par_prof[len(file[f][1])-nbBeforeRollback]+=1


                    file[f] = [gd.rd.RediCube(Arbre[len(file[f][1])-nbBeforeRollback][nouveau_noeud][0]),Arbre[len(file[f][1])-nbBeforeRollback][nouveau_noeud][1],(gd.rd.RediCube(Arbre[len(file[f][1])-nbBeforeRollback][nouveau_noeud][0])).Cout()]





                    #print('changement Noeuds_par prof, profondeur = ',len(file[f][1])-nbBeforeRollback,', ',Noeuds_par_prof[len(file[f][1])-nbBeforeRollback], ' eme noeuds')


    tf=gd.rd.time.time() - start_time
    nb_noeuds=-1
    sol=[]
    if compteur<N:
        nb_noeuds=compteur
        sol=file[0][1]

    #Temps de resolution, nombre de noeuds parcouru, solution
    print('Resolution en ',len(sol),' coups')
    return tf,nb_noeuds,sol#,Arbre

##Arbre, parcours en largeur, elagage palier n de difference de cout avec le rd d'origine
def Resolution_Arbre_Rollback_Basic(r,n,nbBeforeRollback): #1<n
    start_time = gd.rd.time.time()
    r.lastcoup=tuple()
    compteurnbNoeud = 0
    nbDeCoup = 0
    file=[]
    file.append([r,[],r.Cout()])
    nextfile=[]
    trouver = False

    #variable Rollback
    nextfileRollBack=file
    nextfileBestCount = file[0][2]
    nbIncBeforeRollBack = nbBeforeRollback
    nbDeCoupBeforeRollBack = nbDeCoup

    while not trouver:
        CoutFirstRediList = file[0][0].Cout()
        if CoutFirstRediList == CoutRediCubeFinish:
            trouver = True
        else:
            while file:
                print("score noeud suivante : " + str(CoutFirstRediList))
                compteurnbNoeud+=1
                node = file.pop(0)

                for coup in (r.ListCoups(True)):
                    L2=[i for i in node[1]]
                    copy_r = node[0].Copy()
                    copy_r.Move(coup[0],coup[1],coup[2])
                    L2.append({'hauteur':coup[0],'num':coup[1],'sens':coup[2]})
                    #print({'hauteur':hauteur,'num':num,'sens':sens})

                    nextfile.append([copy_r,L2,copy_r.Cout()])


            #Tri par cout, effectue d'abord les coups qui donnent un meilleur cout
            nextfile=sorted(nextfile, key=lambda x: x[2], reverse = True)
            file = nextfile[:n]

            if nextfile[0][2] > nextfileBestCount:
                nextfileRollBack=nextfile
                nextfileBestCount = nextfile[0][2]
                nbIncBeforeRollBack = nbBeforeRollback
                nbDeCoup += 1
                nbDeCoupBeforeRollBack = nbDeCoup
                print("profondeur suivante avec pour nombre de dieu : " + str(nbDeCoup))
            else:
                nbIncBeforeRollBack = nbIncBeforeRollBack - 1
                if nbIncBeforeRollBack == 0:
                    nbIncBeforeRollBack = nbBeforeRollback
                    file = nextfileRollBack[:n]
                    nextfileBestCount = file[0][2]
                    nextfileRollBack = nextfileRollBack[n:]
                    nbDeCoup = nbDeCoupBeforeRollBack
                    print("Rollback")
                else:
                    nbDeCoup += 1
                    print("profondeur suivante avec pour nombre de dieu : " + str(nbDeCoup))
            #reset
            nextfile=[]

    tf=round(gd.rd.time.time() - start_time,2)
    sol=file[0][1]
    #Temps de resolution, nombre de noeuds parcouru, solution
    return sol,tf,nbDeCoup,compteurnbNoeud



'''
Search cost number to all RediCube of the Dataset
'''
def FonctionResolutionDataset(n_inf,n_sup,nameDataset):
    lien = "csv//RediGenerate//" + nameDataset + ".csv"
    df = gd.rd.pd.read_csv(lien,sep=';')
    for n in range(n_inf,n_sup+1):
        r= gd.CreateRedicubeToResolveVisua(n, lien)
        t,noeuds,s = Resolution_Arbre_Rollback_Complexe(r,13,1000,5)
        st=''
        for i in s:
            st+='('
            st+=i['hauteur']
            st+=','
            st+=str(i['num'])
            st+=','
            st+=str(i['sens'])
            st+='),'
        df.loc[n,'Solution']= st
        df.loc[n,'Nombre_noeuds']= noeuds
        df.loc[n,'NbCoups']= len(s)
        df.loc[n,'Temps']= t
        print('Solution ' + str(n) + ' : ' + st + ' Nombre_noeuds : ' + str(noeuds) + ', Temps : ' + str(t))

        df.to_csv(lien,';',index=False,mode='w')