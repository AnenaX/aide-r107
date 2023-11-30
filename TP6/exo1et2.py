import turtle # programme principal # ----------------------------------------

LARGEUR=1000 # largeur de la fenêtre
HAUTEUR=500 # hauteur de la fenêtre

def tracerRectangle(x, y, larg, long):
    t.goto(x,y)
    t.pendown()
    i=0
    for i in range(2):
        t.forward(long)
        t.right(90)
        t.forward(larg)
        t.right(90)

def tracerEscalier(larg, long, marches):
    for i in range(marches):
        t.forward(long)
        t.left(90)
        t.forward(larg)
        t.right(90)

def tracerCible(x, y, n, p, color, ecart):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    for i in range(1, n+1):
        t.penup()
        t.goto(x, -p-x)
        t.pendown()
        t.circle(p)
        p += ecart 
    t.color("black")

def tracerOctogone(cote): 
    n=1
    while n <= 8:
        t.forward(cote)
        t.left(45)
        n = n + 1

def tracerPolygone(nbc, cote):
    t.penup()
    t.goto(90,90)
    t.pendown()
    for i in range(1,cote+1):
        t.forward(cote)
        t.right(360/nbc)



turtle.setup(LARGEUR, HAUTEUR) # initialise la taille de l'écran
t = turtle.Turtle() # La tortue se nommera t
t.speed(10) # 1 : vitesse lente de la tortue, 10 vitesse rapide (pas obligatoire !)
t.penup() # lever le stylo

x = int(input("Coordonné pour x : "))
y = int(input("Coordonné pour y : "))
larg = int(input("Largeur du rectangle : "))
long = int(input("Longueur du rectangle : ")) 
tracerRectangle(x,y,larg,long)

nbrMarches = int(input("Combien y'aura-t-il de marches ? "))
tracerEscalier(larg, long, nbrMarches)

xCible = int(input("Coordonné pour la cible x : "))
yCible = int(input("Coordonné pour la cible y : "))
nbrCercles = int(input("Combien y'aura-t-il de cercles ? "))
r = int(input("Rayon du premier cercle : "))
ecart = int(input("Ecart entre les cercles : "))
tracerCible(xCible, yCible, nbrCercles, r, "red", ecart)

cote = int(input("Coté de l'octogone ?"))
tracerOctogone(cote)

nbcPoly = int(input("Nombre de côté du polygone ? "))
cotePoly = int(input("Tailes des côtés du polygone ? "))
tracerPolygone(nbcPoly, cotePoly)

turtle.exitonclick() # ferme la fenêtre lorsqu'on on fait un clic gauche !