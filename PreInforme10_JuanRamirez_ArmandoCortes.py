# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:28:26 2020

@author: Juan Camilo Ramirez
"""
##Libreria##
import numpy as np

##Definicion de varibles##
util = np.array([
        2784, 23789, 30189, 30967, 32501,
        32701, 31665, 17155, 4614, 834
        ])

##Punto 1##
def promedio1(n,l):
    sum = 0
    for i in range (8,l,1):
        sum += n[i]
    
    return sum/2

promedio1 = str(promedio1(util,10))

def promedio2(n,l):
    sum = 0
    for i in range (0,l,1):
        sum += n[i]
    
    return sum/2
promedio2 =  str(promedio2(util,2))

diferencia = float(promedio2) - float(promedio1)
print("\nEl promedio de la utilidad operacional en los ultimos dos años es " + 
      str(promedio1) + " y el promedio de los primeros dos años es " + 
      str(promedio2) + " por lo que la diferencia en las dos utilidades operacionales es de " + 
      str(diferencia) +  ".")

##Punto 2##
def uoMenor(n):
    x = np.sort(n)
    i=0
    
    while n[i] > x[0]:
        i+=1
    
    return i+1

def uoMayor(n):
    x = np.sort(n)
    i=0
    
    while n[i] < x[9]:
        i+=1
    
    return i+1

print("\n\nLa diferencia entre la utilidad operacional con mayor utilidad y la de menor utilidad es de " + 
      str(np.sort(util)[9]-np.sort(util)[0]) + ".")

##Punto 3##
def mediana(lst):
       n = len(lst)
       if n < 1:
               return None
       if n % 2 == 1:
               return sorted(lst)[n//2]
       else:
               return sum(sorted(lst)[n//2-1:n//2+1])/2.0
        
print("\n\nLa mediana de la utilidad operacional durante los años de registro es: " 
      + str(mediana(util)))

##Punto 4##
def mediana(lst):
       n = len(lst)
       if n < 1:
               return None
       if n % 2 == 1:
               return sorted(lst)[n//2]
       else:
               return sum(sorted(lst)[n//2-1:n//2+1])/2.0

def promedio(n,l):
    sum = 0
    for i in range (0,l,1):
        sum += n[i]
    
    return sum/10

promedio = float(promedio(util,10))
mediana = float(mediana(util))
diferencia=(float(mediana) - float(promedio))
print("\n\nLa diferencia entre la mediana y la media es " + 
      str(diferencia))

##Punto 5##
suma = 0
for fila in util:
    for n in util:
        suma += n


print("\n\nEl porcentaje que le aporta la utilidad operacional de 2008 a la utilidad operacional acumulada es de: " + str(round(util[0]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2009 a la utilidad operacional acumulada es de: " + str(round(util[1]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2010 a la utilidad operacional acumulada es de: " + str(round(util[2]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2011 a la utilidad operacional acumulada es de: " + str(round(util[3]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2012 a la utilidad operacional acumulada es de: " + str(round(util[4]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2013 a la utilidad operacional acumulada es de: " + str(round(util[5]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2014 a la utilidad operacional acumulada es de: " + str(round(util[6]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2015 a la utilidad operacional acumulada es de: " + str(round(util[7]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2016 a la utilidad operacional acumulada es de: " + str(round(util[8]*100/suma,3))+str("%"))
print("El porcentaje que le aporta la utilidad operacional de 2017 a la utilidad operacional acumulada es de: " + str(round(util[9]*100/suma,3))+str("%"))

##Punto 6##
def defit(util):
    a = util[9]-util[8]
    return a
    
print("\n\nEl deficit de el año 2017 es:", defit(util) , "Millones de pesos")

##Punto 7##
def orden(n1,n2):
    defi = (n2*100/n1)
    defi = 100-defi
    return defi

acum = 0
for i in range(0,9,1):
        acum += util[i]

print("\n\nPorcentajes de aporte anual",end="") 
print("\n08: "+ str(round(util[0]*100/acum,2))+str("%"),end="")
print("\n09: "+ str(round(util[1]*100/acum,2))+str("%"),end="")
print("\n10: "+ str(round(util[2]*100/acum,2))+str("%"),end="")
print("\n11: "+ str(round(util[3]*100/acum,2))+str("%"),end="")
print("\n12: "+ str(round(util[4]*100/acum,2))+str("%"),end="")
print("\n13: "+ str(round(util[5]*100/acum,2))+str("%"),end="")
print("\n14: "+ str(round(util[6]*100/acum,2))+str("%"),end="")
print("\n15: "+ str(round(util[7]*100/acum,2))+str("%"),end="")
print("\n16: "+ str(round(util[8]*100/acum,2))+str("%"),end="")
print("\n17: "+ str(round(util[9]*100/acum,2))+str("%"))

print("\n\nDeficit comparado con año anterior",end="")
print("\n08-09: "+ str(round(orden(util[0],util[1]),2))+str("%"),end="")
print("\n09-10: "+ str(round(orden(util[1],util[2]),2))+str("%"),end="")
print("\n10-11: "+ str(round(orden(util[2],util[3]),2))+str("%"),end="")
print("\n11-12: "+ str(round(orden(util[3],util[4]),2))+str("%"),end="")
print("\n12-13: "+ str(round(orden(util[4],util[5]),2))+str("%"),end="")
print("\n13-14: "+ str(round(orden(util[5],util[6]),2))+str("%"),end="")
print("\n14-15: "+ str(round(orden(util[6],util[7]),2))+str("%"),end="")
print("\n15-16: "+ str(round(orden(util[7],util[8]),2))+str("%"),end="")
print("\n16-17: "+ str(round(orden(util[8],util[9]),2))+str("%"))
