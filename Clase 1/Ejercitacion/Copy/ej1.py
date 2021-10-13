import pandas as pd
import os

from pandas.core.frame import DataFrame
from pandas.io.stata import excessive_string_length_error


def selectname(nombreO):

    for i in range(1,99):
        if(os.path.exists("D:\Documents\Work\Analisis_de_Datos\Clase 1\Ejercitacion\Copy\\"+"Copia "+str(i)+" -"+nombreO) == False):
            return "Copia "+str(i)+" -"+nombreO
        else:
            continue
   

    return nombre

def copianator(df, nombre):
    df2 = df.to_dict()
    dataFrame = pd.DataFrame(df2)
    dataFrame.to_excel("D:\Documents\Work\Analisis_de_Datos\Clase 1\Ejercitacion\Copy\\"+selectname(nombre))
    return


nombre = "Datos.xlsx"
df = pd.read_excel("D:\Documents\Work\Analisis_de_Datos\Clase 1\Ejercitacion\Copy\\" + nombre)
copianator(df, nombre)
