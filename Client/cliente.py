"""
Conexão entre vários clientes. Sistema que utiliza um Broadcast para um cliente enviar uma mensagem para os demais. 
Com Threads que são usadas para enviar e receber mensagens paralelamente. 

Primeiro o cliente tenta fazer uma conexão com um servidor, logo após é inserido o nome do usuário.

SendMessages = Função que envia as mensagens, o usuário escreve a mensagem, essa mensagem é transformada de String para BYTE, através do ENCODE.
ReceiveMessages = Função que faz o recebimento de mensagens, que ao ser recebida, essa mensagem é transformada de BYTE para String. 

AF INET -> IPV4
SOCK STREAM -> TCP
PORT = 5000  
ENCODE = Transforma string em BYTE 
DECODE = Transforma BYTE em string 
"""

import threading
import socket

def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(('localhost', 5000))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário: ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[cliente])
    thread2 = threading.Thread(target=sendMessages, args=[cliente, username])

    thread1.start()
    thread2.start()

#Enviar mensagens
def sendMessages(cliente, username):
    msg = input('\n')
    cliente.send(f'{username}: {msg}'.encode('utf-8')) 

#Receber mensagens
def receiveMessages(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            print(msg,'\n')
        except:
            print('\nVocê foi desconectado no servidor!\n')
            cliente.close()
            break
main()