"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    data= open("c:/Analitica_Descriptiva/Taller_1/LAB-01-programacion-basica-en-python-rcburbanoo/files/input/data.csv")
    dic={}
    for line in data:
        fila=line.strip().split("\t")
        if fila[0] in dic:
            dic[fila[0]]=dic[fila[0]]+1
        else:
            dic[fila[0]]=1
    return sorted(dic.items())


