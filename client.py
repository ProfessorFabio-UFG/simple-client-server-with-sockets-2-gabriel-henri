from socket  import *
from constCS import *
from threading import *

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((HOST, PORT)) 


def receber_mensagem():
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            print(mensagem)
        except:
            print("Conexão perdida")
            cliente.close()
            break

thread_receber = Thread(target=receber_mensagem)
thread_receber.start()

while True:
    mensagem = input("")
    if mensagem.lower() == "sair":
        cliente.close()
        break
    cliente.send(mensagem.encode())