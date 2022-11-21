import turtle

turtle.speed(0)
r = 150
colors = ["red","yellow", "blue", "green", "brown", "violet"]
for i in range(0,360,10):
    turtle.right(10)
    cnt = 0
    turtle.color(colors[1//10%len(colors)])
    while (cnt < 2):
        turtle.circle(r,90)
        turtle.circle(r//2, 90)
        cnt += 1
turtle.done()