from socket import *
import asyncio

async def webServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setblocking(False)
    serversocket.bind(('localhost',8442))
    serversocket.listen()

    f = open('web.html', 'r')
    webPage = f.read()
    loop = asyncio.get_event_loop()
    while(1):#aquí va lo que queremos que el servidor haga
        
        #Aceptamos las conexiones desde fuera
        (clientsocket, address) = await loop.sock_accept(serversocket)

        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"

        data += webPage
        data += "\r\n\r\n"

        clientsocket.sendall(data.encode())

        clientsocket.shutdown(SHUT_WR)


    serversocket.close()
    

asyncio.run(webServer())