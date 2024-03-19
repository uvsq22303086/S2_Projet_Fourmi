#Code inspiré du site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/langton/langton.html

#GRILLE:
import tkinter as tk
SIDE = 500
WIDTH = SIDE
HEIGHT = SIDE
DIM = 20
UNIT = SIDE // DIM
COLOR_OFF = 'snow'
COLOR_ON = 'gray16'

def make_grid():
    for j in range(nwidth):
        cnv.create_line((j * UNIT, 0), (j * UNIT, HEIGHT))
    for i in range(nheight):
        cnv.create_line((0, i * UNIT), (WIDTH, i * UNIT))


root = tk.Tk()
cnv = tk.Canvas(root, width=WIDTH, height=HEIGHT,
             background=COLOR_OFF)
cnv.pack()

nwidth = WIDTH // UNIT
nheight = HEIGHT // UNIT

make_grid()


#items[i][j]= plateau dessiner par deplacement de la fourmi, 
#items==0 case blanche = déplacement droite
#pos=position de la fourmi (i,j)
#drn = direction N=Nord,S=Sud,E=Est,O=Ouest
#r = nouvelle position de la fourmi

#Fonction qui détermine la nouvelle position et direction de la fourmi
def bouger ( pos,drn,items):
    i,j=pos
    if items[i][j]==0:
        if drn =='N':
            r= (i,j+1), 'E'#j+1 monte vers le haut et je tourne à droite soit l'est
        elif drn=='S':
             r= (i, j-1), 'O' #j-1 descend case du bas et je tourne à droite soit l'ouest
        elif drn == 'E':
            r= (i+1,j),'S' # i+1 je tourne vers l'est et je tourne à droite soit le sud
        elif drn == 'O':
            r= (i-1,j), 'N' # i-1 je tourne vers l'ouest et je tourne à droite soit le nord
    else: #La case tombée est noir => tourne à gauche ( inverse coordonée case clair)
        if drn == 'N':
            r = (i,j-1),'O' #Je tourne à gauche
        elif drn == 'S':
            r = (i,j+1), 'E'
        elif drn == 'E':
            r = (i-1,j),'N'
        elif drn == 'O':
            r= ( i+1,j),'S'
    return r
grille = tk.Tk()
canvas=tk.Canvas(grille,bg=Color_OFF, height=HEIGHT, width=WIDTH)
canvas.pack(side='left')



#Fonction qui change l couleur de la case actuelle
def case_courante(i,j):
    if (i+j)%2 == 0:#Si la case est blanche
        couleur = Color_ON
    else : 
        couleur = Color_OFF  #Si la case est noir elle devient blanche
    carré = canvas.create_rectangle((i * largeur_case, j * hauteur_case),
                                     ((i + 1) * largeur_case, (j + 1) * hauteur_case), fill=couleur)
    return carré

#Fonction qui dessine les cases
#ndrn=r de la fonction bouger =  nouvelle pos et direction
def dessin(pos,drn,items):
    (ii,jj),ndrn = bouger(pos, drn,items)
    i,j=pos
    carré= items[i][j]

    if carré == 0 : #Case claire
        carré= dessin(i,j)
        items[i][j] = carré
    else : #Case noire, le carré sombre est supprimé
        canvas.delete(carré)
        items[i][j] = 0
    return (ii,jj),ndrn


#Il manque l'animation de la fourmi, la fourmi, et les touches de contrôle pour créer le mouvement


#Interface graphique crée



#fourmi : le code est inspiré du cite : https://rosettacode.org/wiki/Langton%27s_ant#Python

def fourmi(width, height, max_nb_steps):
    grid = [[" "] * width for _ in range(height)]

    # Position initiale de la fourmi
     x = width // 2 
     y = height // 2
    direction = "haut"
i = 0

# Boucle principale
while i < max_nb_steps and 0 <= x < width and 0 <= y < height:
       
        invert_color(grid, x, y)
        direction = next_direction(grid, x, y, direction)   
    
    # Affichage de la grille actuelle
          x, y = next_position(x, y, direction)
    
        print_grid(grid)

 # Incrément du compteur d'étapes
        i += 1


root.mainloop() #lancemant de la boucle IL FAUT LE LAISSER A LA FIN


