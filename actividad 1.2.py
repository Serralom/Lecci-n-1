from msilib.schema import Error
import pandas as pd

#Comprobar si el fichero está disponible
try:
    df = pd.read_csv("./finanzas2020[1].csv", sep='\t')
    print("Fichero disponible")
except Error:
    print ("No se ha encontrado el archivo")

#Comprobar si el fichero contiene todos los meses
columnas = df.columns.tolist()
try:
    print("El fichero contiene todos los meses del año")
except len(columnas) == 12:
    print("Hay algun error en los meses del fichero")

#Comprobar si cada mes contiene datos
for column in df:
    try:
        print(f'{column} contiene datos')
    except df[column].empty == True:
        print(f'{column} no contiene datos')

#Comprobar si cada valor es válido
contador = 0
for column in df:
    for row in df:
        try:
            pass
        except df[column][row].dtypes != float:
            contador += 1
print(f'Hay {contador} valor/es no válidos')