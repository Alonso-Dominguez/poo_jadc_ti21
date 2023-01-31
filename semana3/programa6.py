"""" 
Programa6
Nombre:José Alonso Dominguez Castillo
Fecha:30/01/2023
Descripcion: Calcular el area y el perimetro de un triangulo
"""
print("Insertar base y altura para sacar el area del triangulo")
base = input("Base: ")
altura = input("Altura: ")
area = int(base) * int(altura) / 2
print("Insertar el valor de los lados del triangulo para sacar el perimetro del triangulo")
lado1 = input("Lado 1: ")
lado2 = input("Lado 2: ")
lado3 = input("Lado 3: ")
perimetro = int(lado1) + int(lado2) + int(lado3)
print("Area= ",area)
print("Perimetro= ",perimetro) 