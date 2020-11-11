from chalice.test import Client
from pytest import fixture
from app import app
import json


@fixture
def test_client():
    with Client(app) as client:
        yield client


def test_primeira_jogada(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({
        'piece_code': '', 
        'square_origin': 'A2',
        'square_destination': 'A4'
        })
    )
    assert result.status_code == 201


def test_primeira_jogada_uma_casa(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({
        'piece_code': '', 
        'square_origin': 'A2',
        'square_destination': 'A3'
        })
    )
    assert result.status_code == 201


def test_primeira_jogada_falha(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({
        'piece_code': '', 
        'square_origin': 'A2',
        'square_destination': 'A1'
        })
    )
    assert result.status_code == 201


def test_primeira_jogada_adjacente_falha(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({
        'piece_code': '', 
        'square_origin': 'A2',
        'square_destination': 'B3'
        })
    )
    assert result.status_code == 422