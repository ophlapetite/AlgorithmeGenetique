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
            img.ellipse(x,y, 10,10)#il y a des ronds dessus mais pas de rect
            img.pushMatrix()
            img.translate(x,y)
            img.rotate(rectangle.getOrientation())
            img.rect(0,0,LargeurRect,rectangle.getLongueur())
            img.popMatrix()
        img.endDraw()
            
    
class Rectangle:
    def __init__(self,angle):
        self.orientation=angle*PI/4    #on lui donne une valeur d'orientation par défaut
        self.largeur=LargeurRect
        self.longueur=0
        
    def getLongueur(self):
        return self.longueur
    
    def getOrientation(self):
        return self.orientation
    

def setup():
    
############################Initialisation de la fenêtre###########################
    size(40,40)
    
    
def draw():
    global lettre,img

    #if keyPressed:
      #  lettre=key
      #  i=i+1
   # else:
        #test pour afficher lettre sans passer par la fonction
        #background(255);
        #fill(255,0,0);
        #textSize(40);
        #text(lettre,10,40);
        
    
    #test en passant par la fonction 
    #on demande à l'utilisateur de rentrer la lettre à tester 
    P1=Individu()
    
    for j in range(nbRect):
        i = random(0,8)
        P1.rectangles.append(Rectangle(i))
        
    P1.drawInd()
    img.save('essai.jpg') #quel format d'image choisir pour éviter la compression ?????
    image(img,0,0) #marche pas ça ne s'affiche pas 
    
def keyPressed():
    global lettre
    lettre=key
    
#COUCOU JE SUIS UN COMMENTAIRE 

    
