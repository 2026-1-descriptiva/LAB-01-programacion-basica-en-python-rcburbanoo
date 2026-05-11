"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data= open("files/input/data.csv","r").readlines()
    dic={}
    for line in data:
        fila=line.strip().split("\t")
        if fila[0] in dic:
            if int(fila[1])>dic[fila[0]][0]:
                dic[fila[0]]= (int(fila[1]),dic[fila[0]][1])
            elif int(fila[1])<dic[fila[0]][1]:
                dic[fila[0]]= (dic[fila[0]][0],int(fila[1]))
        else:
            dic[fila[0]]= (int(fila[1]),int(fila[1]))
    resultado=[]
    for letra,valor in dic.items():
        resultado.append((letra,valor[0],valor[1]))
    return sorted(resultado)
