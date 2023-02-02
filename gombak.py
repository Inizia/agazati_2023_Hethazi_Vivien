from Gomba import Gomba

gombak_lista =[]

def beolvasas():
    gombak_fajl = open("gombak_jav.txt","r", encoding="utf-8")
    gombak_fajl.readline()
    lista = gombak_fajl.readlines()
    gombak_fajl.close()

    print(lista)

    i = 0
    while i < len(lista):
        sor = lista[i].strip().split("@")
        print(sor)
        gombak_lista.append(Gomba.sor)
        i += 1
    print((gombak_lista[2]).nev)



