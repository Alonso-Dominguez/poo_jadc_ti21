"""""
Programa 9
Nombre: José Alonso Domínguez Castillo
Fecha: 20/02/23
Descripción: Realizar un programa en python que compare 2 números enteros e imprima el mayor de ellos, y si son iguales imprima "None"
"""
print("Insertar numeros")
numero1= int(input("Número 1: "))
numero2= int(input("Número 2: "))
if numero1 > numero2:
    print("Número mayor: ",numero1)
if numero2 > numero1: 
    print("Número mayor: ",numero2)
if numero1 == numero2:
    print(None)