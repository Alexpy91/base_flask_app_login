
from flask_login import UserMixin  #  импорт миксин для спользования flask login
from datetime import datetime
from app import db, login_manager  #  импортируем ранее созданный объект login_manager (объект класса Login_Manager)


class Users(UserMixin, db.Model):  #  создаем модель пользователя
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	login = db.Column(db.String(30),  unique=True)
	email = db.Column(db.String(30), nullable=False, unique=True)
	avatar = db.Column(db.String, nullable=True)
	password = db.Column(db.String(500), nullable=False)
	data_reg = db.Column(db.DateTime, default=datetime.utcnow)
	points = db.Column(db.Integer)
	message = db.Column(db.String(2500))
	task = db.Column(db.Text)
	status = db.Column(db.Integer)
	level = db.Column(db.Integer)

	def __repr__(self):  #  создаем представлени модели для вывода в консоль
		return f"<Users {self.id}"
	
class Task(db.Model):  #  создаем модель задания
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(150), nullable=False)
	text_task = db.Column(db.String(1500))
	photo = db.Column(db.String, nullable=True)
	data_pub = db.Column(db.DateTime, default=datetime.utcnow)
	level = db.Column(db.Integer)

	def __repr__(self):  #  создаем представлени модели для вывода в консоль
		return f"<Task {self.id}"

@login_manager.user_loader  #  декоратор авторизации пользователя
def load_user(user_id):
    return Users.query.get(int(user_id))

