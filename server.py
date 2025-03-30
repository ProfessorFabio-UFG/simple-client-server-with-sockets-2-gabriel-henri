from socket import *
from constCS import *  #-
from threading import *

clientes = []

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(5)  # Permite até 5 conexões simultâneas

def enviaMensagem(mensagem, remetente):
    for cliente in clientes:
        if cliente != remetente:  # Evita que o remetente receba a própria mensagem
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                clientes.remove(cliente)

def controlaCliente(cliente):  # Agora recebe o cliente como argumento
    while True:
        try:
            mensagem = cliente.recv(1024)
            if mensagem:
                enviaMensagem(mensagem, cliente)
        except:
            break
    clientes.remove(cliente)
    cliente.close()

while True:
    cliente, endereco = s.accept()
    print(f"Nova conexão: {endereco}")
    clientes.append(cliente)

    thread = Thread(target=controlaCliente, args=(cliente,))
    thread.start()
