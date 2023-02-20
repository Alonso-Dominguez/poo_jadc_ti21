"""
programa 11
Nombre: José Alonso Domínguez Castillo
Fecha: 09/02/23
Descripción: Uso del "def"
"""
def mayor(numero1,numero2):#se asignan los numeros
    result=None#asigno una funcion
    if numero1 > numero2:#asigno la condicion que debe realizar
        result=numero1#asigno el resultado que debe regresar 
    elif numero2 > numero1:#asigno otra condicion en caso que la primera no se cumpla
        result=numero2#asigno el resultado que debe regresar
    return result#asigno que debe arrojar el resultado
print(mayor(2,1))#son las pruebas que se deben de hacer
print(mayor(1,2))#son las pruebas que se deben de hacer
print(mayor(2,2))#son las pruebas que se deben de hacer
print(mayor(-1,-2))#son las pruebas que se deben de hacer
print(mayor(-2,-1))#son las pruebas que se deben de hacer
print(mayor(-1,-1))#son las pruebas que se deben de hacer
print(mayor(2,-1))#son las pruebas que se deben de hacer
print(mayor(-1,2))#son las pruebas que se deben de hacer