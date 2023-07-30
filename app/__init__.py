


from flask import Flask  # pass Импорт фласк
from flask_sqlalchemy import SQLAlchemy   # pass импорт алхимии для работы с базами данных
from flask_login import LoginManager   # pass импорт фласк логин для авторизации

app = Flask(__name__)   # pass создание объекта типа фласк (создание приложения с именем app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'   # pass добавление ключа для работы сиссии и др
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'   # pass настройка базы данных указываем sqllite
db = SQLAlchemy(app)   # pass создание объекта db для работы с базой в алхимии



login_manager = LoginManager()   # pass создаем объект класса логин менеджер для авторизации
login_manager.login_view = 'autorization'   # pass указыв функцию авторизации
login_manager.init_app(app)   # pass указыв связи с приложением app
login_manager.login_message_category = "info"
login_manager.session_protection = "strong"


from .models import Users   # pass импорт класса пользователи из моделей
from app import models   # pass импорт моделей 
from app import views   # pass импорт роутов (маршрутизаторов) в приложение

