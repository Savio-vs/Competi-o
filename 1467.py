arq = open("teste.txt")
#entrada = input().strip().split('\n')
#linha = arq.read().split('\n')

while True:
  try:
    linha = input()
    if linha == '1 0 0' or linha == '0 1 1':
        print("A")
    elif linha == '0 1 0' or linha == '1 0 1':
        print("B")
    elif linha == '0 0 1' or linha == '1 1 0':
        print("C")
    else:
        print("*")

  except EOFError:
    break
'''valor = []

for i in range(len(linha)):
    a,b,c= linha[i].split(' ')
    valor.append(a)
    valor.append(b)
    valor.append(c)'''
