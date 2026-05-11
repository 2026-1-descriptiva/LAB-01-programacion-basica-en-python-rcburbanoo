"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data= open("c:/Analitica_Descriptiva/Taller_1/LAB-01-programacion-basica-en-python-rcburbanoo/files/input/data.csv","r").readlines()
    sum=0
    for line in data:
        fila=line.strip().split("\t")
        sum=sum+int(fila[1])
    return sum

