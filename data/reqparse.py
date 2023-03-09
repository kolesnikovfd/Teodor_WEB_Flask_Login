from flask_restful import reqparse

parser_news = reqparse.RequestParser()
parser_news.add_argument('title', required=True)
parser_news.add_argument('content', required=True)
parser_news.add_argument('is_private', required=True, type=bool)
parser_news.add_argument('is_published', required=True, type=bool)
parser_news.add_argument('user_id', required=True, type=int)

parser_user = reqparse.RequestParser()
parser_user.add_argument('id', required=True)
parser_user.add_argument('name', required=True)
parser_user.add_argument('about', required=True, type=bool)
parser_user.add_argument('email', required=True, type=bool)
parser_user.add_argument('created_date', required=True, type=int)
