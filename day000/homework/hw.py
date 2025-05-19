import turtle

# ეკრანის სეტაპი
screen = turtle.Screen()
screen.bgcolor("skyblue")

# კუს შექმნა
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("burlywood")
pen.speed(3)

# სახლის ძირითადი ფორმა (კვადრატი)
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# სახურავის დახატვა
pen.fillcolor("brown")
pen.begin_fill()
pen.left(45)
pen.forward(141)
pen.right(90)
pen.forward(141)
pen.end_fill()

# კარი
pen.penup()
pen.goto(70, 0)
pen.setheading(90)
pen.pendown()
pen.fillcolor("peru")
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(60)
    pen.right(90)
pen.end_fill()

# ფანჯარა
pen.penup()
pen.goto(20, 120)
pen.setheading(0)
pen.pendown()
pen.fillcolor("lightblue")
pen.begin_fill()
for _ in range(4):
    pen.forward(40)
    pen.right(90)
pen.end_fill()
