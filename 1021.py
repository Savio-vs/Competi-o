'''
Leia um valor de ponto flutuante 
com duas casas decimais. Este valor 
representa um valor monetário. A seguir, 
calcule o menor número de notas e moedas 
possíveis no qual o valor pode ser 
decomposto. As notas consideradas são de 
100, 50, 20, 10, 5, 2. As moedas possíveis 
são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas 
necessárias
'''

valor = float(input())
valor_queda = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
moeda = [0,0,0,0,0,0,0,0,0,0,0,0]



for i in range(len(valor_queda)):
    while valor >= valor_queda[i]:
        #print(valor,"taxa de decaimento",valor_queda[i])
        valor = round(valor - valor_queda[i],2)# round arredonda o numero em 2 casas decimais 
        moeda[i] += 1
        # 1894.48


print("NOTAS:")
print("%i nota(s) de R$ 100.00" %moeda[0])
print("%i nota(s) de R$ 50.00" %moeda[1])
print("%i nota(s) de R$ 20.00" %moeda[2])
print("%i nota(s) de R$ 10.00" %moeda[3])
print("%i nota(s) de R$ 5.00" %moeda[4])
print("%i nota(s) de R$ 2.00" %moeda[5])
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" %moeda[6])
print("%i moeda(s) de R$ 0.50" %moeda[7])
print("%i moeda(s) de R$ 0.25" %moeda[8])
print("%i moeda(s) de R$ 0.10" %moeda[9])
print("%i moeda(s) de R$ 0.05" %moeda[10])
print("%i moeda(s) de R$ 0.01" %moeda[11])