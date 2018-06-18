# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:14:29 2018

@author: USUARIO
"""
import numpy #se usa numpy para las funciones de seno y coseno
import conversiones
import calculos_planetas
import info_programa
def excentricidad(c,a):
    """
    con la posición de los focos y el eje mayor, se haya la excentricidad de la elipse
    """
    e=c/a
    return e

def radio_orbital_tiempo(a,e,w,t):
    """
    funcion que con la excentricidad y el angulo orbital, en radianes, regresa el radio
    """
    r=a*(1-e**2)/(1+e*numpy.cos(w*t))
    return r

def angulo_orbital_tiempo(w,t):
    """
    con el angulo orbital o la frecuencia angular, se multiplica con el periodo para obtener una relación
    """
    return w*t

def posicion_foco(a,e):
    """
    Función que relaciona la excentricidad con el eje mayor para sacar la posición de los focos
    """
    c=e*a
    return c

def frecuencia_angular(p):
    """
    Funcion que permite encontrar la frecuencia angular usando el periodo
    """
    w=2*numpy.pi/p # Luego la frecuencia angular
    return w


def coordenadas(a,e,w,t):
    """
    Función para tener las coordenadas de la elipse
    """
    r=a*(1-e**2)/(1+e*numpy.cos(angulo_orbital_tiempo(w,t)))
    Coo=conversiones.coordenadas_polares_a_cartesianas(r,w*t)
    Coo[0]=Coo[0]+2*posicion_foco(a,e)
    return Coo

def función_orbitas_entera():
    T = calculos_planetas.periodo_planetas()
    T_max = max(T)
    t_rango = numpy.linspace(0, T_max, 500)
    Co_planetas = [t_rango]
    posicion = 0
    for planeta in info_programa.planetas:
        Coo_planeta = []
        w_planeta = frecuencia_angular(T[posicion])
        for tiempo in t_rango:
            Ccarte = coordenadas(planeta[1], planeta[0], w_planeta, tiempo)
            Coo_planeta.append(Ccarte)
        Co_planetas.append(numpy.array(Coo_planeta))
        posicion = posicion + 1
    return Co_planetas
