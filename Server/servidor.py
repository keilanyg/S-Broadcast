import threading
import socket

"""
    Função Broadcast: Envia mensagem para todos os clientes, exceto para quem a enviou. 
    Caso o cliente não exista mais, ele é removido da lista de clientes.
    Função MessagesTreatment: Responsável de receber as mensagens de cada usuário

"""

clients = [] #Armazena a lista de usuários

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 5000))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            clients.remove(client)
            break

def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                clients.remove(client)

main()