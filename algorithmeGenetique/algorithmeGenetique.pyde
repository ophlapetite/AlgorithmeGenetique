##################################### PROJET 2020- 2021 ############################

########################Déclaration des paramètres#################################
global nbRect,LargeurRect,lettre,img,imgWidth,imgHeight, N

N=1 #numéro de génération 
nbRect=5
LargeurRect=4 
lettre='A'
imgWidth=40
imgHeight=40
img=None


########################Déclaration des Classes####################################
class Population:
    def __init__(self):
        self.individus=[]       #une liste d'individus initialisée à vide
        self.num=N        #un numéro de population
    

class Individu:
    def __init__(self):
        self.rectangles=[]     #une liste de rectangles
        self.cout=0
            
    def drawInd(self):
        global img, imgWidth, imgHeight
        img=createGraphics(imgWidth,imgHeight)
        img.beginDraw()
        img.noSmooth()
        img.background(255)
        img.fill(255,0,0)
        img.noStroke()
        img.textAlign(CENTER,BOTTOM)
        img.textSize(40)
        img.text(lettre,40/2,40)
        print("drawInd")
        
        img.fill(0,255,0,127)
        
        for rectangle in self.rectangles :
            x = random(0,40)
            y = random(0,40)
            print("un Rectangle")
            img.pushMatrix()
            img.translate(x,y)
            img.rotate(rectangle.getOrientation())
            img.rect(rectangle.getCoord()[0],rectangle.getCoord()[1],rectangle.getLongueur(),LargeurRect)
            img.popMatrix()
        img.endDraw()
            
    
class Rectangle:
    def __init__(self,i):
        self.orientation=i*PI/4    # 8 orientations possibles, valeur i comprise entre 1 et 8
        self.largeur=LargeurRect
        self.longueur=0
        self.coord=(0,0)
        
    def getLongueur(self):
        return self.longueur
    
    def getOrientation(self):
        return self.orientation
    
    def getCoord(self):
        return self.coord
    

def setup():
    
############################Initialisation de la fenêtre###########################
    size(40,40)
    noLoop()
    
    
def draw():

    P1=Individu()
    print(P1.rectangles)
    
    for j in range(2):
        i = random(1,8)
        r=Rectangle(i)
        r.longueur=random(5,20)
        r.coord=(random(0,40),random(0,40))
        P1.rectangles.append(r)
    print(P1.rectangles)
        
    P1.drawInd()
    img.save('essai.jpg') #quel format d'image choisir pour éviter la compression ?????
    image(img,0,0) #marche pas ça ne s'affiche pas 
    
def keyPressed():
    global lettre
    lettre=key
    
