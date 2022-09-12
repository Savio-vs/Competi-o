'''Questão da guarda costeira'''
from math import sqrt

D = []
VF = []
VG= []

while True :
    try:
        D,VF,VG = input().strip().split(' ')
        D = int(D)
        VF = int(VF)
        VG = int(VG)
        
        t_escape = 12/VF

        d_lg = sqrt(pow(D,2)+pow(12,2))
        t_guarda = d_lg /VG

        if t_guarda > t_escape:
            print("N")
        else:
            print("S")
    except EOFError:
        break

