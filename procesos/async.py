import asyncio

#función de escritura sobre archivo de lectura "r" y escritura "w"
async def fWrite(r,w):
    #Bucle que lee todas las lineas del archivo de lectura y las escribe en archivo de escritura
    for line in r.readlines():
        w.write(line)
        await asyncio.sleep(0.25)
    #Cierre de archivos de lectura y escritura
    w.close()
    r.close()
    print("copia ejecutada")
    print("archivos cerrados")
    return line

async def fAsync ():
    for i in range (10):
        print(i)
        await asyncio.sleep(1)
    return 0    

async def main ():
    #Rutas de archivo de lectura y escritura
    rR="procesos/lectura.txt"
    rW="procesos/escritura.txt"
    await asyncio.sleep(1)
    print("rutas establecidas")
    

    #Se inicializa el archivo y se dan permisos
    #r: read only w: write
    aR=open(rR,"r")
    aW=open(rW,"w")
    await asyncio.sleep(1)
    print("archivos abiertos")

    task1=asyncio.create_task(fAsync())
    task2=asyncio.create_task(fWrite(aR,aW))

    value = await task2
    print("Ultimo valor copiado: "+value)
    await task1


    return 0

asyncio.run(main())