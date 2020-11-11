import boto3


BOARD_TABLE = "vhchess"

class BoardRepository:
    """
    docstring
    """

    def __init__(self):
        """
        docstring
        """
        self._client = boto3.client('dynamodb')


    def save_board(self, board):
        response = self._client.put_item(
            TableName=BOARD_TABLE,
            Item=board
        )

        return response