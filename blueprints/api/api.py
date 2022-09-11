from flask import Blueprint, request, jsonify
from utils import get_posts_all, get_post_by_pk
import logging


logging.basicConfig(filename='./logs/api.log', level=logging.INFO)
logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

api = Blueprint('api', __name__)

# Создаем представление, которое обрабатывает запрос GET /api/posts
@api.route('/api/posts')
def api_posts():

    posts = get_posts_all()
    logging.info('Запрос api/posts')
    return jsonify(posts)


# Создаем представление, которое обрабатывает запрос GET /api/posts/<post_id>
@api.route('/api/posts/<int:post_pk>')
def api_certain_post(post_pk):
    post = get_post_by_pk(post_pk)
    logging.info(f'Запрос api/posts/{post_pk}')
    return jsonify(post)