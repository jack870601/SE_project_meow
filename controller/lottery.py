from flask import Flask, render_template,Blueprint, request

#from views.Board import Board


lottery = Blueprint('lottery',__name__)
@lottery.route('/lottery') #定義URL
def router_lottery():
    return render_template('/lottery.html')

