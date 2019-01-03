from flask import Flask, render_template,Blueprint, request,redirect, session, url_for
from model.User import User

#from views.Board import Board


login = Blueprint('login',__name__)
@login.route('/login', methods=['GET', 'POST']) #定義URL
def router_login():
	if session.get("user"):
		return redirect(url_for('home.router_home'))
	else:
		if request.method == "POST":
			username = request.form['username']
			findUser = User.filter(username=username)
			if len(findUser) == 0:
				return redirect('/login?msg=error')
			else:
				session['user'] = User.filter(username=username)[0]
				request.user = User.filter(username=username)[0]
				message = "帳號登入成功"
				return redirect(url_for('direct.router_direct',**locals()))
		else:
			return render_template('/login.html')

