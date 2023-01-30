""""
programa3
Nombre: José Alonso Domínguez Castillo
Fecha: 24/01/2023
Descripción:print y operaciones aritmetica
"""
#Los corchetes "{}" sirven para asignar un epacio a las variables que quieres usar
numero1 = 10
numero2 = 5 
numero3 = 50
variable1 = "="
print ("{} + {}".format (numero1,numero2)) 
print ("{} + {} {}".format (numero1,numero2,variable1),(numero1 + numero2))
print ("{} {} {} * {}".format (numero3,variable1,numero1,numero2))
#El comando "input" sirve para que podamos poner la variable que nosotros queramos
dia = input()
mes = input()
año = input()
print("Fecha de nacimiento: " + dia,mes,año)