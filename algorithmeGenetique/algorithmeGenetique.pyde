##################################### PROJET 2020- 2021 ############################
from random import randint
########################Déclaration des paramètres#################################
global nbRect,LargeurRect,lettre,img,imgWidth,imgHeight, N, nurserie

N=1 #numéro de génération 
nbRect=5
largeurRect=4 
lettre='A'
imgWidth=40
imgHeight=40
img=None
indParPopulation=100
nbSelection=30               #30% de la population est constituée des meilleurs individus de la population précédente
nbReproCroisee=35   
nbMutation=35    
nurserie=[]

########################Déclaration des Classes####################################
class Population:
    def __init__(self,n):
        self.individus=[]       #une liste d'individus initialisée à vide
        self.num=n        #un numéro de population
        
    
    def generePop(self):
        '''
        Fonction qui génère des individus aléatoires et les ajoute pour constituer une population qui servira de base
        '''
        for j in range(indParPopulation):
            P1=Individu(j)
            P1.genereInd()
            self.individus.append(P1)
            
    def drawPop(self):
        '''
        Fonction qui affiche une population en affichant ses individus un par un avec un décalage
        '''
        decX = 0  #décalage de l"image en X
        decY = 0 # décalage de l'image en Y 
        for i in range(len(self.individus)):
            self.individus[i].saveImg()                          #on peut mettre cette ligne en commentaire si on ne veut pas suvegarder chaque image à chaque fois
            image(self.individus[i].img,decX,decY)
            if (i+1)%10 == 0 and i != 0 :
                decY += 40
                decX = 0
            else:
                decX += 40
                
    def engendrePopulationSuivante(self):
        global nurserie
        nurserie=[]
        nurserie=self.selection()
        nurserie+=self.reproductionCroisee()
        #reste à faire les mutations
        nouvellePop=Population(self.num+1)
        nouvellePop.individus=nurserie
        #nouvellePop.drawPop()
        return nouvellePop
                
    def selection(self):
        '''
        Fonction qui va selectionner les nbSelection meilleurs individus de Pop
        '''
        popTrie = triFusion(self.individus)
        meilleurPatrimoine = []
        
        for i in range(nbSelection):
            meilleurPatrimoine.append(popTrie[i])
            
        return meilleurPatrimoine
        
        
    def afficheCout(self):
        '''
        Fonction qui va afficher les couts de chaque individus d'une population
        '''
        for ind in self.individus:
            print(ind.cout)
            
    def reproductionCroisee(self):
        global nurserie
        '''
        Fonction qui va engendrer la génération suivante en faisant des croisement de 2 parents au hasard
        '''
        enfants = []
        rectanglesEnfant = []
    
        groupeParent = nurserie
        nb= nbReproCroisee
        for repro in range(nb):
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
            
            I=Individu(len(nurserie)+1)
            I.rectangles=rectanglesEnfant
            I.genereImg()
            I.calculCout()
            enfants.append(I)
            
            #on remet les parents dans la liste à leur place initiale pour pouvoir les tirer au sort au prochain tour
            groupeParent.insert(indice1,parent1)
            groupeParent.insert(indice2,parent2)
        
        return enfants
    
    #def mutation(self):
    #    global nurserie
    #    for i in range(nbMutation):
    #        indice = randint(0,len(nurserie))
    #        indAMuter=nurserie[indice]
   #         for rect in indAMuter.rectangles:
                
            
        
            
####################################################################################
class Individu:
    def __init__(self,n):
        self.rectangles=[]     #une liste de rectangles
        self.cout=0
        self.numero=n
        self.img=createGraphics(imgWidth,imgHeight)
        
    """def __init__(self,n, rects = []):
        self.rectangles=rects     #une liste de rectangles
        self.cout=0
        self.numero=n
        self.img=createGraphics(imgWidth,imgHeight)"""
        
    def getNum(self):
        return self.numero
    
    def getCout(self):
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
        """
        Fonction qui génère des rectangles aléatoires et les stockes dans rectangles
        """
        for j in range(nbRect):
            i = random(1,8)
            r=Rectangle(i)
            r.setLongueur(random(5,20))
            r.setX(random(0,40)) ; r.setY(random(0,40))
            self.rectangles.append(r)
            
            
    def genereImg(self):
        """
        Fonction qui génère l'image de l'individu, affiche la lettre en rouge et les rectangles en vert 
        """
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
        """
        Fonction qui calcule le cout de l'individu en fonction de la répartition des couleurs des pixels de son image
        """
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
        
        self.cout=int((pA/(pR+pA))*100)
        
    def drawInd(self):
        """
        Fonction qui affiche à l'écran l'image d'un individu
        """
        image(self.img,0,0)
        
    def saveImg(self):
        """
        Fonction qui sauvegarde au format jpg l'image de l'individu
        """
        self.img.save('essai'+str(self.getNum())+'.jpg')

        
        

                    
########################################################################################   
class Rectangle:
    def __init__(self,i):
        self.orientation=i*PI/4    # 8 orientations possibles, valeur i comprise entre 1 et 8
        self.largeur=largeurRect
        self.longueur=0
        self.x=0
        self.y=0
        
    def getLongueur(self):
        return self.longueur
    
    def getOrientation(self):
        return self.orientation
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setLongueur(self,l):
        self.longueur=l
        
    def setX(self,val):
        self.x=val
        
    def setY(self,val):
        self.y=val
############################Autres fonctions utiles################################


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
    if len(m) <= 1:
        return m
    milieu = len(m)//2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = triFusion(gauche)
    droite = triFusion(droite)
    return list(fusion(gauche, droite))

        
############################Initialisation de la fenêtre###########################        
def setup():
    
    size(400,400)
    noLoop()
    
####################################################################################    
def draw():
    global N
    
    Pop=Population(N)
    Pop.generePop()
    #Pop.drawPop()
    for i in range(30):
        Pop=Pop.engendrePopulationSuivante()
    #Pop.engendrePopulationSuivante()
    #Pop.mutation()
    Pop.drawPop()
    Pop.afficheCout()


#####à revoir######
    #def keyPressed():
    #global lettre
    #lettre=key
    
