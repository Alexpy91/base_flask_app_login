
from flask_login import UserMixin  #  импорт миксин для спользования flask login
from datetime import datetime
from app import db, login_manager  #  импортируем ранее созданный объект login_manager (объект класса Login_Manager)


class Users(UserMixin, db.Model):  #  создаем модель пользователя
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	login = db.Column(db.String(30))
	email = db.Column(db.String(30), unique=True)
	avatar = db.Column(db.String(100))
	password = db.Column(db.String(500), nullable=True)
	data_reg = db.Column(db.DateTime, default=datetime.utcnow)
	points = db.Column(db.Integer)
	message = db.Column(db.String(1500))
	task = db.Column(db.Text)
	status = db.Column(db.Integer)
	level = db.Column(db.Integer)

	def __repr__(self):  #  создаем представлени модели для вывода в консоль
		return f"<Users {self.id}"

@login_manager.user_loader  #  декоратор авторизации пользователя
def load_user(user_id):
    return Users.query.get(int(user_id))