# -*- coding: utf-8 -*-
"""
Editor de Spyder
Acá se encuentra las leyes físicas con las que funcionará el programa (lista_planetas.py)
"""
from numpy import pi
G=6.67408e-11
sigma= 5.67e-8
pi4=4*pi
pi4e2=pi**2*4


def ley_stefan_boltzmann(T,L):
    """
    Se usa la ley de boltzmann para calcular del diagrama HR el radio de la estrella, el radio se da en metros, la luminosidad en vatios y la temperatura en Kelvin
    """
    R=(L/(T**4*pi4*sigma))**0.5
    return R
   
def ecuacion_masa (T,L):
    """
    Se usa esta ecuación, para relacionar la masa, luminosidad en vatios y temperatura de una estrella en kelvin
    """
    M=L/(T/30029898)
    return M
        
def tercera_ley(M,a):
    """
    Con la tercera ley de Kepler se calculará el periodo de rotacion de los plaentas que el usuario colocará, "M" pertenece a la masa de la estrella, y "a" pertenece al semieje mayor
    """
    P=(a**3*pi4e2/(G*M))**0.5
    return P

def tercera_ley_a(M,P):
    """
    En este caso, se usa la misma ley, pero despejando el valor del eje mayor y con las mismas unidades que en tercera_ley
    """
    a=(P**2*G*M/pi4e2)**(1/3)
    return a
    
