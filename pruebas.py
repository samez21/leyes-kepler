# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:13:35 2017
En este archivo (pruebas.py) se probarán las funciones y demás cosas realizadas
@author: USUARIO
"""
import orbitas
import conversiones
import leyes
import numpy
import calculos_planetas
import rango_temperaturas

T=5778 # Temperatura del sol en kelvin
L=3.827e26 # luminosidad del sol en vatios
M=1.9819e30 # Masa del sol en kg
Lsol=1 # Número de luminosidades del sol
a=149597870700 # Semieje mayor de la tierra en metros
c=3867644300.41 #Focos de la elipse tierra-sol
Mt=1 # Número de masas terrestres
Rt=1 # Número de radios terrestres
UA=1 # Número de unidades astronómicas
e= 0.01671022 #excentricidad de la tierra
p=3.154e7 # Periodo de la Tierra en segundos
f=2*numpy.pi #Angulo polar
A=numpy.pi # Angulo dado en radianes
r=5 # Coordenada polar r
t=3.154e7 # Periodo de la Tierra en segundos.
k=30000 #temperatura de estrella
l=3.827e26
w=198171664.58844414 # Frecuencia Angular de la tierra
print(leyes.ley_stefan_boltzmann(T,L)) # Prueba  de la ley de Stefan-Boltzmann
print(leyes.ecuacion_masa(T,L)) # Prueba de la ecuación para hallar masa de una estrella
print(leyes.tercera_ley(M,a)) # Prueba de la tercera ley de Kepler
print(leyes.tercera_ley_a(M,p)) # Prueba de la tercera ley de Kepler para encontrar "a"
print(conversiones.luminosidad_solar_a_vatios(Lsol)) # Prueba del factor de conversión de luminosidades solares a vatios
print(conversiones.Mt_a_Kg(Mt)) # Prueba del factor de conversion de masas terrestres a kilogramos
print(conversiones.Rt_a_m(Rt)) # Prueba del factor de conversión de radios terrestres a metros
print(conversiones.UA_a_m(UA)) # Prueba del factor de conversión de unidades astronómicas a metros
print(orbitas.excentricidad(c,a)) # prueba del cálculo de excentricidad
print(orbitas.radio_orbital_tiempo(a,e,w,t)) # Prueba  de fórmula de órbitas
print(calculos_planetas.periodo_planetas()) # Prueba de los periodos de cada planeta
print(conversiones.coordenadas_polares_a_cartesianas(r,A)) # Prueba del factor de conversión de coordenadas polares
print(orbitas.frecuencia_angular(p)) # Prueba de frecuencia angular
print(orbitas.excentricidad(c,a)) # Prueba de función de orbitas excentricidad
print(rango_temperaturas.color_estrellas(k)) # Prueba función del rango de temperaturas
print(orbitas.coordenadas(a,e,w,t))
print(orbitas.función_orbitas_entera(t,e,w,a))