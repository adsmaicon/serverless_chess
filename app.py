from chalice import Chalice, Response, UnprocessableEntityError
from chalicelib.model.piece import Piece
from chalicelib.model.board import Board

app = Chalice(app_name='chess')


@app.route('/jogo/{id_jogo}/jogada', methods=["POST"])
def jogada(id_jogo):
    request_body = app.current_request.json_body

    piece = Piece()

    if (request_body is None 
    or "piece_code" not in request_body
    or "square_origin" not in request_body
    or "square_destination" not in request_body
    or not piece.code_validator(request_body.get("piece_code"))
    or not Board().square_validator(request_body.get("square_origin"))
    or not Board().square_validator(request_body.get("square_destination"))):
        raise UnprocessableEntityError()

    p = piece.get_piece(request_body.get("piece_code"))
    if not p.position_validator(request_body.get("square_origin"), request_body.get("square_destination")):
        raise UnprocessableEntityError()
    
    return Response({'hello': id_jogo}, status_code=201)


@app.route('/jogo/novo', methods=["POST"])
def jogada():
    request_body = app.current_request.json_body

    return Response({'hello': "teste"}, status_code=201)