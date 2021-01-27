import random

WIDTH, HEIGHT = 800, 600
basketball = Actor("basketball")
snake = Actor("snake")
score=0
basketball.speed = 1
game_over = False

def reset_faster():
    basketball.speed += 1
    basketball.x = 0
    basketball.y = random.randint(0, HEIGHT - snake.height)
    
def draw():
  screen.clear()
  screen.draw.text("Score: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 40)
  if (not game_over):
    basketball.draw()
    snake.draw()
  else:
    screen.draw.text("Game Over", center = (WIDTH / 2,HEIGHT / 2), fontsize = 40)

def update():
    global score, game_over
    if (basketball.x < WIDTH):
        basketball.x += basketball.speed
    else:
        game_over = True
        
    if (alien.colliderect(basketball)):
        score += 1
        reset_faster()

def on_mouse_move(pos):
    snake.pos = pos
