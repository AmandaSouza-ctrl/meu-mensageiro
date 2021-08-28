# meu-mensageiro

O objetivo do trabalho é desenvolver uma aplicação cliente/servidor para troca de mensagens 
instantâneas, utilizando a biblioteca de programação socket na linguagem Python, versão 3.6, ou superior.

Os objetivos específicos do trabalho são:

◦ Familiarizar-se com a programação utilizando a API socket.

◦ Enviar e receber dados em uma aplicação que utiliza a arquitetura Cliente/Servidor.

◦ Entender o conceito de protocolos

◦ Entender o funcionamento de aplicações concorrentes


1.3 Descrição do trabalho
Neste trabalho você será desafiado a desenvolver uma aplicação distribuída chamada MeuMensageiro,
conforme as instruções apresentadas neste documento

1.1.1 Identificação dos componentes do sistema

• Servidor: 

o Uma aplicação escrita em Python com programação concorrente que irá tratar atenderá vários 
clientes simultaneamente.
o Possuirá uma base de dados (arquivo CSV) com os usuários registrados no sistema.
o Possuirá uma base de dados (arquivo CSV) com as mensagens.

• Cliente: 

o Uma aplicação escrita em Python que permitirá que os usuários registrados troquem 
mensagens entre si.

1.1.2 Funcionamento básico do sistema

Ao iniciar, o servidor deverá:

1. ler a base de usuários cadastrados e armazenar em memória;
2. entrar em um loop:
a. aguardar por conexões na porta TCP 3333. 
b. criar uma Thread para cada usuário conectado. Caso o usuário informado pelo cliente não 
esteja na base de usuários do servidor, o cliente deverá ser desconectado.

Ao iniciar, o cliente deverá:

1. solicitar o nome do usuário;
2. conectar-se no servidor;
3. entrar em um loop:

  a. baixar as novas mensagens do usuário, se houver;
  b. imprimir as mensagens na tela;
  c. aguardar o usuário enviar mensagens.
  
Troca de mensagens:

Do lado do cliente:

1. Para enviar uma nova mensagem, deve-se utilizar o seguinte formado:

@usuário_destino <espaço em branco> texto completo da mensagem <enter>

2. Após enviar a mensagem o cliente irá buscar novas mensagens no servidor, se houve.

Do lado do servidor:

1. Ao receber uma nova mensagem, o servidor irá:

  a. Verificar se o destinatário existe;
  b. Se existir, irá armazenar a mensagem em um dicionário cuja chave é o login do 
usuário.
  c. Caso o usuário não exista, a mensagem será descartada.
  d. Quando a mensagem for lida pelo destinatário, o servidor irá registrar mensagem no 
arquivo base de dados de mensagem.

2. Após receber uma mensagem o servidor enviará as mensagens novas para este usuário, uma 
por vez. Ao finalizar o envio de todas as mensagens novas, será enviado uma mensagem com 
o caractere ‘f’ informando que fim das mensagens
