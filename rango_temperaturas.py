# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:31:41 2018

@author: USUARIO
"""

def celcius_a_kelvin(c):
    K=c+ 273.15
    return K

def color_estrellas(k):
    if 35000>k>=20000:
        print("el color de su estrella es azul")
    elif 15000>k>20000:
        print("el color de su estrella es blanzo azulado")
    elif 15000>k>9000:
        print("el color de su estrella es blanca")
    elif 9000>k>7000:
        print("el color de su estrella es blanco amarillenta")
    elif 7000>k>5500:
        print("el color de su estrella es amarilla")
    elif 5500>k>4000:
        print("el color de su estrella es amarillo naranjada")
    elif 4000>k>3000:
        print("el color de su estrella es rojo")
    else:
        print("pon una temperatura menor a 35000")
    
    