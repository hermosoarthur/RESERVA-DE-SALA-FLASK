📚 API de Reserva de Salas
Este repositório contém a API de Reserva de Salas, desenvolvida com Flask e SQLAlchemy, como parte de uma arquitetura baseada em microsserviços.

🧩 Arquitetura
A API de Reserva de Salas é um microsserviço que faz parte de um sistema maior chamado School System, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ Esta API depende de outra API de Gerenciamento Escolar (School System), que deve estar em execução e exposta localmente.

A comunicação entre os serviços ocorre via requisições HTTP REST, para validar:

Se a Turma existe: GET /turmas/<id>

(Opcional) Se o Aluno existe: GET /alunos/<id> → Pode ser desativado se não for usado.

🚀 Tecnologias Utilizadas
Python 3.x

Flask

SQLAlchemy

SQLite (como banco de dados local)

Requests (para consumo da API externa)

▶️ Como Executar a API
Clone o repositório:
git clone https://github.com/hermosoarthur/RESERVA-DE-SALA-FLASK
cd reserva-salas

Crie um ambiente virtual (opcional, mas recomendado):
python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

Instale as dependências:
pip install -r requirements.txt

Execute a API:
python app.py

A aplicação estará disponível em: 📍 http://localhost:5001

📝 Observação: O banco de dados é criado automaticamente na primeira execução.

📡 Endpoints Principais
GET /reservas → Lista todas as reservas

POST /reservas → Cria uma nova reserva

GET /reservas/<id> → Detalha uma reserva

PUT /reservas/<id> → Atualiza uma reserva

DELETE /reservas/<id> → Remove uma reserva

Exemplo de corpo JSON para criação:
{ "turma_id": 1, "sala": "101", "data": "2025-05-06", "hora_inicio": "14:00", "hora_fim": "16:00" }

🔗 Dependência Externa
Certifique-se de que a API de Gerenciamento Escolar esteja rodando em: http://localhost:5000

E que os endpoints GET /turmas/<id> e (opcionalmente) GET /alunos/<id> estejam funcionando corretamente, para que a validação seja realizada com sucesso.

📦 Estrutura do Projeto
reserva-salas/
├── app.py
├── reserva_model.py
├── database.py
├── routes.py
├── requirements.txt
└── README.md

🛠️ Futuras Melhorias
Validação de conflito de horário na sala

Integração via fila (RabbitMQ) com outros microsserviços

Autenticação de usuários

🧑‍💻 Autores
Arthur Hermoso

Luana Garrido Moreira Dias

Rafaela Santos Rodrigues

Vitória da Silva Moço

Fanthine Vitoria de Souza