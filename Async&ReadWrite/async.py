import asyncio

#Rutas de archivo de lectura y escritura
rR="lectura.txt"
rW="escritura.txt"

#Se inicializa el archivo y se dan permisos
#r: read only w: write
aR=open(rR,"r")
aW=open(rW,"w")

#función de escritura sobre archivo de lectura "r" y escritura "w"
def fWrite(r,w):
    #Bucle que lee todas las lineas del archivo de lectura y las escribe en archivo de escritura
    for line in r.readlines():
        w.write(line)
        print(line)
    #Cierre de archivos de lectura y escritura
    w.close()
    r.close()
    return 0

    
