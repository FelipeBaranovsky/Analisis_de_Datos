#wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx"

'''
Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato y determinar 
qué equipo es el campeón (1ro) y perdedor (último).
 El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra.

'''


import pandas as pd

df = pd.read_excel("Tabla1.xlsx", index_col="Equipo")
data = df.to_dict("index")  #para obtener cada fila

perdedor = ["Nombre", 99999] 
ganador = ["Nombre", 0] 

for i in data:
    if (int(data[i]["Puntos"]) > ganador[1] or int(data[i]["Puntos"]) == 0):
       ganador[0] = i
       ganador[1] = int(data[i]["Puntos"])
    if (int(data[i]["Puntos"]) < perdedor[1] or int(data[i]["Puntos"]) == 0):
       perdedor[0] = i
       perdedor[1] = int(data[i]["Puntos"])

print("GANADOR --> ", ganador[0], " pts: ", ganador[1])
print("PERDEDOR --> ", perdedor[0], "pts: ", perdedor[1])