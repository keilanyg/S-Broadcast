# S-Broadcast
Conexão entre vários clientes. Sistema que utiliza um Broadcast para um cliente enviar uma mensagem para os demais. 
Com Threads que são usadas para enviar e receber mensagens paralelamente. 

Primeiro o cliente tenta fazer uma conexão com um servidor, logo após é inserido o nome do usuário.

SendMessages = Função que envia as mensagens, o usuário escreve a mensagem, essa mensagem é transformada de String para BYTE, através do ENCODE.

ReceiveMessages = Função que faz o recebimento de mensagens, que ao ser recebida, essa mensagem é transformada de BYTE para String. 

Função Broadcast: Envia mensagem para todos os clientes, exceto para quem a enviou. Caso o cliente não exista mais, ele é removido da lista de clientes.

Função MessagesTreatment: Responsável de receber as mensagens de cada usuário

AF INET -> IPV4

SOCK STREAM -> TCP

PORT = 5000 

ENCODE = Transforma string em BYTE 

DECODE = Transforma BYTE em string
