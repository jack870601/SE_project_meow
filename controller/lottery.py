from flask import Flask, render_template,Blueprint, request,session

#from views.Board import Board


lottery = Blueprint('lottery',__name__)
@lottery.route('/lottery') #定義URL
def router_lottery():
	if session.get("user"):
		user = session['user']
		username = user['username']
	return render_template('/lottery.html', **locals())

