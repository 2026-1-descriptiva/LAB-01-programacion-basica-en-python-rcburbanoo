"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    data= open("files/input/data.csv","r").readlines()
    
    diccionario={}
    for line in data:
        fila=line.strip().split("\t")  
        dic=fila[4].split(",")
        
        for elemento in dic:
            clave,valor=elemento.split(":")
            if clave in diccionario:
                if int(valor)>diccionario[clave][1]:
                    diccionario[clave]= (diccionario[clave][0],int(valor))
                elif int(valor)<diccionario[clave][0]:
                    diccionario[clave]= (int(valor),diccionario[clave][1])
            else:
                diccionario[clave]= (int(valor),int(valor))
                
        
    resultado=[]
    for clave,valor in diccionario.items():
        resultado.append((clave,valor[0],valor[1]))
        
    return sorted(resultado)


    