# 📚  API de Reserva de Salas

## 🧠 Objetivo Geral

Este repositório contém a API de Reserva de Salas, desenvolvida com Flask e SQLAlchemy, como parte de uma arquitetura baseada em microsserviços.

## 🧩 Arquitetura

A API de Reserva de Salas é um microsserviço que faz parte de um sistema maior chamado School System, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ A API depende da [API de Gerenciamento Escolar](https://github.com/hermosoarthur/API-FLASK), que deve estar em execução para o sistema funcionar corretamente.

A comunicação entre os serviços ocorre via requisições HTTP REST, para validar:

Se a Turma existe: GET /turmas/<id>

(Opcional) Se o Aluno existe: GET /alunos/<id> → Pode ser desativado se não for usado.

## 🚀 Tecnologias Utilizadas

Python 3.x

Flask

SQLAlchemy

SQLite (como banco de dados local)

Requests (para consumo da API externa)

## ▶️ Como Executar a API com Docker

1. **Clone o repositório:**
```bash
git clone https://github.com/hermosoarthur/API-FLASK
cd API-FLASK
```                                                                                                                                                                                                     
2. Executar com Docker (recomendado):
```bash
docker network create api-network
```
Essa rede será utilizada por todas as APIs que fazem parte do sistema de microsserviços (como as APIs de Gestão e Reservas), permitindo que elas se comuniquem entre si. *(OBS: caso já tenha feito a execução da API de gestão não é necessario criar )*

3. Construa a imagem da API
```bash
docker build -t api-rsv .
```
4. Execute o container utilizando a rede criada:
```bash
docker run -d --name api-rsv --network api-network -p 5001:5001 api-arsv
```
A aplicação estará disponível em: 📍 http://localhost:5001/reservas

## 📡 Endpoints Principais

GET /reservas → Lista todas as reservas

POST /reservas → Cria uma nova reserva

GET /reservas/<id> → Detalha uma reserva

PUT /reservas/<id> → Atualiza uma reserva

DELETE /reservas/<id> → Remove uma reserva

Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-06",
  "hora_inicio": "14:00",
  "hora_fim": "16:00"
}
```

# 🔗 Dependência Externa

Certifique-se de que a API de Gerenciamento Escolar esteja rodando em: http://localhost:5000

E que os endpoints GET /turmas/<id> e (opcionalmente) GET /alunos/<id> estejam funcionando corretamente, para que a validação seja realizada com sucesso.

## 📦 Estrutura do Projeto

```bash
reserva-de-sala-flask/
├── app.py                 
├── reserva_model.py       
├── database.py            
├── reserva_routes.py      
├── requirements.txt       
└── README.md              
```


# 🛠️ Futuras Melhorias

Validação de conflito de horário na sala

Integração via fila (RabbitMQ) com outros microsserviços

Autenticação de usuários

Docker Compose

# 🧑‍💻 Autores

Arthur Hermoso

Luana Garrido Moreira Dias

Rafaela Santos Rodrigues

Vitória da Silva Moço

Fanthine Vitoria de Souza
