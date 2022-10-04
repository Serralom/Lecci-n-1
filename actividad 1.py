import pandas as pd

#Se modifica el df para que sea apto para su manejo
df = pd.read_csv("./finanzas2020[1].csv", sep='\t')
for column in df:
    df[column] = pd.to_numeric(df[column], errors='coerce')

#Para obtener los meses con mayor y menor gastos

#Establecemos valores de referencia para utilizarlo posteriormente
max = -10000
min = 10000
total = 0
gasto = 0
ingreso = 0

#El mes con menos ingresos medios será en el que más se haya gastado
for column in df:
    a = df[column].mean()
    if a < min:
        min = a
        mesmin = column
print(f'El mes en el que se ha gastado más es {mesmin}')

#El mes con más ingresos medios será en el que más se haya ahorrado
for column in df:
    a = df[column].mean()
    if a > max:
        max = a
        mesmax = column

print(f'El mes en el que se ha ahorrado más es {mesmax}')

#La media de gastos anual es igual a la media de la media mensual
for column in df:
    a = df[column].mean()
    total += a

media = round(total/12, 2)
print(f'La media de gastos es de {media}€ anuales')

#El gasto total es igual a la suma de gastos de todo el año
df_gastos = df[df > 0]

for column in df_gastos:
    a = df_gastos[column].sum()
    gasto += a
print(f'El gasto total a lo largo del año es de {gasto}€')

#Los ingresos totales son iguales a la suma de los ingresos de todo el año
df_ingresos = df[df < 0]
for column in df_ingresos:
    a = df_ingresos[column].sum()
    ingreso += a
print(f'Los ingresos totales son de {ingreso}€')

