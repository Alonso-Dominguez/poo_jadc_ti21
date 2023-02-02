"""" 
Programa7
Nombre:José Alonso Dominguez Castillo
Fecha:31/01/2023
Descripcion: Calcular e imprimir el area y el prerimetro de circulo y cuadrado
"""
print("Ingresar datos del cuadrado para sacar su area y perimetro")#Texto para indicar que valores debe de ir
lado = int(input("Lado: "))#Datos que el usuario desee poner
area = (lado * lado)#Operacion que se realizara
perimetro = (lado * 4)#Operacion que se realizara
print("-El area del cuadrado es ",area ,"y el perimetro es ",perimetro)#Respuesta que arrojara el programa
print("Insertar el radio del circulo para sacar el perimetro y el area del circulo")#Texto para indicar que valores debe de ir
radio = int(input("Radio: "))#Datos que el usuario desee poner
area = (3.1416 * radio**2)#Operacion que se realizara
perimetro = (2 * 3.1416 * radio)#Operacion que se realizara
print("-El area del circulo es ",area,"y el perimetro del circulo es ",perimetro)#Respuesta que arrojara el programa