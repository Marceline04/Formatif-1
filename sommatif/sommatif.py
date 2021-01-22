import math
WIDTH = 500
HEIGH = 300
bird = 'Actor'("bird.png")
bird.pos = (WIDTH, HEIGH/2)
speed = 1 # nombre de pixels par update()

def draw():
   'screen'.fill("red")
   bird.draw()

def on_mouse_down(pos):
   print("position: " + str (pos) )
   bird.angle = bird.angle_to(pos)
   print ("Angle is: " + str(round(bird.angle)))

def update():
    angle_radians = math.radians(bird.angle)
    bird.x += speed * round(math.cos(angle_radians))
    bird.y += speed * -round(math.sin(angle_radians))