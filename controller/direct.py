from flask import Flask, render_template,Blueprint, request,session,redirect
from model.Board import Board
from model.Post import Post
#from views.Board import Board


direct = Blueprint('direct',__name__)
@direct.route('/direct') #定義URL
def router_direct():

	return redirect('/home/1', **locals())

