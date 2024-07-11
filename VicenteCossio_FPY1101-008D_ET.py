import csv 
import os
import time
import random


os.system("cls")

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]



def asignar_sueldos():
    trabajadores2=[]
    for laburantes in trabajadores:
        precio= random.randint(300000, 2500000)
        trabajadores2.append((laburantes,precio))
    return trabajadores2

trabajadores2=[]


def clasificacion(trabajadores2):
    menores80000=[]
    entre800y2000=[]
    mayora2500000=[]
    for trabajadores23 in trabajadores2:
        if trabajadores23[1] < 800000:
            menores80000.append(trabajadores23)
        elif 800000 <= trabajadores23[1] <= 2000000:
            entre800y2000.append(trabajadores23)
        else:
            mayora2500000.append(trabajadores23)
    return menores80000, entre800y2000,mayora2500000


def guardado(trabajadores2, archivo_csv='sueldosguardados.csv'):
    with open(archivo_csv, 'w', newline='') as archivo:
        campos = ["Nombre", "Sueldo", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"]
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)
        escritor_csv.writeheader()

        for trabajadores23 in trabajadores2:
            descuento_afp = trabajadores23[1] * 0.12
            descuento_salud = trabajadores23[1] * 0.07
            sueldo_liquido = (trabajadores23[1] - descuento_afp - descuento_salud) * trabajadores23[2]
            escritor_csv.writerow({
                'Nombre': trabajadores23[0],
                'Sueldo': trabajadores23[1],
                'Descuento Salud': descuento_salud,
                'Descuento AFP': descuento_afp,
                'Sueldo Liquido': sueldo_liquido
                })



def promedio(trabajadores2):
    total_precios= 0
    for trabajadores23 in trabajadores2:
        total_precios += trabajadores23[1]
    return total_precios / len(trabajadores2)

def medida_geometrica(trabajadores2):
    total_cant = 0 
    for trabajadores23 in trabajadores2:
        total_cant += trabajadores23[1]
        medida_geo = total_cant / len(trabajadores2)
    return medida_geo ** (1/ len(trabajadores23))

def masalto(trabajadores2):
    producto_mas_caro = None 
    precio_mas_alto = 0 
    for trabajadores23 in trabajadores2:
        if trabajadores23[1] > precio_mas_alto:
            precio_mas_alto = trabajadores23[1]
            producto_mas_caro = trabajadores23
    return producto_mas_caro

def masbajo(trabajadores2):
    producto_mas_barato = None
    precio_mas_bajo = float("inf")
    for trabajadores23 in trabajadores2:
        if trabajadores23[1] < precio_mas_bajo:
            precio_mas_bajo= trabajadores23[1]
            producto_mas_barato = trabajadores23
    return producto_mas_barato







def salir():
    print("Saliendo del programa.. ")
    print("MUCHAS GRACIAS POR UTILIZAR EL PROGRAMA")
    print("Desarrollado por: Vicente Cossio RUT: 21985776-4")

    

def menu():
    while True:
        print("-"*30)
        print("Bienvenido al programa")
        print("-"*30)

                                        
        print("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas.\n4. Reporte de sueldos\n5. Salir del programa")
        
        try:
            opc=int(input("Ingrese la opcion deseada:"))
        except ValueError:
            print("Ingrese un valor correcto")

        os.system("cls")

        if opc==1:
            trabajadores2=asignar_sueldos()
            time.sleep(1)
            print("Sueldos Asignados exitosamente...")
            time.sleep(1)
        elif opc ==2:
                print("-------Clasificando Sueldos------- ")
                menores80000, entre800y2000, mayora2500000 = clasificacion(trabajadores2)
                print("\nSueldos Menores a $800.000")
                for traba in menores80000:
                    print(traba)
                    time.sleep(0.5)
                
                print("\nSueldo entre $800.000 y $2.000.000")
                for traba in entre800y2000:
                    print(traba)
                    time.sleep(0.5)

                print("\nSueldo superiores a $2.000.000")    
                for traba in mayora2500000:
                    print(traba)
                    time.sleep(0.5)

        elif opc==3:
            while True:
                print("1. Promedio \n2. Media Geometrica \n3. Sueldo mas alto\n4. Sueldo mas bajo ")
                opcion=int(input("Ingrese la estadistica que desea ver: "))

                if opcion==1:
                    promedio_sueldos=promedio(trabajadores2)
                    print(f"Promedio Sueldos: {promedio_sueldos}")
                    break
                elif opcion==2:
                    media_geo=medida_geometrica(trabajadores2)
                    print(f"Media Geometrica Sueldos: {media_geo}")
                    break
                elif opcion==3:
                    sueldomasalto=masalto(trabajadores2)
                    print(f"El sueldo mas alto es: {sueldomasalto}")
                    break
                elif opcion==4:
                    sueldomasbajo=masbajo(trabajadores2)
                    print(f"El sueldo mas bajo es: {sueldomasbajo}")
                    break
        elif opc==4:

            guardado(trabajadores2)
            print("Guardando los sueldos en csv = 'sueldosguardados.csv' ")      
        elif opc==5:
            salir()
            break
                

menu()












