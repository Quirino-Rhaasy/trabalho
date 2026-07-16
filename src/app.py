from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []
contador = 1

@app.route("/")
def home():
    return {"mensagem": "Sistema de Gerenciamento de Tarefas"}

@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar():

    global contador

    dados = request.json

    tarefa = {
        "id": contador,
        "titulo": dados["titulo"],
        "concluida": False
    }

    tarefas.append(tarefa)
    contador += 1

    return jsonify(tarefa), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):

    dados = request.json

    for tarefa in tarefas:

        if tarefa["id"] == id:

            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])

            return jsonify(tarefa)

    return {"erro": "Tarefa não encontrada"}, 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir(id):

    global tarefas

    tarefas = [t for t in tarefas if t["id"] != id]

    return {"mensagem": "Tarefa removida"}

if __name__ == "__main__":
    app.run(debug=True)
