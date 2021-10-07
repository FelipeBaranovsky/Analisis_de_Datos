import pandas as pd

data = {
    "Personas" : ["Felipe", "Marcos", "Eduardo"],
    "Nota" : [10,10,10],
    "Asistencias" : [4,8,0]
}

dataframe = pd.DataFrame(data)
print(dataframe)
dataframe.to_excel("ej2.xlsx")


