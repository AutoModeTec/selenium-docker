# awsproduct

# 1.0) Subindo o servidor docker

**Version 1.0.0**

Código e exemplos sobre subir o servidor docker e executar o programa.


## Requisitos:

#### Docker e docker compose
	
Esse link te dará mais informações de como fazer isso: https://docs.docker.com/docker-for-windows/install/

#### Python

No link abaixo está disponivel o instalador do python: https://www.python.org/downloads/

#### Selenium

Após a instalação do python coloque esse comando para instalar a biblioteca selenium:

	$ pip install selenium


## Como usar:

#### Para inicializar o servidor:

Com o terminal na pasta do arquivo "docker-compose.yml" digite:
    
        $ docker-compose up 

Ou, para rodar o arquivo em background:

	$ docker-compose up -d

Para desligar o servidor:

	$ docker-compose down

# 2.0) Ligando o software
Com o terminal na pasta do arquivo "main.py" digite:
    
    $ python3 main.py

#### Com isso o programa permanecerá rodando e enviando para números novos adicionados no banco de dados

# 3.0) O que cada parte do código faz:

## "main.py":

#### ![image](https://user-images.githubusercontent.com/70957747/120118805-d5a53400-c16a-11eb-8899-6b11df42a814.png)

Essa função é responsável por enviar a screenshot da página para o Banco de Dados.

#### ![image](https://user-images.githubusercontent.com/70957747/120118877-1735df00-c16b-11eb-820a-6995449cae1c.png)

Essa função é responsável por verificar se existem novos números no Banco de Dados, se já foi enviada mensagem para esse e, por fim, realizar o gatilho para o envio.

#### ![image](https://user-images.githubusercontent.com/70957747/120118928-55330300-c16b-11eb-87e6-75c8a2ab4bcc.png)

Essa função é responsável por verificar se o QrCode já foi lido pelo usuário.

## Pasta Scripts:
#### ![image](https://user-images.githubusercontent.com/70957747/120119065-06399d80-c16c-11eb-954c-96ff637a266a.png)

Essa função é responsável por verificar se a mensagem foi enviada.

#### ![image](https://user-images.githubusercontent.com/70957747/120119317-6c72f000-c16d-11eb-89cd-dffb92db2e54.png)

Essa função é responsável por passar as tabelas de dados do Banco de Dados para um arquivo excel e salvá-lo na pasta.

#### ![image](https://user-images.githubusercontent.com/70957747/120119355-b065f500-c16d-11eb-8be1-d925f46fe93b.png)

Essa função é responsável por adicionar em uma tabela do Banco de Dados os números não existentes.

#### ![image](https://user-images.githubusercontent.com/70957747/120119369-c5db1f00-c16d-11eb-8701-b433c2b6ef09.png)

Essa função é responsável por adicionar em uma tabela do Banco de Dados os números em que o envio falhou.

#### ![image](https://user-images.githubusercontent.com/70957747/120119525-79441380-c16e-11eb-9060-c8de99a3e46a.png)

Essa classe é responsável pelo envio de mensagens através da pesquisa por contatos dentro do WhatsApp.

#### ![image](https://user-images.githubusercontent.com/70957747/120119543-a1337700-c16e-11eb-8638-c7307965a682.png)

Essa classe é responsável por enviar mensagens para números através da URL.

#### ![image](https://user-images.githubusercontent.com/70957747/120119561-c7591700-c16e-11eb-80b8-f92bf3f68764.png)

Essa função é responsável por ler arquivos csv e extrair os números dentro deles.

#### ![image](https://user-images.githubusercontent.com/70957747/120119607-012a1d80-c16f-11eb-8b4d-2f6f80f23637.png)

Essa função é responsável por verificar quais chats possuem respostas.

#### ![image](https://user-images.githubusercontent.com/70957747/120119618-14d58400-c16f-11eb-9324-f494513a8caa.png)

Essa função é responsável pelo ordenamento da lista de números que responderam.

## Pasta Bot:
####

Essa função é responsável por

####

Essa função é responsável por

####

Essa função é responsável por


---

## License & copyright

© Automode  


