"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd

def pregunta_01():
    
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    datos = []
    contenido = lineas[4:]

    fila = []

    for linea in contenido:
        dividir = linea.strip().split()

        if dividir:
            if not fila:
                fila = [int(dividir[0]), int(dividir[1]), float(dividir[2].replace(',', '.')), " ".join(dividir[4:])]
            else:
                fila[3] += " " + " ".join(dividir)
        else:
            if fila:
                fila[3] = fila[3].replace('.', '')
                datos.append(fila[:4])
                fila = []

    columnas = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
    return pd.DataFrame(datos, columns=columnas)

if __name__ == "__main__":
    df_tabla = pregunta_01()
    print(df_tabla)

    
"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
