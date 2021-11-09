import socket
import ssl

target_host = "www.buda.com"
# puerto 443, el cual está abierto para escuchar conexiones TCP
target_port = 443
context = ssl.create_default_context()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# se envuelve el socket con SSL para solicitar datos a Buda de manera segura
client = context.wrap_socket(client, server_hostname=target_host)

client.connect((target_host, target_port))


def obtenerInfoMercadoBitcoin():

    request = "GET /api/v2/markets/btc-cop HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("market BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()
        f.write(data + "\n")
    f.close()


def obtenerTickerMercadoBitcoin():
    request = "GET /api/v2/markets/btc-cop/ticker HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("ticker BTC.txt", "w")
    data = ""
    print(f"DATA: {data}")
    response = client.recv(4096)
    data = response.decode()
    f.write(data)
    f.close()


def obtenerLibroMercadoBitcoin():
    request = "GET /api/v2/markets/btc-cop/order_book HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("orderBook BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()
        f.write(data)

    f.close()


def obtenerCostoAbonosRetiros():
    request = "GET /api/v2/currencies/btc/fees/withdrawal HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("withdrawal_BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()
        f.write(data)

    f.close()


def obtenerTrades():
    request = "GET /api/v2/markets/btc-cop/trades HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("trades_BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()
        f.write(data)
    f.close()


def obtenerVolumen():
    request = "GET /api/v2/markets/btc-cop/volume HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host
    client.send(request.encode())
    f = open("volume_BTC.txt", "w")
    data = ""
    while data.strip() != "0":
        response = client.recv(4096)
        data = response.decode()
        f.write(data)
    f.close()


obtenerInfoMercadoBitcoin()
obtenerTickerMercadoBitcoin()
obtenerLibroMercadoBitcoin()
obtenerCostoAbonosRetiros()
obtenerTrades()
obtenerVolumen()
