from chalice.test import Client
from pytest import fixture
from app import app
import json


@fixture
def test_client():
    with Client(app) as client:
        yield client


def test_primeira_jogada(test_client):
    result = test_client.http.post("/jogo/novo", headers={"Content-type": "application/json"}, 
    body=json.dumps({
        'nick_name': 'pepo'
        })
    )
    assert result.status_code == 201