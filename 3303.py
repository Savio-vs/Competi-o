while True:
    try :
        entrada = input()
        tam  = len(entrada)
        if tam >= 10:
            print("palavrao")
        else:
            print("palavrinha")

    except EOFError:
        break