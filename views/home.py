from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


home = Blueprint('home',__name__)
@home.route('/home') #定義URL
def router_home():
    return render_template('/home.html')

