"""
Fecha:14/02/23
Nombre:José Alonso Domínguez Castillo
Descripción:Herencias
"""
class Persona:#Se asigna una clase
    __nombre=None#Se asignan valores
    __edad=None#Se asignan valores
    def __init__(self):#Llamamos al constructor de la clase
        print("Persona")#Se manda a imprimir
class Alumno:#Se asigna otra clase
    __matricula=None#Se asignan valores 
    def __init__(self):#Llmamos al constructor de la clase
        super().__init__()#LLama all constructor de la clase que esta heredando
        print("Alumno")#Se manda a imprimir
objeto_persona=Persona()#Se instansia una clase
objeto_alumno=Alumno()#Se instancia una clase
print(dir(objeto_persona))#"dir" sirve para hacer una lista valores
print(dir(objeto_alumno))#"dir" sirve para hacer una lista valores
