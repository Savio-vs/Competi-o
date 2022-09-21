
def dec (x):# recebi binario
    valor = 0
    for i in range(len(x)):
        if x[-(i+1)] != '0':#inicia a leitura de tras para frente
            valor = valor + pow(2,i)
    return valor

def hex (x): #recebe binario
    tabela_hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    tam = len(x)
    tam = int(tam/4)
    entrada_interira = int(x)
    blocos_bin = []
    valor = ""
# dividi o binario recebido em blocos de 4 bits
# e envia para a função dec, recebendo seu valor 
# decimal respectivo, e identificando esse valor 
# na tabela de hexadecimal.
    for i in range(tam+1):
        blocos_bin.append(entrada_interira%10000)
        blocos_bin[i] = dec(str(blocos_bin[i]))
       
        if blocos_bin[i] == 0 and i==(tam) :
            pass
        else:    
            valor = valor + tabela_hex[blocos_bin[i]]
        entrada_interira = entrada_interira // 10000

    valor = valor[::-1]  
      
    return valor

def bin(x):# recebi decimal
    x = int(x)
    valor = ""
# conversão para base 2
    while x> 1:
        valor = valor + str(x%2)
        x = x//2
        if x == 1:
            valor = valor + str(x)
# invertendo a string da variavel valor, 
# para representar o real valor do binario.    
    valor = valor[::-1] # 
    return valor
def hex_bin (x):# recebi hexadecimal
    tabale_bin={
    "0":"0000","1":"0001","2":"0010","3":"0011",
    "4":"0100","5":"0101","6":"0110","7":"0111",
    "8":"1000","9":"1001","a":"1010","b":"1011",
    "c":"1100","d":"1101","e":"1110","f":"1111"
    }
    valor=""
    for i in range(len(x)):
        if i == 0:
            valor = tabale_bin[x[i]]
            valor = int (valor)
            valor = str(valor)
        elif x[i] in tabale_bin:
            valor = valor + tabale_bin[x[i]]
    return valor
while True:
    try:
        repeticao = int(input())
        for i in range(repeticao) :
            caso = input().strip().split(" ")
            if caso[1] == 'bin':
                valor = caso[0]
                print(f"Case {i+1}:")
                decimal = dec(valor)
                print(f"{decimal} dec")
                hexa = hex(valor)
                print(f"{hexa} hex\n")
             
            elif caso[1] == 'dec':
                valor = caso[0]
                print(f"Case {i+1}:")
                binario = bin(valor)
                hexa = hex(binario)
                print(f"{hexa} hex")
                print(f"{binario} bin\n")
                
            elif caso[1] == 'hex':
                valor = caso[0]
                print(f"Case {i+1}:")
                binario = hex_bin(valor)
                decimal = dec(binario)
                print(f"{decimal} dec")
                print(f"{binario} bin\n")
           
    except EOFError:
        break