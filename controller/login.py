from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


login = Blueprint('login',__name__)
@login.route('/login') #定義URL
def router_login():
    return render_template('/login.html')

