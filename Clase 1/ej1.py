#Import pandas
import pandas as pd
df = pd.read_excel("Datos.xlsx")
data = df.to_dict("list")
print(data["Nombre"])
print(data)
print(df)