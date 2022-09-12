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
N1=0 
N2=0 
N3=0
N4=0
N5=0
N6=0
M1=0
M2=0
M3=0
M4=0
M5=0
M6 = 0 

while (valor - 100) >= 0:
    valor = valor -100 
    N1 += 1

while (valor -50) >= 0:
    valor = valor -50
    N2 += 1

while (valor - 20) >= 0:
    valor = valor -20
    N3 += 1
while (valor -10) >= 0:
    valor = valor -10
    N4 += 1
while (valor -5) >= 0:
    valor = valor -5
    N5 += 1
while (valor -2) >= 0:
    valor = valor -2
    N6 += 1

while (valor - 1) >= 0:
    valor = valor - 1
    M1 += 1
while (valor -0.5) >= 0:
    valor = valor -0.5
    M2 += 1
while (valor -0.25) >= 0:
    valor = valor -0.25
    M3 += 1
while (valor -0.10) >= 0:
    valor = valor -0.10
    M4 += 1
while (valor -0.05) >= 0:
    valor = valor -0.05
    M5 += 1
while (valor -0.01) >= 0:
    valor = valor -0.01
    M6 += 1
print("NOTAS:")
print("%i nota(s) de R$ 100.00" %N1)
print("%i nota(s) de R$ 50.00" %N2)
print("%i nota(s) de R$ 20.00" %N3)
print("%i nota(s) de R$ 10.00" %N4)
print("%i nota(s) de R$ 5.00" %N5)
print("%i nota(s) de R$ 2.00" %N6)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" %M1)
print("%i moeda(s) de R$ 0.50" %M2)
print("%i moeda(s) de R$ 0.25" %M3)
print("%i moeda(s) de R$ 0.10" %M4)
print("%i moeda(s) de R$ 0.05" %M5)
print("%i moeda(s) de R$ 0.01" %M6)