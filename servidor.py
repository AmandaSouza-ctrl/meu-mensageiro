import socket
import struct
import _thread
import time
import csv
import json

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

# Campos da mensagem
idSensor = None
tpSensor = None
vlSensor = None
nmSensor = None
structsize = 28
CST_USUARIO = "usuario"
csv_usuarios_sistema = "./usuarios_sistema.csv"
csv_mensagens = "./mensagens.csv"

def carrega_arquivo(arquivo):
	lista=[]
	
	with open(arquivo, newline="") as csvfile:
		itens = csv.reader(csvfile, delimiter=',')
		for item in itens:
			lista.append(item[0])
	#print(lista)
	return lista

def verifica_usuario(informacao_usuario,arquivo_usuario_sistema):

	if informacao_usuario in arquivo_usuario_sistema:
		return True
	else:
		return False

def armazena_mensagem (chave,mensagem):
	
	dict_mensagem={chave:mensagem}
	with open(csv_mensagens,"a",newline="", encoding="utf-8") as csvfile:
		escreve = csv.writer(csvfile)

		for itens in mensagem:
			escreve.writerow([chave,itens])

def destinatario(mensagem):
	
	dest = mensagem.split()
	dest= dest[0].split('@')
	
	return(dest[1])
	
# Funcao de recepcao e desempacotamento da mensagem
def myRecv (socket):
	try:
		msg = socket.recv(structsize)
		print (cliente, msg)
		return struct.unpack('!IHh20s', msg)
	except:
		return None

def conectado(con, cliente, informacao_usuario,arquivo_usuario_sistema):

	print("Conectado ao cliente: ", cliente)
	idSensor, tpSensor, vlSensor, nmSensor = myRecv(con)
	print (cliente, idSensor, tpSensor, vlSensor, nmSensor.decode())
	dict_mensagens={}
	lista=[]
	while True:
		msg = con.recv(1024)
		if not msg:
			break
		#lista.append(msg.decode())
		
		dest=destinatario(msg.decode())
		if verifica_usuario(dest,arquivo_usuario_sistema):
			print('entrou')
		else:
			print("Destinatário não existe na base de usuário. Desconectando cliente")
			_thread.exit()
			#dict_mensagem = armazena_mensagem(informacao_usuario,lista)
		#escreve_aquivo(informacao_usuario,dict_mensagem)
		print(cliente, ": ", msg.decode())
		
	print("Cliente desconectado: ", cliente)
	#tcp.close() #fechei a conexao com o cliente
	_thread.exit()

### Inicio da execucao do programa
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

#abre o arquivo
arquivo_usuario_sistema = carrega_arquivo("./usuarios_sistema.csv")

while True:
	con, cliente = tcp.accept()
	informacao_usuario = con.recv(1024)
	
	#if not informacao_usuario:
	#	 break
	
	informacao_usuario=str(json.loads(informacao_usuario))
	print("informacao: ", informacao_usuario)
	if verifica_usuario (informacao_usuario,arquivo_usuario_sistema):
		_thread.start_new_thread(conectado, tuple([con,cliente,informacao_usuario,arquivo_usuario_sistema])) #chama o conectado
	else:
		print("Cliente não existe na base de usuário. Desconectando cliente")
	#tcp.close() #fechei a conexao com o cliente
		_thread.exit()

tcp.close()
