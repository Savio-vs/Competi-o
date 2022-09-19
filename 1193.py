
def dec (x):# recebi binario
    valor = 0
    for i in range(len(x)):
        if x[-(i+1)] != '0':#inicia a leitura de tras para frente
            valor = valor + pow(2,i)
    return valor
def hex (x): #recebe binario
    tam = len(x)
    tam = int(tam/4)
    blocos_bin = []
    i=0
    while i < tam:
        j=i+4
        blocos_bin.append(x[i:j:-1])
        
    print(blocos_bin)
def bin(x):# recebi decimal
    
    return x

while True:
    try:
        repeticao = int(input())
        for i in range(repeticao) :
            caso = input().strip().split(" ")
            if caso[1] == 'bin':
                valor = caso[0]
                print(f"Caso {i}")
                #dec(valor)
                hex(valor)
                #print(f"{valor} dec")
             
            elif caso[1] == 'dec':
                valor = caso[0]
                print(f"Caso {i}")
                
            elif caso[1] == 'hex':
                valor = caso[0]
                print(f"Caso {i}")
                
            else:
                print('Erro de formatação')
    except EOFError:
        break