import hashlib
import os




def sha1file(filename):
    with open(filename, "rb") as file:
        content = file.read()
        hashSha1 = (hashlib.sha1(content)).hexdigest()
        return hashSha1


with open("hash.txt","a") as file:
    # hash punto 1
    file.write("Punto 1:\n " + sha1file("Punto1\punto1.py") + "\n")

    #hash punto 2
    file.write("Punto 2:\n")
    file.write("- punto2.py: " + sha1file("punto2\punto2.py") + "\n")
    #file.write("- market BTC.txt: " + sha1file("punto2\market BTC.txt") + "\n")
    #file.write("- ticker BTC.txt: " + sha1file(r"punto2\ticker BTC.txt") + "\n")
    #file.write("- orderBook BTC.txt: " + sha1file("punto2\orderBook BTC.txt") + "\n")

    # hash punto 3
    file.write("Punto 3:\n ")
    file.write("- punto3.py: " + sha1file("Punto3\punto3.py") + "\n")
    file.write("- web.html: " + sha1file("Punto3\web.html") + "\n")

    # hash punto 4
    file.write("Punto 4:\n ")
    # cliente
    file.write("- cliente:\n ")
    file.write("-- client.py: " + sha1file("punto4\cliente\cliente.py") + "\n")
    file.write("-- file.txt: " + sha1file(r"punto4\cliente\Test.txt") + "\n")
    # servidor
    file.write("- servidor:\n ")
    file.write("- server.py: " + sha1file("punto4\servidor.py") + "\n")