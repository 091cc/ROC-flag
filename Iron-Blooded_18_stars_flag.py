import turtle as t 
import math

t.speed(0)

# red rectangle（red, 240 x 150）
t.penup()
t.color("red")
t.goto(-120, -75)
t.pendown()
t.begin_fill()
for _ in range(2):
    t.forward(240)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

# nonagram (black)
t.penup()
t.color("black")
t.goto(0, 66)
t.pendown()
t.begin_fill()
for i in range(9):
    t.goto((66 * math.cos(math.radians(90 - i * 40))), (66 * math.sin(math.radians(90 - i * 40))))
    t.goto((18 * math.cos(math.radians(90 - i * 40 - 20))), (18 * math.sin(math.radians(90 - i * 40 - 20))))
t.goto(0, 66)
t.end_fill()

# 4. yellow circles (yellow, diameter 12)
t.color("yellow")
for i in range(9):
    # outer circle yellow star
    t.penup()
    t.goto((66 * math.cos(math.radians(90 - i * 40))), (66 * math.sin(math.radians(90 - i * 40))) - 6)
    t.pendown()
    t.begin_fill()
    t.circle(6)
    t.end_fill()
    
    # inner circle yellow star
    t.penup()
    t.goto((18 * math.cos(math.radians(90 - i * 40 - 20))), (18 * math.sin(math.radians(90 - i * 40 - 20))) - 6)
    t.pendown()
    t.begin_fill()
    t.circle(6)
    t.end_fill()

t.hideturtle()
t.done()