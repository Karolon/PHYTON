
x=int(input())
y=[]
i=x
while x != 0:
  if 2^i <= x:
    x=x-2^i
    y.append(1)
  else:
    y.append(0)
  print(y)
  i-=1
print(y)
