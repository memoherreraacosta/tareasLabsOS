#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:09:24 2018

@author: memoherrera
"""

### Ejercicio 1

def ejercicio1(lista):
    if lista[0] != None:
        return lista[0]


#La complejidad de este algoritmo es O(1) debido a que solo hace un paso para
#realizar el algoritmo    


### Ejercicio 2

def ejercicio2(lista):
   for i in lista :
       print(i)
#La complejidad de este algoritmo es O(n) debido a que lee la lista en 
#una sola iteracion
       

### Ejercicio 3

def ejercicio3(arreglo):
    for i in arreglo:
        for j in arreglo:
            print(arreglo[i]) + "," + print(arreglo[j])
#La complejidad del arreglo es O(n**2) debido a que hace dos ciclos
#for para realizar el algoritmo
    
    
### Ejercicio 4

def ejercicio4(arreglo):
    corchete =[]
    llave = []
    parentesis = []
    
    for i in range (len(arreglo)):
        if(arreglo[i]=="[" or arreglo[i]=="]"):
            if(arreglo[i]=="["):
                corchete.append(arreglo[i])
            elif (arreglo[i] =="]"):
                if((len(corchete) ==0)):
                    return False
                else:
                    corchete.pop()
                    
        elif(arreglo[i]=="(" or arreglo[i]==")"):
            
            if(arreglo[i]=="("):
                parentesis.append(arreglo[i])
            elif (arreglo[i] ==")"):
                if((len(parentesis) ==0)):
                    
                    return False
                else:
                    parentesis.pop()
            
        elif(arreglo[i]=="{" or arreglo[i]=="}"):
            if(arreglo[i]=="{"):
                llave.append(arreglo[i])
            elif (arreglo[i] =="}"):
                if((len(llave) ==0)):
                    return False
                else:
                    llave.pop()
    if((len(corchete))==0 and (len(parentesis))==0 and (len(llave))==0):
        
        return True
    
    return False
#La complejidad de este algoritmo es maximo O(n) porque hara una sola iteracion
# a la lista
    

### Ejercicio 5 
def ejercicio5(palabra1, palabra2):
    
    palabra1 = palabra1.upper()
    palabra2 = palabra2.upper()
    
    palabraLista1 = list(palabra1)
    palabraLista2 = list(palabra2)
    
    palabraListaOrdenada1 = palabraLista1.sort()
    palabraListaOrdenada2 = palabraLista2.sort()
    
    bandera = True
    contador = 0
    
    while contador < len(palabra1) and bandera :
        if palabraListaOrdenada1 [contador] == palabraListaOrdenada2 [contador]:
            contador += 1
        else :
            bandera = False
    
    return bandera   
#Complejidad del algoritmo es O(n) debido a que si
#las palabras son anagramas recorreran las palabras en una 
#iteracion



####################################################
    

#Pruebas
    

####################################################
    
import matplotlib.pyplot as plt
import time 


#Prueba ejercicio 1
def prueba1():
    arreglo = [20]
    xIteraciones = []
    yTiempo = []
    for i in range(30):
        start = time.time()
        print(ejercicio1(arreglo))
        end = time.time()
        xIteraciones.append(i)
        yTiempo.append(end-start)    
    
    plt.plot(xIteraciones,yTiempo)
    plt.grid()


#Prueba ejercicio 2
def prueba2():
    arreglo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    xIteraciones = []
    yTiempo = []
    for i in range(30):
        start = time.time()
        print(ejercicio2(arreglo))
        end = time.time()
        xIteraciones.append(i)
        yTiempo.append(end-start)    
    
    plt.plot(xIteraciones,yTiempo)
    plt.grid()

#Prueba ejercicio 3 
def prueba3():
    arreglo = [0,1,2,3,4,5]
    xIteraciones = []
    yTiempo = []
    
    for i in range(30):
        start = time.time()
        print(ejercicio3(arreglo))
        end = time.time()
        xIteraciones.append(i)
        yTiempo.append(end-start)    
    
    
    plt.plot(xIteraciones,yTiempo)
    plt.grid()

#Prueba ejercicio 4 
def prueba4(): 
    xIteraciones = []
    yTiempo = []
    
    for i in range(30):
        start = time.time()
        print(ejercicio4("[()]"))
        end = time.time()
        xIteraciones.append(i)
        yTiempo.append(end-start)    
    
    
    plt.plot(xIteraciones,yTiempo)
    plt.grid()

#Prueba ejercicio 5
def prueba5():
    xIteraciones = []
    yTiempo = []
    
    for i in range(30):
        start = time.time()
        print(ejercicio5("Hola","aloh"))
        end = time.time()
        xIteraciones.append(i)
        yTiempo.append(end-start)    
    
    
    plt.plot(xIteraciones,yTiempo)
    plt.grid()















