"""Verificações solicitadas no roteiro de laboratório."""

from app import app


def test_pagina_inicial():
    cliente = app.test_client()
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.get_json()["mensagem"] == "Laboratório CI/CD TADS"


def test_saude():
    cliente = app.test_client()
    resposta = cliente.get("/saude")
    assert resposta.status_code == 200
    assert resposta.get_json()["status"] == "ok"


def test_tarefas():
    cliente = app.test_client()
    resposta = cliente.get("/tarefas")
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert len(dados) == 2
    assert dados[0]["titulo"] == "Criar repositório"


def test_rota_inexistente():
    cliente = app.test_client()
    resposta = cliente.get("/rota-inexistente")
    assert resposta.status_code == 404
