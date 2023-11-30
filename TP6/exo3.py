import turtle # programme principal # ----------------------------------------

LARGEUR=1000 # largeur de la fenêtre
HAUTEUR=500 # hauteur de la fenêtre

def spyrographe(x, y, n, angle, longeur, couleur):
    t.penup()
    t.goto(x,y)
    t.color(couleur)
    t.pendown()
    for i in range(n):
        t.forward(longeur)
        t.left(angle)


turtle.setup(LARGEUR, HAUTEUR) # initialise la taille de l'écran
t = turtle.Turtle() # La tortue se nommera t
t.speed(10) # 1 : vitesse lente de la tortue, 10 vitesse rapide (pas obligatoire !)
spyrographe(0,0,89 ,150,90,"red")
turtle.exitonclick()