import turtle
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('dark blue')
laki.width(0.5)
laki.speed(100)
for j in range(8):
    for x in range(10,141,5):
        for i in range(8):
            laki.forward(x)
            laki.right(360/8)
        laki.right(45)
laki.hideturtle()
laki.screen.exitonclick()
#Matin tavakoli
