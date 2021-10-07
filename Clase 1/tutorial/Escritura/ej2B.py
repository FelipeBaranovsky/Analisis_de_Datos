import pandas as pd

df = pd.read_excel("ej2.xlsx")
print(df)
columna = "Nota"
print(df[columna])
indice = 0

print("\n---------df.loc[indice]---------\n")
print(df.loc[indice])

print("\n---------df.loc[indice][columna]---------\n")
print(df.loc[indice][columna])

print("\n---------cantidad de celdas---------\n")
print(df.size) # cantidad de celdas

print("\n---------(filas, columnas)---------\n")
print(df.shape) # (filas, columnas)

print("\n---------(tabla + info extra)---------\n")
print(df.info())  # tabla + info extra de las columnas

pd.set_option("display.max_columns", 2)
print(df)