from chalice import Chalice, Response, UnprocessableEntityError
from chalicelib.model.piece import Piece
from chalicelib.model.board import Board

app = Chalice(app_name='chess')


@app.route('/jogo/{id_jogo}/jogada', methods=["POST"])
def jogada(id_jogo):
    request_body = app.current_request.json_body

    if (request_body is None 
    or "piece_code" not in request_body
    or "square" not in request_body
    or not Piece().code_validator(request_body.get("piece_code"))
    or not Board().square_validator(request_body.get("square"))):
        raise UnprocessableEntityError()
    
    return Response({'hello': id_jogo}, status_code=201)
