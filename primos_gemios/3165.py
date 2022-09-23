
entrada = int(input())
primos = []
        
while entrada >0 :
    cont = 0
    for i in range (entrada):
        if entrada % (i+1) == 0 :
            cont +=1
    if cont ==2 :
        print(f"numeros primos {entrada}")
        primos.append(entrada)
    if len(primos) > 2:
        for i in range(len(primos)):
            if (i+1) < len(primos) :
                if (primos[i] - 2) == primos[i+1] :
                    print(primos[i+1],primos[i])
                    exit()

    entrada-=1