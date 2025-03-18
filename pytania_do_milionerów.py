file = open('odp.txt', 'w')

question = []
correct = []
wrong = []
que= []
a = ''
while a != 'y':
  q = []
  q.append(input('Treść pytania:\n'))
  q.append(input('Poprwana odp:\n'))
  d = []
  d.append(input('Zła odp1:\n'))
  d.append(input('Zła odp2:\n'))
  d.append(input('Zła odp3:\n'))
  q.append(d)

  que.append(q)
  
  a = input("wszystko?")























file.close()