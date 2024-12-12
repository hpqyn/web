import turtle

turtle.bgcolor("#9870db")
turtle.pensize(3)

a = turtle.Turtle()
a.penup()
a.goto(-200,60)
a.pendown()
a.color("red")
style = ('courier',30,'italic')
a.write('I',font=style,align='left')
a.hideturtle()

def curve():
	for i in range(200):
		turtle.right(1)
		turtle.forward(1)

turtle.speed(0)
turtle.color("red","pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.0)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()


a.penup()
a.goto(-15,75)
a.pendown()
a.color("red")
style = ('courier',10,'italic')
a.write('LOVE',font=style,align='left')
a.hideturtle()


a.penup()
a.goto(180,60)
a.pendown()
a.color("red")
style = ('courier',15,'italic')
a.write('ZYN',font=style,align='left')
a.hideturtle()


a.penup()
a.goto(-150,-130)
a.pendown()
a.color("red")
style = ('courier',30,'italic')
a.write('SO MUCH...😆',font=style,align='left')
a.hideturtle()

turtle.done()