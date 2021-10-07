#Import pandas
import pandas as pd
df = pd.read_excel("Datos.xlsx")

#TODO: LIST -> significa que vamos a almacenar a cada columna como una lista con su contenido
data = df.to_dict("list")
print(data["Nombre"])
print("\n")
print(data)
print("\n")

#TODO: RECORDS-> significa que vamos a obtener el contenido separado por cada fila
data = df.to_dict("records")
print(data[2]["Nombre"])
print("\n")
print(data[2])
print("\n")
print(data)
print("\n")

#TODO: INDEX -> significa que vamos a obtener el contenido como diccionarios 
# donde la clave es algun campo de cada fila, en este caso la clave de los 
# diccionarios será la clave "Apellido"
df = pd.read_excel("Datos.xlsx", index_col ="Apellido") 
data = df.to_dict("index")
print(data["Martinez"])
print("\n")
print(data["Martinez"]["Legajo"])
print("\n")
print(data)
print("\n")
print(df)
