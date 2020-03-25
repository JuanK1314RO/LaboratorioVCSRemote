# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:54:36 2020

@author: Juan Camilo Ramirez
"""
#%% Primer ejercicio
a = int(input("Ingese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingese el valor de c: "))
d = int(input("Ingrese el valor de d: "))

print("El producto es:", a*c)
print("El doble de a es", a*2)
print("El cuadrado de b es", b**2)
print("La raiz cuadrada de d es:", d**(1/2))

#%% Segundo ejercicio 
print("Ingrese los valores de a,b,c de la ecuacion cuadratica")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = (b**2-4*a*c)

if d>0:
    x1 = (-b+d**(1/2))/2*a
    x2 = (-b-d**(1/2))/2*a
    print("El valor de x1 es:", x1)
    print("El valor de x2 es:", x2)
elif d==0:
    print("el valor de x1 y x2 son iguales", -b/2*a)
elif d<0:
    print("No existe solcuion a la ecuacion cuadratica dentro del dominio de los numeros reales")