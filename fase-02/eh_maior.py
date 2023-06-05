A = str(input())
A = A.split(" ")

a = float(A[0])
b = float(A[1])
c = float(A[2])

maiorAB = (a + b + abs(a -b)) / 2
maiorXC = (maiorAB + c + abs(maiorAB - c)) / 2

print(f"{int(maiorXC)} eh o maior")