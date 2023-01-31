"""" 
Programa7
Nombre:José Alonso Dominguez Castillo
Fecha:31/01/2023
Descripcion: Calcular e imprimir el area y el prerimetro de circulo y cuadrado
"""
print("Ingresar datos del cuadrado para sacar su area y perimetro")
lado = int(input("Lado: "))
area = (lado * lado)
perimetro = (lado + lado + lado + lado)
print("El area del cuadrado es ",area ,"y el perimetro es ",perimetro)
print("Insertar el radio del circulo para sacar el perimetro y el area del circulo")
radio = int(input("Radio: "))
area = (3.1416 * radio**2)
perimetro = (2 * 3.1416 * radio)
print("El area del circulo es ",area,"y el perimetro del circulo es ",perimetro)