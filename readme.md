# Projeto CheetosChess

![Python application](https://github.com/adsmaicon/serverless_chess/workflows/Python%20application/badge.svg?branch=master)

</br>

Projeto da Guilda de Python Serverless, onde será feito um jogo de xadrez com TDD.

</br>

## Criando o virtual env
```sh
$  python3 -m venv .venv
```

## Ativar o virtual env
```sh
$  source .venv/bin/activate
``` 

## Instalar os pacotes necessários

```sh
pip3 install chalice
pip3 install boto3
pip3 install pytest
```
<br/>

### Definir local do python
No vscode, utilizando o comando `Ctrl + Shift + P`, encontrar a opção `Python: Select Interpreter` e informar o caminho do .venv (.venv/bin/python)

<br/>

### Definindo a ferramenta de Testes
No vscode, utilizando o comando `Ctrl + Shift + P`, encontrar a opção `Python: Configure Tests`, selecionar `pytest`, e informar a pasta `tests`

<br/>

### Executar os testes
```sh
pytest tests/
```
