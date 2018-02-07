# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:31:41 2018

@author: USUARIO
"""
import warnings

def celcius_a_kelvin(c):
    K = c + 273.15
    return K

def color_estrellas(k, externo=True):
    if 35000 > k >= 20000:
        color="azul"
    elif 15000 > k >= 20000:
        color="blanzo azulado"
    elif 15000 > k >= 9000:
        color="blanca"
    elif 9000 > k >= 7000:
        color="blanco amarillenta"
    elif 7000 > k >= 5500:
        color="amarilla"
    elif 5500 > k >= 4000:
        color="amarillo naranjada"
    elif 4000 > k >= 3000:
        color="rojo"
    else:
        warnings.warn("Debe ingresar una temperatura menor a 35000 y mayor que 3000 kelvins.")
    if externo:
        return color
    else:
        return "el color de su estrella es {}".format(color)
