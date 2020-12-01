################################################################################### PROJET PYTHON 2020- 2021 ############################################################################################

from random import randint  #pour obtenir des entiers aléatoires
import time                 #pour mesurer le temps d'execution
N=1                         #numéro de génération 
nurserie=[]                 # déclaration de la liste représentant la nurserie 
saveStats= True             #remplir ou non le fichier csv pour faire un graphique
#########################################################################################RÉGLAGES########################################################################################################

nbGeneration=100            #nombre de générations à engendrer 
nbRect=5                    #nombre de rectangles par individu
largeurRect=4               #largeur fixe des rectangles
lettre='A'                  #glyphe à approcher
imgWidth=40                 #largeur de l'image 
imgHeight=40                #hauteur de l'image                  
indParPopulation=100        #nombre d'individus par population 
nbSelection=40              #nombre d'individus sélectionnés
nbReproCroisee=30           #nombre d'individus engendrés par reproduction croisée
nbMutation=30               #nombre d'individus mutés dans la nurserie
coefMutation=0.4            #coefficient du cout initial qui doit être supérieur au coût après mutation
decOrdo = 100               #décalage de l'axe en ordonnée pour tracer le graphique
graduation = 100/10         #Nb de générations sur le nombre de graduations 

###################################################################################### CLASSE POPULATION ################################################################################################

class Population:
    
    
    def __init__(self,n):
        '''
        Constructeur d'une population
        
        :param n: Le numéro de la population créée
        '''
        self.individus=[]     #une liste d'individus initialisée à vide
        self.num=n            #numéro de génération correspondant        

    def generePop(self):
        '''
        Fonction qui génère des individus aléatoires et les ajoute à la liste d'individus pour constituer une première population
        '''
        for j in range(indParPopulation):
            P1=Individu(j)                 
            P1.genereInd()
            self.individus.append(P1)
            
    def drawPop(self):
        '''
        Fonction qui affiche une population en affichant ses individus un par un avec un décalage
        '''
        decX = 0                                                  #décalage de l'image en X
        decY = 0                                                  # décalage de l'image en Y 
        for i in range(len(self.individus)):
            #self.individus[i].saveImg()                          #on peut mettre cette ligne en commentaire si on ne veut pas sauvegarder toutes les images à chaque fois
            image(self.individus[i].img,decX,decY)                #affiche l'image dans la fenêtre à la position donnée
            if (i+1)%10 == 0 and i != 0 :                         
                decY += 40
                decX = 0
            else:
                decX += 40
                
    def engendrePopulationSuivante(self):
        '''
        Engendre la population suivante à partie d'une population 'Parente'
        
        :return: la nouvelle population créée
        '''
        global nurserie
        
        nurserie = self.selection()                                #la selection des meilleurs individus de la population parente
        nurserie += self.reproductionCroisee()                     #enfants créés par reproduction entre les meilleurs individus de la population parente
        nurserie += self.mutation()                                #partie de la population parente mutée 
                
    def selection(self):
        '''
        Fonction qui va selectionner les n meilleurs individus d'une population
        '''
        popTriee = triFusion(self.individus)
        return popTriee[:nbSelection+1]         
        
            
    def reproductionCroisee(self):
        '''
        Fonction qui va engendrer la génération suivante en faisant des croisements de 2 parents au hasard
        '''
        groupeParent = self.individus
        laSelection = []
        
        nb= nbReproCroisee
        for repro in range(nb):
            rectanglesEnfant = []

            indice1 = randint(0,len(groupeParent)-1)
            parent1 = groupeParent[indice1]
            groupeParent.pop(indice1)
        
            indice2 = randint(0,len(groupeParent)-1)
            parent2 = groupeParent[indice2]
            groupeParent.pop(indice2)
        
            rectParent1 = parent1.rectangles
            rectParent2 = parent2.rectangles
            
            coupure=nbRect//2
            
            rectanglesEnfant=parent1.rectangles[:coupure]+parent2.rectangles[coupure:]
            
            #on créé le fils résultant
            I=Individu(len(nurserie)+len(laSelection)+1)
            I.rectangles=rectanglesEnfant
            I.genereImg()
            I.calculCout()
            laSelection.append(I)
            
            #on remet les parents dans la liste à leur place initiale pour pouvoir les tirer au sort au prochain tour
            groupeParent.insert(indice1,parent1)
            groupeParent.insert(indice2,parent2)
            
        return laSelection
    
    def mutation(self):
        '''
        Un individu subissant une mutation génétique voit un ou plusieurs de ses gènes modifiés
        '''
        groupeMutation = nurserie[:] #copie sans pointeur
        enfants = []
    
        for i in range(nbMutation):
            indice = randint(0,len(groupeMutation)-1)
            indMutation = groupeMutation[indice]
            groupeMutation.remove(indMutation)
            coutInitial = indMutation.cout
            coutApres = -1
            I = Individu(len(nurserie)+len(enfants)+1)
            #coef modifiable
            while (coutApres < coutInitial*coefMutation):
                I.rectangles = indMutation.rectangles
                lesRects = []
                for rect in I.rectangles:
                    mutation=randint(1,4)
                    newRec = Rectangle(1)
                    
                    if(mutation==1):
                        #on change l'orientation
                        i = random(1,8)
                        newRec.orientation=i*PI/4
                        newRec.longueur = rect.longueur
                        newRec.x = rect.x
                        newRec.y = rect.y
                    elif(mutation==2):
                        #on change la taille
                        newRec.setLongueur(random(5,20))
                        newRec.x = rect.x
                        newRec.y = rect.y
                        newRec.orientation = rect.orientation
                    elif(mutation==3):
                        #on change les coordonnées
                        newRec.setX(random(0,40)) ; newRec.setY(random(0,40))
                        newRec.orientation = rect.orientation
                        newRec.longueur = rect.longueur
                    elif(mutation==4):
                        i = random(1,8)
                        newRec.orientation=i*PI/4
                        newRec.setLongueur(random(5,20))
                        newRec.setX(random(0,40)) ; newRec.setY(random(0,40))
                    lesRects.append(newRec)
                    
                I.rectangles=lesRects
                        
                I.genereImg()
                I.calculCout()
                coutApres = I.cout
            
            enfants.append(I)
            
        return enfants
    
    def afficheCout(self):
        '''
        Fonction qui va afficher les coûts de chaque individu d'une population
        '''
        for ind in self.individus:
            print(ind.cout)
            
    def meilleurIndividu(self):
        '''
        Affiche le meilleur individu d'une population
        '''
        popTrie = triFusion(self.individus)
        popTrie[0].drawIndBlack()
            

    def stats(self):
        '''
        Affichage console des statistiques liées au coût des individus 
        '''
        coutMin = 101
        coutMax = -1
        coutMoyen = 0
        
        for ind in self.individus:
            coutMoyen += ind.cout
            
            #min
            if(ind.cout < coutMin):
                coutMin = ind.cout
                
            #max
            if(ind.cout > coutMax):
                coutMax = ind.cout
                
        #moyenne
        coutMoyen = coutMoyen/indParPopulation
        
        print("Cout Min : "+str(coutMin)+ ", Cout Max : "+str(coutMax)+", Cout Moyen : "+str(coutMoyen)+" Generation :"+str(N))
        if(saveStats == True):
            file=open("stats.csv","a")
            line=str(coutMin)+";"+str(coutMoyen)+";"+str(coutMax)
            file.write(line)
            file.write("\n")
            file.close()
            
