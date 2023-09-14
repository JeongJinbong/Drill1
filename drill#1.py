import turtle

def movingforward_turtle():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def movingleft_turtle():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def movingright_turtle():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def movingback_turtle():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

    
turtle.shape('turtle')

turtle.onkey(movingforward_turtle, 'w')
turtle.onkey(movingleft_turtle, 'a')
turtle.onkey(movingright_turtle, 'd')
turtle.onkey(movingback_turtle, 's')
turtle.onkey(restart, 'Escape')
turtle.listen()
