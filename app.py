from flask import Flask

#  Импортируем блюрпринты
from blueprints.main.views import main_blueprint
from blueprints.search.views import search_blueprint
from blueprints.api.api import api
from blueprints.errors.views import error_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# Регистрируем юлюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(api)
app.register_blueprint(error_blueprint)


if __name__ == "__main__":
    app.run()

