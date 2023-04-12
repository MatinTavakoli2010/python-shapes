import turtle
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('dark blue')
laki.width(2)
laki.speed(10)
for j in range(8):
    for i in range(4):
        laki.forward(50)
        laki.right(90)
    laki.right(45)
laki.hideturtle()
laki.screen.exitonclick()
#Matin tavakoli
