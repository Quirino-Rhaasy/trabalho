from src.app import app

client = app.test_client()

def test_home():

    resposta = client.get("/")

    assert resposta.status_code == 200

def test_criar_tarefa():

    resposta = client.post(
        "/tarefas",
        json={"titulo": "Estudar Engenharia de Software"}
    )

    assert resposta.status_code == 201

def test_listar():

    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
