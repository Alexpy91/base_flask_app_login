from app import app
from flask import render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users
from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
from flask_login import login_user, login_required, logout_user

@app.route('/', methods=['GET'])  #  роут для главной страницы (метод ГЕТ)
def index():					  #  главная функция  	
	return render_template('index.html',title='Главная страница')  #  возвращаем адрес главн страницы 






@app.route('/registration', methods=['POST', 'GET'])
def registratrion():
	if request.method == 'POST':
		try:
			hash = generate_password_hash(request.form['psw'])  #  получение хеша введенного пароля для сохр его в базе
			
			u = Users(name=request.form['name'], email=request.form['email'], avatar=request.form['image'], login=request.form['login'], password=hash, points=0, message='', task='', status=0, level=1)  #  создание объекта u в который записываем что пойдет в базу
			db.session.add(u)  #  добавление в сессию
			db.session.flush()  #  сохранение в сессии
			db.session.commit()  #  сохранение в базе

		except:	
			db.session.rollback()  #  откат сохранения из базы
			print("Ошибка добавления в базу данных")
	return render_template('registration.html',title='Регистрация')

@app.route('/login', methods=['GET', 'POST'])
def autorization():
	login = request.form.get('login')   #  запись в переменную то, что получили от пользователя поле логин
	password = request.form.get('psw')
	remember = True if request.form.get('remember') else False
	if login and password:  #  если поля логин и пароль не пустые 
		user = Users.query.filter_by(login=login).first()  #  в переменную user записыаваем первую запись из базы найденную по введенному логину 

		if user and check_password_hash(user.password, password):  #  сравниваем хэш пароля в базе и хэш созданный для введенного при авторизации пароля 
			login_user(user)  #  авторизируем в системе пользователя user
			next_page = request.args.get('next')  #  запоминаем по какому адресу до авторизации пытался попасть пользователь 
			return redirect(next_page)  #  перенаправляем его на эту страницу после авторизации

			# return redirect(url_for('profile'))
		else:
			flash("Неверные поля логин или пароль!", category='error')
			return render_template("login.html")
			
	else:
		flash("Заполните поля логин и пароль!", category='error')
		
		return render_template("login.html")

		
@app.route('/logout', methods=['POST', 'GET'])  #  Метод для выхода пользователя
@login_required  #  декоратор не пропускающий если пользователь не авторизирован (выйти могут только авторизированные) 
def logout():
	logout_user()  #  выход пользователя 
	return redirect(url_for('autorization'))  #  перенаправление на авторизацию 


@app.route('/profile', methods=['GET'])
@login_required  #Вешается если на эту страницу только авторизованные
def profile():
	user_data = Users.query.get(1)  #  В скобках нужно как то передать id того пользователя который авторизирован
	return render_template('profile.html',title='Профиль пользователя', user_data=user_data)



@app.after_request  #  спец декаратор отслеживающий коды ответов сервера 
def redirect_to_signin(response):  #  созд функцию передаем в нее статус ответа сервера
	if response.status_code == 401:  #  401 это статус что страница не доступна для неавторизированных
		return redirect(url_for('autorization') + '?next=' + request.url)  #  создание строки для перенаправления
		
	return response