"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    data= open("c:/Analitica_Descriptiva/Taller_1/LAB-01-programacion-basica-en-python-rcburbanoo/files/input/data.csv","r").readlines()
    diccionario={}
    for line in data:
        fila=line.strip().split("\t")  
        dic=fila[4].split(",")
        for elemento in dic:
            key,value=elemento.split(":")
            if key in diccionario:
                diccionario[key]=diccionario[key]+1
            else:
                diccionario[key]=1


    return dict(sorted(diccionario.items()))

