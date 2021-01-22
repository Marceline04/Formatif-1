import pgzrun
import math


WIDTH = 600
HEIGHT = 300
bird = Actor("bird.jpg")
bird.pos = (WIDTH, HEIGHT / 2)
speed = 1 


def draw():
    screen.fill("red")
    bird.draw()


def on_mouse_down(pos):
    print("position: " + str(pos))
    bird.angle = bird.angle_to(pos)
    print("Angle is: " + str(round(bird.angle)))


def update():
    angle_radians = math.radians(bird.angle)
    bird.x += speed * round(math.cos(angle_radians))
    bird.y += speed * -round(math.sin(angle_radians))


pgzrun.go()