from flask import Flask, render_template,Blueprint, request,session
from model.User import User
#from views.Board import Board


lottery = Blueprint('lottery',__name__)
@lottery.route('/lottery', methods=['GET', 'POST']) #定義URL
def router_lottery():
	if session.get("user"):
		user = session['user']
		username = user['username']

	if request.method =="POST":
		NewUser_name = User.filter(id=1)[0]['username']
	return render_template('/lottery.html', **locals())

