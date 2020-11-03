##################################### PROJET 2020- 2021 ############################

########################Déclaration des paramètres#################################
global nbRect,LargeurRect,lettre,img,imgWidth,imgHeight, N

N=1 #numéro de génération 
nbRect=5
largeurRect=4 
lettre='A'
imgWidth=40
imgHeight=40
img=None
indParPopulation=100


########################Déclaration des Classes####################################
class Population:
    def __init__(self,n):
        self.individus=[]       #une liste d'individus initialisée à vide
        self.num=n        #un numéro de population
    
    def generePop(self):
        for j in range(indParPopulation):
            P1=Individu(j)
            P1.genereInd()
            self.individus.append(P1)
            
    def drawPop(self):
        decX = 0  #décalage de l"image en X
        decY = 0 # décalage de l'image en Y 
        for ind in self.individus:
            ind.drawInd()
            img.save('essai'+str(ind.getNum())+'.jpg')
            image(img,decX,decY)
            i=ind.getNum()
            if (i+1)%10 == 0 and i != 0 :
                decY += 40
                decX = 0
            else:
                decX += 40
            
            
####################################################################################
class Individu:
    def __init__(self,n):
        self.rectangles=[]     #une liste de rectangles
        self.cout=0
        self.numero=n
        
    def getNum(self):
        return self.numero
  
    def genereInd(self):
        for j in range(nbRect):
            i = random(1,8)
            r=Rectangle(i)
            r.setLongueur(random(5,20))
            r.setX(random(0,40)) ; r.setY(random(0,40))
            self.rectangles.append(r)
          
    def drawInd(self):
        global img
        img=createGraphics(imgWidth,imgHeight)
        img.beginDraw()
        img.noSmooth()
        img.background(255)
        img.fill(255,0,0)
        img.noStroke()
        img.textAlign(CENTER,BOTTOM)
        img.textSize(imgHeight)
        img.text(lettre,imgWidth/2,imgHeight)
    
        
        img.fill(0,255,0,127)
        
        for rectangle in self.rectangles :
            img.pushMatrix()
            img.translate(rectangle.getX(),rectangle.getY())
            img.rotate(rectangle.getOrientation())
            img.rect(0,0,rectangle.getLongueur(),largeurRect)
            img.popMatrix()
        img.endDraw()
        
        #calcul du coût
        pB=0 #nb pixels blancs
        pR=0 # rouges
        pV=0 #verts
        pA=0 # autre couleur/mélange
        for i in range(0,len(img.pixels)):
            col=(red(img.pixels[i]), green (img.pixels[i]),blue(img.pixels[i]))
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
        
        self.cout=pV+pR
        print(self.cout)
            
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
        
############################Initialisation de la fenêtre###########################        
def setup():
    
    size(400,400)
    noLoop()
    
####################################################################################    
def draw():
    global N

    
    Pop=Population(N)
    Pop.generePop()
    Pop.drawPop()
    N=N+1 



def keyPressed():
    global lettre
    lettre=key
    
