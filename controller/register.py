from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


register = Blueprint('register',__name__)
@register.route('/register') #定義URL
def router_login():
    return render_template('/register.html')

