from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


title = Blueprint('title',__name__)
@title.route('/title') #定義URL
def router_title():
    return render_template('/title.html')

