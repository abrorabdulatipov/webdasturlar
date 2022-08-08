#
import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('blue')
t.speed(10)
turtle.bgcolor('black')
size = 1

for _ in range(200):
     t.forward(size)
     t.right(91)
     size += 1


window.mainloop()
#
#
