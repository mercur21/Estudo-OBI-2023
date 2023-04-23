# Cibele > Camila | Celeste < Camila.

c1 = int(input()) 
c2 = int(input()) 
c3 = int(input()) 

if c2 > c1 and c1 > c3 or c1 == c2 and c2 == c3 or c1 > c2 and c3 > c2:
    x = c1
if c2 > c1 and c2 < c3 or c2 < c1 and c2 > c3 or c1 < c2 and c2 == c3:
    x = c2
if c3 > c2 and c3 < c1 or c1 == c3 and c2 != c1 or c1 < c3 and c2 > c1 and c3 < c2:
    x = c3
if c1 == c2 and c1 > c3:
    x = c1

print("------------")
print(x)

