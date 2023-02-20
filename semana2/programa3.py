""""
programa3
Nombre: José Alonso Domínguez Castillo
Fecha: 24/01/2023
Descripción:Format y operaciones aritmeticas
"""
#Los corchetes "{}" sirven para asignar un epacio a las variables que quieres usar
numero1 = 10#Se asigna un valor a la variable
numero2 = 5 #Se asigna un valor a la variable
numero3 = 50#Se asigna un valor a la variable
variable1 = "="#Se asigna un valor a la variable
print ("{} + {}".format (numero1,numero2))#Se imprime usando ".format" para que acomode las variable asignando un espacio para cada variable usando los corchetes "{}"  
print ("{} + {} {}".format (numero1,numero2,variable1),(numero1 + numero2))#Se imprime usando ".format" para que acomode las variable asignando un espacio para cada variable usando los corchetes "{}" 
print ("{} {} {} * {}".format (numero3,variable1,numero1,numero2))#Se imprime usando ".format" para que acomode las variable asignando un espacio para cada variable usando los corchetes "{}" 
#El comando "input" sirve para que podamos poner la variable que nosotros queramos
dia = input()#Se pone "input" para el usuario le de un valor a la variable 
mes = input()#Se pone "input" para el usuario le de un valor a la variable
año = input()#Se pone "input" para el usuario le de un valor a la variable
print("Fecha de nacimiento: " + dia,mes,año)#Se manda a imprimir las variables con un texto personalizado