import turtle

#----------------------------------------------- drawing --------------------------------------------
# draw a line
def drawLine(x1, y1, x2, y2, color):
    # TODO
    t.penup()
    t.pencolor(color)
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.pencolor("black")
    
# draw a frame (orthonormal)
def drawFrame(color):
    h=HEIGHT/2-20
    w=WIDTH/2-20
    drawLine(0, -h, 0, h, color)
    drawLine(-w, 0, w, 0, color)

# draw the points of a curve 
def drawCurve(coord):
    # TODO
    for i in range(0, len(coord)):
        x=coord[i][0]*UNITE
        y=coord[i][1]*UNITE
        if(x>-WIDTH/2 and x<WIDTH/2) and (y>-WIDTH/2 and y<WIDTH/2):
            # draw the point if it is into the turtle screen
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(3)

# eval evaluate expressions
# ex of expressions : 'x*(x+1)*(x+2)', 'x+1' 
# ex : eval("(x**2+1)/(x**2-1)", {"x":5})
def calculatePlots(expr, xmin, xmax, step):
    coord=[] # coord will contains the coordinates of each point of the curve 
    x=xmin
    while(x<=xmax):
        coord.append([round(x,1), round(eval(expr, {"x": x}),1)])
        x=x+step
    return coord

#-------------------------------------- menu functions --------------------------------------------
# frame around a string 
def frame(title):
    lg=len(title)
    print("+-", end="")
    for i in range(1, lg+1):
        print("-", end="")
    print("-+")
    print("| ", end="")
    print(title, end="")
    print(" |")
    print("+-", end="")
    for i in range(1, lg+1):
        print("-", end="")
    print("-+")

# display a menu
def settingsMenu():
    frame("  Settings menu  ")
    print(f"1. Set the interval of values on the abscissa [{xmin}, {xmax}])")
    print(f"2. Set the size of interval between two graduations (default {step})")
    print(f"3. Set the color to draw the curve (default {colorC})")
    print("4. Reinit to default settings ")
    print("5. Quit settings")
    choice=int(input("Choice ? "))
    return choice

# modify settings
def modifySettings():
    choice=settingsMenu()    
    while(choice!=5):
        if(choice==1):
            print(f"L'axe des abscisses s'étend entre [{XMIN}, {XMAX}]")
            xmin=int(input("xmin ? "))
            xmax=int(input("xmax ? "))
        elif(choice==2):
            step=float(input(f"Step between each point to calculate (default, {STEP}) ? ")) 
        elif(choice==3):
            colorC=input(f"Color of the plots of the curve (default, {COLOR}) ? ")
            t.pencolor(colorC)
        elif(choice==4): 
            step=STEP
            xmin=XMIN
            xmax=XMAX
        else:
            print("Invalid choice. Retry !")
        choice=settingsMenu()    

# display a menu
def menu():
    frame("Menu")
    print("1. Draw a curve f(x)")
    print("2. Clear the screen")
    print("3. Settings")
    print("4. Save last curve")
    print("5. Load all curves")
       # TODO
    print("9. Quit")
    choice=int(input("Choice ? "))
    return choice

def saveCurve(expr, xmin, xmax, step, color):
    fic = open("./graph.plot", "w")
    fic.write(expr + ';' + xmin + ';' + xmax + ';' + step + ';' + color + "\n")
#-------------------------------- saving curves and loading curves from files --------------------------------
# TODO : add the code of saveCurve function
# Save curve in a file

# TODO : add the code of loadAllCurves function
# load curves in the screen


# TODO : load one curve among all curves

   

# TODO : display all expressions in the file 


# ---------------------------------------------------------------------------------------------------------------------
#                                             Main program
# ---------------------------------------------------------------------------------------------------------------------
# constants, default values
WIDTH=1000 # window width 
HEIGHT=500 # window height
UNITE=20 # size in pixel between two graduations on the frame
STEP=0.2 # a point calculated each 0.2 (ex : xmin = 1, then we compute points 1, 1.2, 1.4, 1.6 etc.)
COLOR="blue"
# points to display are calculated between XMIN and XMAX 
XMAX=(WIDTH-20)/2/UNITE
XMIN=-XMAX
FILE="./graph.plot"

# initialize variables with default values
step=STEP
xmin=XMIN
xmax=XMAX
colorC=COLOR

turtle.setup(WIDTH, HEIGHT) # initialize the size of the screen
t=turtle.Turtle() # turtle named t
t.speed(6)
drawFrame("black")

frame("GraphPlot")
choice=menu()
while(choice!=9):
    if(choice==1):
        expr=input("Entrez l'expression de la fonction f(x) ? ")
        coord=calculatePlots(expr, xmin, xmax, step)
        drawCurve(coord)    
    elif(choice==2): 
        if(t):
            t.clear()
            drawFrame("black")
        print("Screen cleared")
    elif(choice==3): 
        modifySettings()
    #elif(choice==4): 
        # TODO
    #elif(choice==5): 
        # TODO
    else:
        print("Invalid choice. Retry !")
    choice=menu()
print("Bye !")
