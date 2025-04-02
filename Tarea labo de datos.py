# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 18:32:58 2025

@author: Tiago
"""


#Actividad 1:
empleado_01 = [[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000]]

def superanSalarioActividad01(empleado_01: list[list[float]],umbral: float) -> list[list[int]]:
    res:list[list[float]] = []
    
    for i in range (len(empleado_01)):
        if empleado_01[i][3] > umbral:
            res.append(empleado_01[i])
    
    return res


superanSalarioActividad01(empleado_01,15000)
        
#Actividad 2:
empleado_02 = [[20222333,45,2,20000],[33456234,40,0,25000],[45432345,41,1,10000],[43967304,37,0,12000],[42236276,36,0,18000]]

def superanSalarioActividad01(empleado_01: list[list[float]],umbral: float) -> list[list[int]]:
    res:list[list[float]] = []
    
    for i in range (len(empleado_01)):
        if empleado_01[i][3] > umbral:
            res.append(empleado_01[i])
    
    return res


superanSalarioActividad01(empleado_02,15000) #Continua Funcionando

#Actividad 3:

empleado_03 = [[20222333,20000,45,2],[33456234,25000,40,0],[45432345,10000,41,1],[43967304,12000,37,0],[42236276,18000,36,0]]

def superanSalarioActividad01(empleado_01: list[list[float]],umbral: float) -> list[list[int]]:
    res:list[list[float]] = []
    
    for i in range (len(empleado_01)):
        if empleado_01[i][3] > umbral:
            res.append(empleado_01[i])
    
    return res

#No funciona

def superanSalarioActividad03(empleado_03: list[list[float]],umbral: float) -> list[list[int]]:
    res:list[list[float]] = []

    for i in range (len(empleado_03)):
        if empleado_03[i][1] > umbral:
            res.append(empleado_02[i])
    
    return res


superanSalarioActividad03(empleado_03, 15000)

#Actividad 4:
    
    
empleado_04 = [
    [20222333, 33456234, 45432345, 43967304, 42236276],  # DNIs
    [45, 40, 41, 37, 36],                                # Edades
    [2, 0, 1, 0, 0],                                     # Hijos
    [20000, 25000, 10000, 12000, 18000]                  # Salarios
]

def superanSalarioActividad04(empleado_04: list[list[float]],umbral: float) -> list[list[int]]:
    res:list[list[float]] = []

    for i in range (len(empleado_04)):
        if empleado_04[3][i] > umbral:
            res.append(empleado_02[i])
    
    return res


superanSalarioActividad03(empleado_04, 15000)
