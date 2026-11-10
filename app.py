"""API de tarefas do laboratório prático de CI/CD do curso TADS."""

import os

from flask import Flask, jsonify


app = Flask(__name__)

TAREFAS = [
    {"id": 1, "titulo": "Criar repositório", "concluida": True},
    {"id": 2, "titulo": "Configurar CI/CD", "concluida": False},
]


@app.get("/")
def inicio():
    return jsonify({
        "mensagem": "Laboratório CI/CD TADS",
        "versao": "1.0.0",
    })


@app.get("/saude")
def saude():
    return jsonify({"status": "falha"})


@app.get("/tarefas")
def listar_tarefas():
    return jsonify(TAREFAS)


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=porta)
