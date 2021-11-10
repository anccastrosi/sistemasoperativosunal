import socket

IP = socket.gethostname()
PORT = 2498
ADDR = (IP, PORT)
FORMAT = "utf-8"
BUFFER_SIZE = 1024


# se sube un archivo al servidor
def uploadFile(filename):
    # se envía la información del archivo en pedazos de 1024 bytes
    try:
        content = open(filename, "rb")
        l = content.read(BUFFER_SIZE)
        while l:
            s.send(l)
            l = content.read(BUFFER_SIZE)
        # se envía un EOF para indicar que se ha enviado el archivo
        s.send("\nEOF".encode())
        content.close()
    except:
        print(f"Archivo {filename} no encontrado")


# se obtiene la lista de archivos subidos al servidor, archivo a archivo
def listOfFiles():
    s.send("L".encode())
    lenFiles = int(s.recv(1).decode())
    data = ""
    for i in range(lenFiles):
        data += s.recv(1024).decode()
    ls = data.split(";")
    return ls


# se obtiene el comando por parte del cliente para
# S: Subir archivo
# L: Ver lista de archivos en el servidor
def getCommand():
    cmd = input(
        "Ingrese comando a ejecutar (S: Subir Archivo, L: Ver lista de archivos en el servidor): ")
    if cmd[0] == "S":
        filename = input("Ingrese nombre de archivo a subir: ")
        if not (filename in listOfFiles()):
            cmdS = ("S" + filename).encode()
            s.send(cmdS)
            uploadFile(filename)
        else:
            print("El archivo ya fue subido")

    if cmd[0] == "L":
        files = listOfFiles()
        print(files)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

# bucle while para recibir comandos por consola
while 1:
    getCommand()
