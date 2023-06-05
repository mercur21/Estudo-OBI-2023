l1 = str(input())
l2 = str(input())

l1 = l1.split(" ")
l2 = l2.split(" ")

n1 = float(l1[1]) # quantidade
v1 = float(l1[2]) # valor

n2 = float(l2[1]) # quantidade
v2 = float(l2[2]) # valor

total = (n1 * v1) + (n2 * v2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))