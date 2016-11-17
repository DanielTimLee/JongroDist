from flask import request
from flask_restful import Resource

from app import api_root, db, oauth_provider
from app.api.exceptions import ConflictError
from app.models.application.board import BoardModel


@api_root.resource('/v1/board')
class Board(Resource):
    def get(self):
        boards = BoardModel.query.all()

        # TODO: 데이터가 존재하지 않을 경우 에러 발생.
        # TODO: 에러 핸들링 중에 NotFound 404 외에 데이터 부재시 에러 처리.
        if not boards:
            raise ConflictError

        board_list = []
        for board in boards:
            board_list.append({
                'id': board.id,
                'name': board.name,
                'title': board.title,
            })

        return {
            'items': board_list
        }

    @oauth_provider.require_oauth('manage_site')
    def post(self):
        request_body = request.get_json()

        new_board = BoardModel(
            name=request_body['name'],
            title=request_body['title']
        )
        db.session.add(new_board)
        db.session.commit()

        return {
            'success': True,
            'messages': [
                '성공적으로 반영되었습니다.'
            ]
        }
