"""" 
Programa6
Nombre:José Alonso Dominguez Castillo
Fecha:30/01/2023
Descripcion: Calcular el area y el perimetro de un triangulo
"""
print("Insertar base y altura para sacar el area del triangulo")#Texto para indicar que valores debe de ir
base = input("Base: ")#Datos que el usuario desee poner
altura = input("Altura: ")#Datos que el usuario desee poner
area = int(base) * int(altura) / 2#Operacion que se realizara
print("Insertar el valor de los lados del triangulo para sacar el perimetro del triangulo")#Texto para indicar que valores debe de ir
lado1 = input("Lado 1: ")#Datos que el usuario desee poner
lado2 = input("Lado 2: ")#Datos que el usuario desee poner
lado3 = input("Lado 3: ")#Datos que el usuario desee poner
perimetro = int(lado1) + int(lado2) + int(lado3)#Operacion que se realizara
print("Area= ",area)#Respuesta que arrojara el programa
print("Perimetro= ",perimetro)#Respuesta que arrojara el programa