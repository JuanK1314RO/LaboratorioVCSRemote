# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:59:58 2020

@author: Juan Camilo Ramirez
"""

# -------- Paquetes y librerías -------- #

import numpy as np

#  ------------- Funciones ------------- #

def temperaturariohacha():#Temperatura en la ciudad de Riohacha en el 2020
    temperatura = np.array([
        [25,25,26,27,27,27,27,27,28,27,27,26],#Temperatura por la mañana
        [31,32,32,32,33,34,34,34,34,33,32,32],#Temperatura por la medio dia
        [29,29,29,30,30,31,31,30,30,29,29,29]])#Temperatura por la noche
    return temperatura

def temperatura_hora_mes(temperatura, hora, mes):
    return temperatura[hora,mes]

def tem_min(temperatura):
    hora, mes = temperatura.shapes
    pos = 0
    tem_base = temperatura[0]
    minimo = len(tem_base)
    for nivel in range(0,hora):
        for tem in range(0,mes):
            if minimo > temperatura[nivel,tem]:
                tem_base = temperatura[nivel,tem]
                minimo = len(tem_base)
                pos = (nivel,tem)
    print("La temperatura minima es de " + str(tem_base) + "º y se encuentra en" +
          str(pos))

def tem_max(temperatura):
    hora, mes = temperatura.shapes
    pos = 0
    tem_base = temperatura[0]
    minimo = len(tem_base)
    for nivel in range(0,hora):
        for tem in range(0,mes):
            if minimo < temperatura[nivel,tem]:
                tem_base = temperatura[nivel,tem]
                minimo = len(tem_base)
                pos = (nivel,tem)
    print("La temperatura minima es de "+ str(tem_base) + "º y se encuentra en" +
          str(pos))

def premedio_tem(temperatura):
    hora, mes = temperatura.shapes
    suma = 0
    i = 0
    for nivel in range(0,hora):
        for tem in range(0,mes):
            suma += tem
            i +=1
    print("La temperatura promedio es de ", str(suma/i) + 
          " en todo el año"
#----------------------------Terminal----------------------------#
temperatura=temperaturariohacha()
tem_min(temperatura)
tem_max(temperatura)
promedio_tem(temperatura)