import os
import numpy as np
import FuncionesE as fn

os.system("cls")
matriz=np.empty((10,4),type(int))

fn.llenado(matriz)
ruts=[]
depa=0
opc=0
while(opc!=5):
    os.system("cls")
    print("              Casa Feliz             ")
    print("        **********************       ")
    print("1.	Comprar departamento	")
    print("2.	Mostrar departamentos disponibles")
    print("3.	Ver listado de compradores      ")
    print("4.	Mostrar ganancias totales     ")
    print("5.	Salir                           ")

    opc=fn.valiopc()

    if(opc==1):
        tt=fn.tipodepa()
        fn.mostrardis(matriz)
        depa=fn.validadepa()
        comprueba= fn.buscarDisponible(matriz,depa)
        if (comprueba):       
            print("El departamento esta disponible!!")
            pagar=fn.comprardepa(matriz, depa)
            print("\t Usted pagará: ", pagar, " UF")
        else: 
            print("\t El departamento no esta disponible")
        os.system("pause")

    if(opc==2):
        fn.mostrardis(matriz)
        os.system("pause")

    if(opc==3):
        fn.Listado(ruts)
        os.system("pause")

    #if(opc==4):

    if(opc==5):
        fn.salir()
