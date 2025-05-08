import random as ran
import turtle as tr

r = 100


żółć = tr.Turtle()
żółć.goto(0,0)
żółć.down()
for i in range(5):
  żółć.forward(r)
  żółć.left(90)

żółć.speed(100000000000)


żółć.circle(r,90)
żółć.up()
points_in_circle = 0

points = 1000
for i in range(1000):
  x = ran.randint(0,r)
  y = ran.randint(0,r)
  if x**2 + y**2 < r**2:
    żółć.color("blue")
    points_in_circle+=1
  else:
    żółć.color("green")
  żółć.goto(x,y)
  żółć.dot(5)
  
print(points_in_circle/points*4)
input()