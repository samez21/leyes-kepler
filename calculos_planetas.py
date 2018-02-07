# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 19:26:29 2017
En este archivo (calculos_planetas.py) se encontrarán los calculos con las listas realizadas
@author: USUARIO
"""
import info_programa # Se importa debido a que están las listas de los planetas
import leyes # Se usará la tercera ley para encontrar el periodo de los planetas
import conversiones # Se usan factores de conversión
def periodo_planetas():
    """
    esta función usa las lista de listas en info_programa.py y usa la función tercera_ley ubicada en leyes.py 
    """
    periodos=[]
    Ce=conversiones.luminosidad_solar_a_vatios(info_programa.estrella[1])# Masa de la estrella - Calcular masa a partir de temp y luminosidad
    Me=leyes.ecuacion_masa(info_programa.estrella[0],Ce)
    for planeta in info_programa.planetas:
        Co=conversiones.UA_a_m(planeta[1]) # Se convierte a metros para que funcione con la tercera ley
        Cp=leyes.tercera_ley(Me,Co) # Se calcula el periodo después de realizar conversión - convertido a años
        periodos.append(Cp) # Se incorpora  el resultado a una lista
    return periodos
        
        
        
   