############################################################################################# CLASSE INDIVIDU ##########################################################################################
class Individu:
    def __init__(self,n):
        '''
        Constructeur d'individu
        
        :param n: Le numéro de l'individu créé
        '''
        self.rectangles=[]                                 #une liste de rectangles
        self.cout=0
        self.numero=n
        self.img=createGraphics(imgWidth,imgHeight)       #création d'une image de 40*40pixels
        
    def getNum(self):
        '''
        retourne le numéro de l'individu
        '''
        return self.numero
    
    def getCout(self):
        '''
        retourne le cout de l'individu
        '''
        return self.cout
    
    def genereInd(self):
        '''
        Fonction qu génère un individu aléatoire
        '''
        # remplissage du tableau de rectangles avec rectangles aléatoires
        self.genereRect()
        #création de l'image de l'individu
        self.genereImg()
        #calcul du coût
        self.calculCout()
        
    def genereRect(self):
        '''
        Fonction qui génère des rectangles aléatoires et les stockes dans la liste de rectangles
        '''
        for j in range(nbRect):
            i = random(1,8)
            r=Rectangle(i)
            r.setLongueur(random(5,20))
            r.setX(random(0,40)) ; r.setY(random(0,40))
            self.rectangles.append(r)
            
            
    def genereImg(self):
        '''
        Fonction qui génère l'image de l'individu, affiche la lettre en rouge et les rectangles en vert 
        '''
        self.img.noSmooth()
        self.img.beginDraw()
        self.img.background(255)
        self.img.fill(255,0,0)
        self.img.noStroke()
        self.img.textAlign(CENTER,BOTTOM)
        self.img.textSize(imgHeight)
        self.img.text(lettre,imgWidth/2,imgHeight)
        
        self.img.fill(0,255,0,127)
        
        for rectangle in self.rectangles :
            self.img.pushMatrix()
            self.img.translate(rectangle.getX(),rectangle.getY())
            self.img.rotate(rectangle.getOrientation())
            self.img.rect(0,0,rectangle.getLongueur(),largeurRect)
            self.img.popMatrix()
        self.img.endDraw()
        
    def calculCout(self):
        '''
        Fonction qui calcule le cout de l'individu en fonction de la répartition des couleurs des pixels de son image
        '''
        pB=0.0 #nb pixels blancs
        pR=0.0 # rouges
        pV=0.0 #verts
        pA=0.0 # autre couleur/mélange
        for i in range(0,len(self.img.pixels)):
            col=(red(self.img.pixels[i]), green (self.img.pixels[i]),blue(self.img.pixels[i]))
            if col==(255,255,255):
                pB=pB+1
            else:
                if col==(255,0,0):
                    pR=pR+1
                else:
                    if col==(128,255,128):
                        pV=pV+1
                    else:
                        pA=pA+1
        
        self.cout=int((pA/(pR+pV+pA))*100)
        
    def drawInd(self):
        '''
        Fonction qui affiche à l'écran l'image d'un individu
        '''
        image(self.img,0,0)
        
    def saveImg(self):
        '''
        Fonction qui sauvegarde au format jpg l'image de l'individu
        '''
        self.img.save('essai_'+str(N)+'_'+str(self.getNum())+'.jpg')
        
    def drawIndBlack(self):
        '''
        Fonction qui affiche l'image d'un individu en noir sans la lettre rouge en dessous
        '''
        self.img=createGraphics(imgWidth,imgHeight)
        self.img.beginDraw()
        self.img.background(255)
        self.img.fill(0,0,0)
        
        for rectangle in self.rectangles :
            self.img.pushMatrix()
            self.img.translate(rectangle.getX(),rectangle.getY())
            self.img.rotate(rectangle.getOrientation())
            self.img.rect(0,0,rectangle.getLongueur(),largeurRect)
            self.img.popMatrix()
        self.img.endDraw()
        image(self.img,0,0)
        
                
                    
