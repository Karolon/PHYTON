def input_function():
  powers = [0]*10
  fun = input()
  for f in fun.split():
    if f.find("x") == -1:
      value = int(f)
      power = 0
    else:
      place = f.find("x")
      if place == 0:
        value = 1
      else:
        if f[0:place] in ['-','+']:
          value = 1
        else:
          value = int(f[0:place])
      power = int(f[place+2:])
    powers[power] = value
  return powers


def print_function(start = -5, end = 5, skale_down_y = 1, scale_up_x = 20):
  powers = input_function()
  print(powers)
  import turtle as tr
  turtl = tr.Turtle()
  turtl.speed(1000)
  
  y = 0
  for i in range(10):
    y += start**i*powers[i]
  y = y//skale_down_y
  turtl.up()
  turtl.goto(start*scale_up_x,y)
  turtl.down()
  positions = []
  for x in range(start+1,end+1):
    y = 0
    for i in range(10):
      y += x**i*powers[i]
    y = y//skale_down_y
    turtl.goto(x*scale_up_x,y)
    positions.append(y)
    
    
    
  turtl.up()
  turtl.color("grey")
  turtl.goto(start*scale_up_x, 0)
  turtl.down()
  turtl.goto(end*scale_up_x,0)
  turtl.up()
  turtl.goto(0,max(positions))
  turtl.down()
  turtl.goto(0,min(positions))
  turtl.hideturtle()
  
  
print_function()
input()