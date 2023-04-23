soma = []
x = 0

while True:
    x +=1
    n = int(input())
    soma.append(n)
    if n == 0 and len(soma) > 1:
        soma.pop(-1)
        soma.pop(-1)
    if x == 11:
        break

if len(soma) >= 1:
    soma.pop(0)

print("----------------------")
print(sum(soma))