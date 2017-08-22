from pila import *

def es_entero(value):
  try:
    int(value)
    return True
  except:
    return False

def dar_prioridad(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2
    if a=="^":
        return 1
    elif a=="(":
        return 0
    
def isOperador(element):
    if element =="+" or element =="-" or element =="*" or element =="/" or element =="^" or element =="(":
       return True
    else:
        return False
      
def expresionALista(expresion,listaSalida):
  for x in expresion:
    listaSalida.append(x)
  return listaSalida
    
def infijoApostfijo(pila,expresion):
    #expresion = expresion[::-1]
    prefijo =[]
    listaEntrada = []
        
    for element in expresion:
        if es_entero(element)==True:
            prefijo.append(element)
        if isOperador(element)==True:
            if pila.es_vacia == False:
                tope == pila.desapilar()
                while pila.es_vacia() == False:
                    if   dar_prioridad(element)> dar_prioridad(tope):
                        pila.apilar(tope)
                        pila.apilar(element)
                    elif dar_prioridad(element)<= dar_prioridad(tope):
                        pila.desapilar(tope)
                        prefijo.append(tope)
            else:
              pila.apilar(element)
    return prefijo

        
                
        
        
        
