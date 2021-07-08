# -*- coding: utf-8 -*-
from flask import render_template
from app import application
from app.forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Робот клоун'}
    posts = [
        {
            'author': {'username': 'Игорь'},
            'body': 'что такое коворкинг??? и где его найти??? как делать скриншот???'
        },
        {
            'author': {'username': 'Аврам'},
            'body': 'скоро тут все будет'
        }, 
        {
            'author': {'username': 'Гетельман'},
            'body': 'люблю хлеб с майонезом'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

from flask import render_template, flash, redirect, url_for


@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
