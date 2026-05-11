"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data= open("c:/Analitica_Descriptiva/Taller_1/LAB-01-programacion-basica-en-python-rcburbanoo/files/input/data.csv","r").readlines()
    dic={}
    for line in data:
        sum=0
        fila=line.strip().split("\t")
        letra=fila[0]
        codigo=fila[4].split(",")
        for i in codigo:
            letras,valor=i.split(":")
            sum=sum+int(valor)
        if letra in dic:
            dic[letra]=dic[letra]+sum
        else:
            dic[letra]=sum
    return dict(sorted(dic.items()))
        
print(pregunta_12())  