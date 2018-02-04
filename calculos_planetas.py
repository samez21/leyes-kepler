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
    Me=conversiones.Mt_a_Kg(info_programa.estrelllas) # Se llama al factor de conversión 
    for planeta in info_programa.planetas:
        Co=conversiones.UA_a_m(planeta[1]) # Se convierte a metros para que funcione con la tercera ley
        Cp=leyes.tercera_ley(Me,Co) # Se calcula el periodo después de realizar conversión 
        periodos.append(Cp) # Se incorpora  el resultado a una lista
    return periodos 
        
        
        
   