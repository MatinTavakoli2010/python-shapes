import turtle
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('dark blue')
laki.width(0.5)
laki.speed(100)
for j in range(8):
    for x in range(20,151,5):
        for i in range(4):
            laki.forward(x)
            laki.right(90)
        laki.right(45)
laki.hideturtle()
laki.screen.exitonclick()
#Matin tavakoli
