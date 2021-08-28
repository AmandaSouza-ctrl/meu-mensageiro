import socket
import struct
import json

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
# Campos da mensagem
idSensor = 2		# inteiro de 4 bytes sem sinal
tpSensor = 6		# inteiro de 2 bytes sem sinal
vlSensor = 32			# inteiro de 2 bytes
nmSensor = "Sensor de presença"  #Ate 20 bytes
structsize = 28			# quantidade de bytes da mensagem

# Funcao de empacotamento e envio de da mensagem
def mySend (socket, idSensor, tpSensor, vlSensor):
	msg = struct.pack('!IHh20s', idSensor, tpSensor, vlSensor, nmSensor.encode())
	print (msg)
	socket.send (msg)

######### Inicio do programa
nome_usuario=input('Informe o nome do usuário: ')


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
#tcp.send(nome_usuario.encode())
nome_usuario = str.encode(json.dumps(nome_usuario)) 
tcp.send(nome_usuario)
mySend (tcp, idSensor, tpSensor, vlSensor)

#nome_usuario=[]
#nome_usuario=input('Informar login: ')
#nome_usuario= str.encode(json.dumps(nome_usuario))
#tcp.send(nome_usuario)
#tcp.send(nome_usuario.encode())

######### Envia uma mensagem
print ('Para sair use CTRL+X\n')
print( 'para enviar uma mensagem utilize o formato: @usuario_destino<espaço em branco> texto completo da mensagem<enter>')
msg = input("Digite uma mensagem: ")
while msg != '\x18':
 	tcp.send (msg.encode())
 	msg = input("Digite uma mensagem: ")

tcp.close()
