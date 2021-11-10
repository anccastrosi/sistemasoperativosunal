import socket
import os


PORT = 2498
# socket del servidor
ftpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ftpServer.bind((socket.gethostname(), PORT))
ftpServer.listen(3)
conn, addr = ftpServer.accept()

# se suben archivos desde el cliente, hasta que el cliente envíe la señal de EOF, indicando que se alcanzó el final
# del archivo


def receiveFile(filename):
    dataOfFile = ""
    file = open(filename, "w")
    while dataOfFile[-3:] != "EOF":
        data = conn.recv(1024)
        dataOfFile = data.decode()
        data = dataOfFile.split("\n")
        for line in data:
            if line.strip() != "EOF":
                file.write(line)
    file.close()

# se envía la lista de archivos, archivo a archivo


def sendListOfFiles():
    listOfFiles = os.listdir(os.getcwd())
    conn.send(str(len(listOfFiles)).encode())
    print(listOfFiles)
    for file in listOfFiles:
        print(file)
        conn.send((file + ";").encode())


# bucle while para estar escuchando comandos por parte del cliente
# S: para subir un archivo
# L: para obtener la lista de archivos subidos
while True:
    cmd = conn.recv(32).decode("utf-8")
    if cmd[0] == "S":
        filename = (cmd[1:]).strip()
        receiveFile(filename)
    if cmd[0] == "L":
        sendListOfFiles()
