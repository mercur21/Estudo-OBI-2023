#           (0)   1    2    3   (4)   5    6    7   (8)   9   10   11   12   13   (14)  15   16   17   18   19  (20)  21   22   23                                           
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]

a = alfabeto.index("a") #0
e = alfabeto.index("e") #4
i = alfabeto.index("i") #8
o = alfabeto.index("o") #14
u = alfabeto.index("u") #20


while True:
     P = str(input())
     if len(P) < 30 and len(P) >= 1:
         break

P1 = list(P)

for i in range(len(P1)):
    if P1[i] in consoantes:
        x = alfabeto.index(P1[i])
        if x == 1 or x == 2 or x == 22:
            x1 = 0 #a
        if x == 3 or x == 5 or x == 6:
            x1 = 4 #e
        if x == 7 or x == 9 or x == 10 or x == 11:
            x1 = 8 #i
        if x == 12 or x == 13 or x == 15 or x == 16 or x == 17:
            x1 = 14 #o
        if x == 18 or x == 19 or x == 21 or x == 22:
            x1 = 20 #u    
        x2 = x + 1 
        if x == 23: #z
            x2 = 23 #z
        P1[i] += alfabeto[x1] + alfabeto[x2]


print("".join(P1))