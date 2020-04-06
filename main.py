import turtle
import random
import os

win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgpic("space_invaders_background.gif")

# REGISTER SHAPES
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# FOR BORDER
bd_pen = turtle.Turtle()
bd_pen.speed(0)
bd_pen.color("white")
bd_pen.penup()
bd_pen.setposition(-300, -300)
bd_pen.pendown()
bd_pen.pensize(4)

for side in range(4):
    bd_pen.fd(600)
    bd_pen.left(90)
bd_pen.hideturtle()

# SCORE
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
Score = "Score : %s" % score
score_pen.write(Score, False, align="left", font=("Courier", 15, "normal"))
score_pen.hideturtle()

# PLAYER
player = turtle.Turtle()
player.color("Red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# NO. OF INVADERS
number_inv = 3
invaders = []
for i in range(number_inv):
    invaders.append(turtle.Turtle())

# INVADER
for inv in invaders:
    inv.color("Blue")
    inv.shape("invader.gif")
    inv.speed(0)
    inv.penup()
    x1 = random.randint(-200, 200)
    y1 = random.randint(100, 250)
    inv.setposition(x1, y1)

inv_speed = 10

# BULLET

bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("white")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 30


# MOVEMENT OF PLAYER


def player_left():
    x = player.xcor()

    # BORDER CHECK
    if x < -265:
        x = -265
    x -= 20
    player.setx(x)


def player_right():
    x = player.xcor()
    x += 20

    # BORDER CHECK
    if x > 280:
        x = 280
    player.setx(x)


# MOVEMENT OF BULLET

def fire():
    global bullet_state
    if bullet_state == "ready":
        os.system("afplay laser.wav&")
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def collision(t1, t2):
    if bullet.distance(inv) < 15:
        return True

    else:
        return False


def collision_1(a1, a2):
    if inv.distance(player) < 15:
        return True
    else:
        return False


# BULLET STATE

bullet_state = "ready"

# KEYBOARD BINDING

win.listen()
win.onkeypress(player_left, "Left")
win.onkeypress(player_right, "Right")
win.onkeypress(fire, "space")

# GAME LOOP
while True:
    win.update()
    for inv in invaders:

        # INVADER MOVEMENT
        x = inv.xcor()
        x += inv_speed
        inv.setx(x)

        if inv.xcor() > 280:
            # MOVE ALL INVADERS DOWN
            for j in invaders:
                y = j.ycor()
                y -= 40
                j.sety(y)
            # CHANGE DIRECTION
            inv_speed *= -1

        if inv.xcor() < -275:
            # MOVE ALL INVADERS DOWN
            for j in invaders:
                y = j.ycor()
                y -= 40
                j.sety(y)
            # CHANGE DIRECTION
            inv_speed *= -1

            # CHECK TO SEE THE POSITION OF BULLET
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bullet_state = "ready"

        # COLLISION BETWEEN BULLET AND INVADER
        if collision(bullet, inv):
            os.system("afplay explosion.wav&")
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            x1 = random.randint(-200, 200)
            y1 = random.randint(100, 250)
            inv.setposition(x1, y1)
            # SCORE UPDATION
            score += 10
            Score = "Score : %s" %score
            score_pen.clear()
            score_pen.write(Score, False, align="left", font=("Courier", 15, "normal"))

        # COLLISION BETWEEN INVADER AND PLAYER
        if collision_1(inv, player):
            os.system("afplay explosion.wav&")
            player.hideturtle()
            inv.hideturtle()
            print("Game OVER !!!")

    # BULLET MOVEMENT

    y = bullet.ycor()
    y += bullet_speed
    bullet.sety(y)
