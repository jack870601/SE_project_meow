from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


person = Blueprint('person',__name__)
@person.route('/person') #定義URL
def router_login():
    return render_template('/person.html')