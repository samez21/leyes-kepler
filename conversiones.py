# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 13:07:10 2017
En este archivo (conversiones.py) se tendrán todos los factores de conversión útiles en la aplicación
@author: samez
"""
import numpy#se importa para las funciones de seno, coseno y tangente

def luminosidad_solar_a_vatios(Lsol):
    """
    se ingresa el valor en luminosidades solares, y se convierte en vatios
    """
    vatios=Lsol*3.827e26
    return vatios

def Mt_a_Kg(Mt):
    """
    se ingresa el valor en masas terrestres y se convierte en kg
    """
    Kg=5.972e24*Mt
    return Kg

def Rt_a_m(Rt):
    """
    se ingresa el valor en radios terrestres y se convierte en metros
    """
    m=6371000*Rt
    return m

def UA_a_m(UA):
    """
    se ingresa el valor en unidades astronómicas y se convierte a metros
    """
    m=149597870700*UA
    return m

def coordenadas_polares_a_cartesianas(r,A):
    """
    Se ingresan coordenadas polares, con los grados en radianes, y se convierte a coordenadas cartesianas
    """
    x=r*numpy.cos(A)
    y=r*numpy.sin(A)
    return [x,y]

def segundos_a_años(s):
    d=s/31536000
    return d
