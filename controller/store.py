from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


store = Blueprint('store',__name__)
@store.route('/store') #定義URL
def router_store():
    return render_template('/store.html')

