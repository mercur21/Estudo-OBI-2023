import math
p1 = str(input())
p2 = str(input())

p1 = p1.split(" ")
p2 = p2.split(" ")

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

distancia = ((x2 - x1)**2) + ((y2 - y1)**2)
distancia = math.sqrt(distancia)
print('{:.4f}'.format(distancia))