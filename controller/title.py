from flask import Flask, render_template,Blueprint, request,session

#from views.Board import Board


title = Blueprint('title',__name__)
@title.route('/title') #定義URL
def router_title():
	if session.get("user"):
		user = session['user']
		username = user['username']


	return render_template('/title.html', **locals())

