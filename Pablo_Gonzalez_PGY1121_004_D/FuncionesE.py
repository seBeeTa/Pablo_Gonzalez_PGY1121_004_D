import os
import numpy as np

def llenado(pp):
    p=1
    for i in range(10):
        for j in range(4):
            pp[i,j]=p 
            p+=1 

def valiopc():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 6")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp 

def mostrardis(m):
    os.system("cls")
    aux=1
    print("Piso ", end="")
    print("\tA|\tB|\tC|\tD")
    for i in range(10):
        print("\n", aux)
        aux+=1
        for j in range(4):
            if(j==1):
                print("\t", m[i,j], end=" ")
            else:
                print("\t", m[i,j], end=" ")
    print("\n")
    os.system("pause")

def validadepa():
    depa=0
    while True:
        try: 
            depa=int(input("Ingrese el número de departamento 1-40\n"))
            if (depa>=1 and depa<=40):
                break
            else:
                print(" Error.. ingrese departamento entre  1 y 40")
        except ValueError:
            print(" Error.. ingrese departamento entre  1 y 40")
    return depa

def tipodepa():
    os.system("cls")
    tipo=""
    while(len(tipo)<=0):
        print("(A)")
        print("(B)")
        print("(C)")
        print("(D)")
        print()
        tipo=input("   Elija el tipo de departamento:\n")
        if(tipo!="A" and tipo!="B" and tipo!="C" and tipo!="D"):
            print("Debe ingresar una opcion correcta")
            tipo=""
    return tipo 

def comprardepa(matriz, depa, ruts,aa ):
    for i in range(13):
        for j in range(8):
            if(depa==aa[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Rut debe tener 8 digitos minimo "))
                            if(rut<9999999):
                                print("Error, debe tener 8 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(ruts)>0): 
                        sw=0
                        for y in range(len(ruts)):
                            if(rut==ruts[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya existe y no se puede agregar el comprador")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
                aa[i,j]=0
            if (matriz[j,i]==depa):
                matriz[j,i]=0          
                if i==0:
                    pago=3800
                if i==1:
                    pago=3000
                if i==2:
                    pago=2800
                if i==3:
                    pago=3500
    return pago

def buscarDisponible(matriz, depa):
    for x in range(10):
        for i in range(4):
            if (depa==matriz[x,i]):
                return True

def Listado(r):
    r.sort()
    print("Listado de pasajeros del avión ordenados de menor a mayor ")
    print("\t",r)

def salir():
    print("Pablo Gonzalez")
    print("11-07-2023")