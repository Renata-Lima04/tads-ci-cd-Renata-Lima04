# Laboratório prático de CI/CD — TADS

Projeto baseado no roteiro de 200 minutos: API Flask, testes com pytest,
integração contínua no GitHub Actions e publicação no Render condicionada à
aprovação dos checks.

## Funcionalidades

| Rota | Método | Resultado |
|---|---|---|
| `/` | GET | Identificação da API e versão `1.1.0` |
| `/saude` | GET | `{"status": "ok"}` |
| `/tarefas` | GET | Lista de duas tarefas |
| Qualquer rota ausente | GET | HTTP `404` |

## Executar no computador

Requisitos: Python 3.12+ e Git.

```powershell
# Windows / PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python app.py
```

No Linux/macOS, ative o ambiente com `source .venv/bin/activate`.
Abra `http://localhost:5000/`, `/saude` e `/tarefas`.

## GitHub Actions (CI)

O arquivo `.github/workflows/ci.yml` executa os quatro testes em cada push
para `main` e pull request para `main`. Usa Python 3.12.

## Publicação no Render (CD)

O arquivo `render.yaml` é um Blueprint opcional para criar o serviço. Também
é possível criar **New > Web Service**, conectado ao repositório GitHub:

- Branch: `main`
- Runtime: `Python 3`
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Plano: `Free` se estiver disponível, sem confirmar custos pagos
- Auto-Deploy: **After CI Checks Pass**

A regra de CI não dispensa aprovação explícita dos serviços no painel e a
primeira implantação pode ocorrer imediatamente ao criar o Web Service.
Verifique no painel se a configuração ficou em **After CI Checks Pass**.

## Experimento de falha e recuperação

O histórico registra a falha controlada em `/saude` e a recuperação na versão `1.1.0`. As execuções podem ser conferidas na guia Actions.

## Estrutura

```text
app.py                       API Flask
requirements.txt             Dependências
.gitignore                   Arquivos ignorados
.python-version              Python 3.12
render.yaml                  Blueprint de hospedagem
.github/workflows/ci.yml     Workflow de CI
tests/test_app.py            Quatro testes
docs/                       Relatório e roteiro de publicação
scripts/                     Comandos auxiliares
```

**Atenção:** não salve credenciais, chaves ou tokens neste repositório.
