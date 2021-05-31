#coding:utf-8
import socket
import threading
import os
import ast

print("""
                  ____               _                              
                 |  _ \ ___  ___ ___(_)_   _____ _ __               
                 | |_) / _ \/ __/ _ \ \ \ / / _ \ '__|              
                 |  _ <  __/ (_|  __/ |\ V /  __/ |                 
 _____ _____ ____|_| \_\___|\___\___|_| \_/ \___|_|____ _____ _____ 
|_____|_____|_____|                              |_____|_____|_____|

""")

class ClientSocket(threading.Thread):
    def __init__(self,sockClient,ip,address):
        threading.Thread.__init__(self)
        self.sockClient=sockClient
        self.ip,self.address=(ip,address)
        print("Connecion by {} {}".format(self.ip,self.address))
    def run(self):
        reponse=self.sockClient.recv(1024).decode("utf8")
        fileNameAndContent = ""
        while reponse:
            fileNameAndContent+=reponse
            reponse=self.sockClient.recv(1024000).decode("utf8")
        fileNameAndContent = ast.literal_eval(fileNameAndContent)
        fileName,contentFile = fileNameAndContent['filename'],fileNameAndContent['content']
        with open(fileName,'w+') as fichier:
            pass
        
        if type(contentFile) == str:
            with open(fileName,'w') as fichier:
                fichier.write(contentFile)
        else:
            with open(fileName,'wb') as fichier:
                fichier.write(contentFile)
        
        print("Fichier bien reçu")
        print("Connection Terminée avec l'adresse ip {} connecté au port {}".format(self.ip,self.address))
        self.sockClient.close()

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
port = 5555
serverSocket.bind(("",port))
print("......Listening..... on port {}".format(port))

while True:
    serverSocket.listen(10)
    newClient,(ip,address)=serverSocket.accept()
    newThread=ClientSocket(newClient,ip,address)
    newThread.start()
