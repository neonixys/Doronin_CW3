from flask import Blueprint, render_template, request
from utils import search_for_posts, get_posts_all, get_posts_by_user

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


# Создаем представление для поиска по маршруту
@search_blueprint.route('/search/')
def search_page():
    s = request.args.get('s')
    suitable_posts = search_for_posts(s)

    return render_template('search.html', posts=suitable_posts)
