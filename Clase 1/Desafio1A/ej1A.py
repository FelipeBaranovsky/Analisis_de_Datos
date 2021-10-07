
#wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx"

'''
Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato.
 El archivo tiene cuatro columnas
  Equipo, Puntos, Goles a favor y Goles en contra. 
  Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra),
   y mostrar todas las diferencias de gol usando print.
'''
import pandas as pd

df = pd.read_excel("Tabla1.xlsx", index_col = "Equipo")

data = df.to_dict("index")

print("Diferencia de goles: \n")
for i in data:
   print(i,": ",(data[i]["Goles a favor"]-data[i]["Goles en contra"]))
   


