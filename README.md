# Info Clinicas

Sistema para gestão de clínicas

## Setup

Crie um virtualenv para o projeto e ative:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

Como o virtualenv ativado, instale as dependências
```bash
pip3 install --upgrade pip && pip3 install -r requirements-dev.txt
```

## Rodando

```bash
python3 manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)