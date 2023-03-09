from flask import jsonify
from flask_restful import abort, Resource

from . import db_session
from .reqparse import parser_user
from .users import User


def abort_if_news_not_found(id):
    session = db_session.create_session()
    news = session.query(User).get(id)
    if not news:
        abort(404, message=f"User {id} not found")


class UsersResource(Resource):
    def get(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        user = session.query(User).get(id)
        return jsonify({'user': user.to_dict(
            only=('id', 'name', 'about', 'email', 'created_date'))})

    def delete(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        user = session.query(User).get(id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('id', 'name', 'email')) for item in users]})

    def post(self):
        args = parser_user.parse_args()
        session = db_session.create_session()
        user = User(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            created_date=args['created_date']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
