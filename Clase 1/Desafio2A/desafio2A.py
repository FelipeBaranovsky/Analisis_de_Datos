
'''
### Mini desafío 2.A
Calcular el promedio de las notas de química de todos los alumnos en el archivo 
**Datos.xlsx**.

- **Tip:** Podemos usar la función **sum**($iterable$) para obtener la suma de todos los campos. Un ejemplo de como funciona:
python
mi_lista = [1, 2, 3, 4, 5]
total = sum(mi_lista)
print(total)

 ¡La función **len()** también sigue siendo válida!
'''

import pandas as pd

df = pd.read_excel("Datos.xlsx")
data = df.to_dict("list")

promedio = sum(data["Quimica"])/df.shape[0]

print("Promedio: ", promedio)