import turtle
laki=turtle.Turtle()
laki.shape('turtle')
laki.color('dark blue')
laki.width(2)
laki.speed(100)
for j in range(12):
    for i in range(8):
             laki.forward(100)
             laki.left(360/8)
    laki.left(360/12)
laki.hideturtle()
laki.screen.exitonclick()
#Matin tavakoli
