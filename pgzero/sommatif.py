import pgzrun
import math


WIDTH = 600
HEIGHT = 300
bird = Actor("bird.jpg")
bird.pos = (WIDTH, HEIGHT / 2)
speed = 2


def draw():
    screen.fill("blue")
    bird.draw()


def on_mouse_down(pos):
    print("position: " + str(pos))
    bird.angle = bird.angle_to(pos)
    print("Angle is: " + str(round(bird.angle)))


def update():
   bird.x = bird.x - speed


pgzrun.go()