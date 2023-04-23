# Cibele > Camila | Celeste < Camila.

c1 = input("Digite a idade de uma das irmãs: ") #2
c2 = input("Digite a idade de uma das irmãs: ") #1
c3 = input("Digite a idade de uma das irmãs: ") #2

if c2 > c1 and c1 > c3 or c1 == c2 and c2 == c3 or c1 > c2 and c3 > c2:
    x = c1
if c2 > c1 and c2 < c3 or c2 < c1 and c2 > c3 or c1 < c2 and c2 == c3:
    x = c2
if c3 > c2 and c3 < c1 or c1 == c3 and c2 != c1 or c1 < c3 and c2 > c1 and c3 < c2:
    x = c3
if c1 == c2 and c1 > c3:
    x = c1
    
print(f"A idade de Camila é: {x} anos.")

