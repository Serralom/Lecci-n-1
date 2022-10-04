import pandas as pd

datos = pd.read_csv("techogar.csv", header=0)

#print(datos)
#print (datos['Cable'])
#print(datos.head)
#print(datos.sort_values(by='Teléfono', ascending=False))
#print(datos[datos.ix[:5]<10])
tel = datos['Teléfono']
print(tel[tel>10])

#print(df["Enero"][:10]) #Muestra desde el primer valor hasta el 10
#print(df['Enero'])
#print(df.columns.tolist())
#print(df.describe())
#print(df.idxmax())
#print(df.max())
#print(df)