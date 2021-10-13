import pandas as pd

df = pd.read_excel("D:\Documents\Work\Analisis_de_Datos\Clase 1\Desafio 3\Datos.xlsx", index_col = "Legajo")

data = df.to_dict("index")

for i in data:
    if data[i]["Matematica"] >= 4:
        print("Promedio de ",data[i]["Apellido"],": ",(data[i]["Matematica"] + data[i]["Quimica"] + data[i]["Fisica"])/3)
        

