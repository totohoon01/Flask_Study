# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate, migrate
from models import db
from views import main_views, user_views, question_views, answer_views
import config

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # 블루프린터 등록
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    # ORM
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
