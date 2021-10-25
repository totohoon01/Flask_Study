import os

BASE_DIR = os.path.dirname(__file__)

# 정해진 이름!
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

# pip install Flask-Migrate
# flask db init
# flask db migrate
# flask db upgrade
# pip install Flask-WTF
