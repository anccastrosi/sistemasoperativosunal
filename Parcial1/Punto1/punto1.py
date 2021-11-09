import pandas as pd
from pandas.io.json import json_normalize
# Solo escribir en el excel desde el JSON

# Abriendo el JSON
df = pd.read_json('src.json')
print(df)
# Writing Excel File:
df.to_excel('data.xlsx')
aW = open("funciones.txt", "w")
#imprime todas las posibles combinaciones entre nombre y descripción
for k,v in df.name,df.description:
    aW.write(str(k)+" "+str(v)+"\n")
    print(k+" "+v)
