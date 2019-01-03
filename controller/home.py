from flask import Flask, render_template,Blueprint, request,session
from model.Board import Board
from model.User import User
from model.Post import Post
#from views.Board import Board


home = Blueprint('home',__name__)
@home.route('/home/<int:id>', methods=['GET', 'POST']) #定義URL
def router_home(id):
	if session.get("user"):
		user = session['user']
		username = user['username']
	
	#Board = Board.filter()
	post_all = Post.filter(board=id)
	
	# id = Board.filter(name="run")[0]['id']
	# all_post = Post.filter(board=id)

	if request.method == "POST":
		title = request.form['title']
		description = request.form['description']
		newPost = Post(title=title,description=description,board=id,author=user['id'],username=username)
		newPost.create()

		 
	return render_template('/home.html', **locals())

