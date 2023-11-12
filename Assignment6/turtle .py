import turtle

turtle.bgcolor("red")
pen = turtle.Pen()

t = 2
m = int(360 / t)
i = 5
pen.shape("turtle")
pen.shapesize(0.75)
for i in range(50,100):
    for j in range(t):
        pen.pencolor("blue")
        pen.forward(i)
        pen.left(m)
        m = int(360 / t)
    i+=10  
    t = t + 1