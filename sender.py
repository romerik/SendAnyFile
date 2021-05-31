#coding:utf-8
import socket
import threading
import sys

print("""
                  ____                 _                         
                 / ___|  ___ _ __   __| | ___ _ __               
                 \___ \ / _ \ '_ \ / _` |/ _ \ '__|              
                  ___) |  __/ | | | (_| |  __/ |                 
 _____ _____ ____|____/ \___|_| |_|\__,_|\___|_|____ _____ _____ 
|_____|_____|_____|                           |_____|_____|_____|

""")

print("Please run this script in the file you want to send folder")

fileName = input("The file you want to send name : ")
try:
    with open(fileName,'r') as fichier:
                contenu=fichier.read()
except:
    try:
        with open(fileName,'rb') as fichier:
                    contenu=fichier.read()
    except:
        print("Fichier introuvable")
        sys.exit(0)


serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
port = 5555
receiverAdress = input("Receiver IP Adress : ")

try:
    serverSocket.connect((receiverAdress,port))
except:
    print("Connection failed")

message ={'filename':fileName,'content':contenu}
message = "{}".format(message)
serverSocket.sendall(message.encode())

print("Fichier bien envoyé\nConnection clause")

serverSocket.close()
