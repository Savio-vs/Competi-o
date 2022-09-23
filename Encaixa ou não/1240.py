while True :
    try :
        repetição = int (input())
        for i in range(repetição):
            v1,v2 = input().split(" ")
            tam_v1 = len(v1)
            tam_v2 = len(v2)
            if tam_v1 >= tam_v2:
                n = tam_v1-tam_v2
                if v1[n:] == v2:
                    
                    print("encaixa")
                else:
                    
                    print("nao encaixa")
            else:
                print("nao encaixa")
    except EOFError:
        break
    except ValueError:
        break