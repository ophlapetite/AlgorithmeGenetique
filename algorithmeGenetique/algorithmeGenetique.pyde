##################################### PROJET 2020- 2021 ############################

########################Déclaration des paramètres#################################
global nbRect,LargeurRect,lettre,img,imgWidth,imgHeight
    
nbRect=5
LargeurRect=4 
lettre='A'
imgWidth=40
imgHeight=40


########################Déclaration des Classes####################################
class Population:
    def __init__(self,numero):
        self.individus=[]       #une liste d'individus initialisée à vide
        self.num=numero         #un numéro de population
    

class Individu:
    def __init__(self):
        self.rectangles=[]     #une liste de rectangles
        self.cout=0
            
    def drawInd(ind):
        img=createGraphics(imgWidth,imgHeight)
        img.beginDraw()
        img.noSmooth()
        img.background(255)
        img.fill(255,0,0)
        img.noStroke()
        img.textAlign(CENTER,BOTTOM)
        img.textSize(40)
        img.text(lettre,40/2,40)
            
    
class Rectangle:
    def __init__(self,la):
        self.orientation=PI/4    #on lui donne une valeur d'orientation par défaut
        self.largeur=LargeurRect
        self.longueur=0
    

def setup():
    
############################Initialisation de la fenêtre###########################
    size(400,500)
    
def draw():

    I1=Individu()
    I1.drawInd()
