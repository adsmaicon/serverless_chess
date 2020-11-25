from chalice.test import Client
from pytest import fixture
from app import app
import json


@fixture
def test_client():
    with Client(app) as client:
        yield client


def test_start_game(test_client):
    result = test_client.http.post(
        "/jogo/novo",
        headers={
            "Content-type": "application/json"
        },
        body=json.dumps({
            'nick_name': 'pepo'
        })
    )
    assert result.status_code == 201


def test_start_game_header_location(test_client):
    result = test_client.http.post(
        "/jogo/novo",
        headers={
            "Content-type": "application/json"
        },
        body=json.dumps({
            'nick_name': 'Alisson'
        })
    )
    headers = list(map(lambda x: x.lower(), result.headers))
    assert 'location' in headers


def test_start_game_get_game_id(test_client):
    result = test_client.http.post(
        "/jogo/novo",
        headers={
            "Content-type": "application/json"
        },
        body=json.dumps({
            'nick_name': 'Alisson'
        })
    )

    headers = {k.lower(): v for k, v in result.headers.items()}
    uriSplitted = headers['location'].split('/')

    assert len(uriSplitted) > 3 
