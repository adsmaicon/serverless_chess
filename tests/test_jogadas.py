from chalice.test import Client
from pytest import fixture
from app import app
import json


@fixture
def test_client():
    with Client(app) as client:
        yield client

def test_empty_payload(test_client):
    result = test_client.http.post("/jogo/2/jogada")
    assert result.status_code == 422


def test_primeira_jogada(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'K', 'square': 'C5'}))
    assert result.json_body == {'hello': '2'}


def test_jogada_status_code_create(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': '', 'square': 'C5'}))
    assert result.status_code == 201


def test_invalid_piece_code(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'Banana', 'square': 'C5'}))
    assert result.status_code == 422


def test_invalid_square(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'K', 'square': 'xxx'}))
    assert result.status_code == 422


def test_invalid_square_column(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'K', 'square': 'X1'}))
    assert result.status_code == 422


def test_invalid_square_row(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'K', 'square': 'A9'}))
    assert result.status_code == 422


def test_invalid_square_empty(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'K', 'square': ''}))
    assert result.status_code == 422


def test_jogada_status_code_create(test_client):
    result = test_client.http.post("/jogo/2/jogada", headers={"Content-type": "application/json"}, 
    body=json.dumps({'piece_code': 'K', 'square': 'C5'}))
    assert result.status_code == 201    