######################################################################################## CLASSE RECTANGLE ###############################################################################################
class Rectangle:
    def __init__(self,i):
        '''
        Constructeur d'individu
        
        :param i: entier compris entre 1 et 8 
        '''
        self.orientation=i*PI/4    # 8 orientations possibles, valeur i comprise entre 1 et 8
        self.largeur=largeurRect
        self.longueur=0
        self.x=0
        self.y=0
        
    def getLongueur(self):
        '''
        retourne la longueur du rectangle
        '''
        return self.longueur
    
    def getOrientation(self):
        '''
        retourne l'orientation du rectangle
        '''
        return self.orientation
    
    def getX(self):
        '''
        retourne la position en x du rectangle
        '''
        return self.x
    
    def getY(self):
        '''
        retourne la position en y du rectangle
        '''
        return self.y
    
    def setLongueur(self,l):
        '''
        donne une longueur au rectangle
        
        :param l: entier
        '''
        self.longueur=l
        
    def setX(self,val):
        '''
        donne une position en x au rectangle
        
        :param val: entier
        '''
        self.x=val
        
    def setY(self,val):
        '''
        donne une position en y au rectangle
        
        :param val: entier
        '''
        self.y=val
        
############################################################################################ MÉTHODES DE TRI #############################################################################################


def fusion(gauche,droite):
    resultat = []
    indexGauche, indexDroite = 0,0
    while indexGauche < len(gauche) and indexDroite < len(droite):
        if gauche[indexGauche].cout >= droite[indexDroite].cout:
            resultat.append(gauche[indexGauche])
            indexGauche += 1
        else:
            resultat.append(droite[indexDroite])
            indexDroite += 1
    
    if gauche:
        resultat.extend(gauche[indexGauche:])
    if droite:
        resultat.extend(droite[indexDroite:])
        
    return resultat
    
def triFusion(m):
    """
    Fonction qui trie le tableau passé en paramètre
    """
    if len(m) <= 1:
        return m
    milieu = len(m)//2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = triFusion(gauche)
    droite = triFusion(droite)
    return list(fusion(gauche, droite))

        
###################################################################################### INITIALISATION DE LA FENETRE ######################################################################################        
def setup():
    
    size(400,400)
    noLoop()              #on peut le mettre en commentaire si on veut que la fonction draw s'exécute en boucle
    
    
##########################################################################################################################################################################################################    
def draw():
    global N
    
    #remise à 0 du fichier csv
    if(saveStats==True):
        file=open('stats.csv', 'w')
        line="Cout Minimum;Cout Moyen; Cout Maximum"
        file.write(line)
        file.write("\n")
        file.close() 
        
    #début du calcul du temps d'exécution
    tempsExec = range(100000)
    tps1 = time.clock()
    tempsExec.sort()
    
    
    Pop=Population(N)
    Pop.generePop()
    print("----------- Les stats -----------")

    for i in range(nbGeneration):
        N += 1
        nouvellePop=Population(N)
        Pop.engendrePopulationSuivante()
        nouvellePop.individus = nurserie
        nouvellePop.stats()
        Pop.individus = nouvellePop.individus
        
    print("-----------")
    #affichage du meilleur individu
    nouvellePop.meilleurIndividu()
    #affichage de la population finale
    #nouvellePop.drawPop()

    #mesure du temps d'execution
    tps2 = time.clock()
    print("temps d'execution : ",tps2-tps1, " secondes.")
