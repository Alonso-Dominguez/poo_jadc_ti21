"""
Nombre: José Alonso Domínguez Castillo
Fecha: 26/01/2023
Descripción: Operaciones con .format
"""
numero1 = 10#Se asigna un valor a la variable
numero2 = 5#Se asigna un valor a la variable
print ("{n1} + {n2} = {suma}".format(n1=numero2,n2=numero2,suma = numero2 + numero2)) #con "suma" puedes realizar una suma con los distintos valores asignados
print ("{n1} {n2}".format(n1=numero1,n2=numero1)) #si no se pone ninguna operación imprimira los valores asignados sin ningun cambio alguno
print ("{n1} / {n2} = {split}".format(n1=numero1,n2=numero2,split = numero2 / numero1)) #con "split" puedes realizar diviciones con los valores asignados
print ("{n1} * {n2} = {matriz}".format(n1=numero1,n2=numero2,matriz = numero2 * numero1)) #con "matriz" puedes realizar multiplicaciones con los valores asignados
print ("{n1} - {n2} = {resta}".format(n1=numero2,n2=numero1,resta = numero2 - numero1)) #con "resta" puedes realizar una resta a los valores asignados