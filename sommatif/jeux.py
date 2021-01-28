# <en-tête>
#Marceline Tambwe, tammar28@ecolecatholique.ca
#2020-01-28

#ajout les fonctions addictionel
import pgzrun
import random

# set the size of the screen
WIDTH, HEIGHT = 800, 600

#Cree des objet 
basketball = Actor("basketball")
snake = Actor("snake")

#La vitesse
# (les valeurs de départ pour les variables du jeu)
score=0
basketball.speed = 1
game_over = False


#Définir une fonction qui...
def reset_faster():
    basketball.speed += 1 # = basketball.speed + 1
    basketball.x = 0
    basketball.y = random.randint(0, HEIGHT)

# Définir une fonction qui est utiliser pour l'animation 
def draw():
  screen.clear()
  screen.draw.text("Score: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 40)
  if (not game_over):
    basketball.draw()
    snake.draw()
  else:
    screen.draw.text("Game Over", center = (WIDTH / 2,HEIGHT / 2), fontsize = 40)

# Définir une fonction qui est...  
def update():
    global score, game_over
    if (basketball.x < WIDTH):
        basketball.x += basketball.speed
    else:
        game_over = True
        
    if (snake.colliderect(basketball)):
        score += 1
        reset_faster()

# Définir une fonction qui fait bouger l'objet
def on_mouse_move(pos):
    snake.pos = pos

#
pgzrun.go()