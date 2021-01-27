import pgzrun

images = [ ]
img1= Actor("Driving",pos= (x,y))
images.append(img1)
img2= Actor (shopping)
images.append(Actor("Sleeping.JPG", pos = (x, y))
images.append(Actor("Shopping.jpeg", pos = (x, y))
images.append(Actor("End.JPG", pos = (x, y))

img1.dx = 2
img2.dy = -1

WIDTH = 600
HEIGHT = 300
Driving = Actor("Driving.JPG")
Driving.pos = (WIDTH, HEIGHT / 2)
speed = 2


def draw():
    screen.fill("yellow")
    Driving.draw()
    Large_box = Rect((100, 100), (400, 300))
   

def on_mouse_down(pos):
    print("position: " + str(pos))
    Driving.angle = Driving.angle_to(pos)
    print("Angle is: " + str(round(Driving.angle)))


def update():
   Driving.x = Driving.x - speed

pgzrun.g3o()