'''
Escribir una funcion que reciba como parámetros: una variable de tipo DataFrame (la tabla de alumnos) y el índice de un alumno. 
Luego debe devolver con return el promedio de sus notas en las diferentes materias.
'''
import pandas as pd

def funcion(dataframe, indice):
    alumno = dataframe.to_dict("index")
    alumno = alumno[indice]
    suma = 0.0
    divisor = 0.0
    
    del alumno["Nombre"]
    del alumno["Apellido"]
    del alumno["Legajo"]
    
   
    for i in alumno:
        suma += alumno[i]
        divisor += 1
    promedio = suma / divisor
    
    


    '''
    dataframe = dataframe[ dataframe["Nombre"] == "Maria" ]
    print(dataframe) 
    '''                        
     
    #promedio = (alumno["Quimica"] + alumno["Fisica"] + alumno["Matematica"])/3
    
    return promedio

df = pd.read_excel("Datos.xlsx")

print("Pmedio de Maria", funcion(df, 2))
