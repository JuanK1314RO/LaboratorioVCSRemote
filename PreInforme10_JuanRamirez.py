# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:28:26 2020

@author: Juan Camilo Ramirez
"""

import numpy as np

Util = np.array([
        2784, 23789, 30189, 30967, 32501,
        32701, 31665, 17155, 4614, 834
        ])

##Punto 6##
def defit(Util):
    a = Util[9]-Util[8]
    
    print("El deficit de el año 2017 es:", a)