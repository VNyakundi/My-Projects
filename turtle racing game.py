import turtle
import time
import random

WIDTH, HEIGHT = (500,500)
COLORS = ["red","blue","black","purple","cyan","orange","yellow","green","pink","brown"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("enter the number of racers(2-10): ")
        if racers.isdigit:
            racers = int(racers)
        else:
            print("input is not numeric....try again")
            continue

        if 2<=racers<=10:
            return racers
        else:
            print("number is not in range 2-10, try again")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.foward(distance)

            x, y = racer.pos()
            if y >= HEIGHT //2-10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH //2+(i+1)*spacingx, -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle racing")

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
print(colors)

winner = race(colors)
print("the winner is the turtle with color:", winner)
time.sleep(5)




