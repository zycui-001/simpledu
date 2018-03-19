# -*-coding:utf-8-*-

from flask import Blueprint, render_template, flash, url_for, redirect, request, current_app
from simpledu.models import Course, db, User
from simpledu.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required


# 省略了 url_prefix,那么默认就是‘／’
front = Blueprint('front', __name__)

@front.route('/')
def index():
#	courses = Course.query.all()
	page = request.args.get('page', default=1, type=int)
	pagination = Course.query.paginate(
		page=page,
		per_page=current_app.config['INDEX_PER_PAGE'],
		error_out=False)
	return render_template('index.html', pagination=pagination)
#	return render_template('index.html', courses=courses)


@front.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		login_user(user, form.remember_me.data)
		return redirect(url_for('.index'))
	return render_template('login.html', form=form)

@front.route('/logout')
@login_required
def logout():
	logout_user()
	flash('您已退出登录', 'success')
	return redirect(url_for('.index'))

@front.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		form.create_user()
		flash('注册成功，清登录！', 'success')
		return redirect(url_for('.login'))
	return render_template('register.html', form=form)
