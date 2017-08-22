# -*- coding: utf-8 -*-
from pila import *
class Pelicula:
    
    def __init__(self,nombre,genero,año):
        self.n = nombre
        self.g = genero
        self.a = año

    
    def getNombre(self):
        return self.n       
      
    def getGenero(self):
        return self.g
    
    def getAño(self):
        return self.a

pelicula1 = Pelicula("transformers","ciencia ficcion", 2007) 
pelicula2 = Pelicula("Al filo del mañana","ciencia Ficcion",2014)
pelicula3 = Pelicula("Spiderman", "Accion",2017)
pelicula4 = Pelicula("Avengers","Accion",2012)
pelicula5 = Pelicula("Avengers 2", "Accion",2015)
pelicula6 = Pelicula("Mi Villano Favorito 3" ,"Infantil",2017)
pelicula7 = Pelicula("Ex MAchina","ciencia Ficcion",2011)

pila = Pila()

print("a continuacion se agregaran a la pila las peliculas "+ "\n")

pila.apilar(pelicula1.getNombre())
pila.apilar(pelicula2.getNombre())
pila.apilar(pelicula3.getNombre())
pila.apilar(pelicula4.getNombre())
pila.apilar(pelicula5.getNombre())
pila.apilar(pelicula6.getNombre())
pila.apilar(pelicula7.getNombre())

print("los elementos de la pila son los siguientes :"+ "\n")
print(pila.items)
print("\n")
print("A continuacion se Desapilaran los elementos :"+ "\n")          
    
while pila.es_vacia() != True:
    print ( pila.desapilar())
print("\n")
print("la pila esta vacia "+ "\n")
print(pila.items)
