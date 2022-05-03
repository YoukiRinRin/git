import turtle

turtle.shape('turtle')
turtle.speed(0)

while True:
    turtle.forward(200)
    turtle.right(90)
    turtle.circle(50)
    turtle.right(125)

    if abs(turtle.pos()) < 1:
        break

turtle.mainloop()