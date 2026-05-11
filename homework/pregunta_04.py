"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    data= open("c:/Analitica_Descriptiva/Taller_1/LAB-01-programacion-basica-en-python-rcburbanoo/files/input/data.csv")
    dic={}
    for line in data:
        fila=line.strip().split("\t")  
        mes=fila[2].split("-")[1]
        if mes in dic:
            dic[mes]=dic[mes]+1
        else:
            dic[mes]=1
    return sorted(dic.items())
