"""""
Programa 9
Nombre: José Alonso Domínguez Castillo
Fecha: 20/02/23
Descripción: Realizar un programa en python que compare 2 números enteros e imprima el mayor de ellos, y si son iguales imprima "None"
"""
print("Insertar numeros")#Texto que pide datos a ingresar
numero1= int(input("Número 1: "))#Se asigna el "int" y el "input" para que el usuario pueda ingresar un valor a la variable pero con solo numeros
numero2= int(input("Número 2: "))#Se asigna el "int" y el "input" para que el usuario pueda ingresar un valor a la variable pero con solo numeros
if numero1 > numero2:#"if" sirve para asignar una declaración
    print("Número mayor: ",numero1)#Se manda a imprimir el numero mayor
if numero2 > numero1: 
    print("Número mayor: ",numero2)#Se manda a mprimir el numero mayor
if numero1 == numero2:
    print(None)#Si no se cumple lo anterior que imprima "None"