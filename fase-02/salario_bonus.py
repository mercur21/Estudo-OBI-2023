nome = str(input()) #nome vendedor
A = float(input()) #salário fixo
B = float(input()) #total de vendas
total = A + ((B * 15) / 100) #total a receber

print('TOTAL = R$ {:.2f}'.format(total))