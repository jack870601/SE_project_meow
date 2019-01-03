from flask import Flask, render_template,Blueprint, request,session,redirect

#from views.Board import Board


logout = Blueprint('logout',__name__)
@logout.route('/logout') #定義URL
def router_logout():
	session.clear()
	return redirect('/home/1')

