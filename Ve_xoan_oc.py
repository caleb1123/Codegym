import turtle

d = 400
bd = 0
while(turtle.distance(0,0)<d):
    bd +=1
    turtle.forward(bd)
    turtle.left(20)
turtle.done