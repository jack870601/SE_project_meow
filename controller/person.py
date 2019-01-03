from flask import Flask, render_template,Blueprint, request,session

#from views.Board import Board


person = Blueprint('person',__name__)
@person.route('/person') #定義URL
def router_login():
	if session.get("user"):
		user = session['user']
		username = user['username']
		coin = user['coin']
		title = user['title']
	return render_template('/person.html',**locals())