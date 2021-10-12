# Info Clinicas

Sistema para Gestão de Clínicas

Aplicação disponível em https://info-clinicas-dev.herokuapp.com

## Setup

Crie um virtualenv para o projeto e ative:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

Como o virtualenv ativado, instale as dependências
```bash
pip3 install --upgrade pip && pip3 install -r requirements-dev.txt
```

## Rodando - Desenvolvimento

```bash
python3 manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

## Deploy

### Ambiente de DESENVOLVIMENTO

Deploy configurado para fazer automaticamente, conforme alterações na branch `dev`

Para fazer de forma manual rodar:
```bash
git push dev master
```

#### Disponível em
[https://info-clinicas-dev.herokuapp.com](https://info-clinicas-dev.herokuapp.com)


### Ambiente de PRODUÇÃO

Deploy configurado para fazer automaticamente, conforme alterações na branch `master`

Para fazer de forma manual rodar:
```bash
git push prod master
```

#### Disponível em
[https://info-clinicas.herokuapp.com/](https://info-clinicas.herokuapp.com/)
