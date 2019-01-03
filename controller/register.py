from flask import Flask, render_template, Blueprint, request, redirect
from model.User import User

#from views.Board import Board


register = Blueprint('register',__name__)
@register.route('/register', methods=['GET', 'POST']) #定義URL
def router_register():
	if request.method == 'POST':

		username = request.form['username']
		password = request.form['password']
		newUser = User(username=username,password=password,login_count=0, is_admin=0, is_active=1,title="無",profile="無",coin=5)
		newUser.create()
		return redirect('/login')
	else:
		return render_template('/register.html')

