import pgzrun
pgzrun.g3o()

WIDTH = 600
HEIGHT = 300
Driving = Actor ("Driving.JPG")
Driving.pos = (WIDTH, HEIGHT / 2)
speed = 2


def draw():
    screen.fill("yellow")
    Driving.draw()


def on_mouse_down(pos):
    print("position: " + str(pos))
    Driving.angle = Driving.angle_to(pos)
    print("Angle is: " + str(round(Driving.angle)))


def update():
   Driving.x = Driving.x - speed


images = [ ]
img1= 'Actor'("Driving",pos= (x,y))
images.append(img1)
img2= 'Actor' (shopping)
images.append(Actor("image2", pos = (x, y))
images.append(Actor("End.JPG", pos = (x, y))


pgzrun.g3o()