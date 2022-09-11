from flask import Blueprint


# Добавим настройку директории с шаблонами
error_blueprint = Blueprint('error_blueprint', __name__,)

# Добавим обработчик запросов к несуществующим страницам
@error_blueprint.app_errorhandler(404)
def page_not_found(e):
    return 'Страница не найдена'

# Добавим обработчик ошибок, возникших на стороне сервера
@error_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return 'На сервере что-то пошло не так('

