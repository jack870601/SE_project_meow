from flask import Flask, render_template, request
from  controller.direct import direct
from  controller.home import home
from  controller.login import login
from  controller.title import title
from  controller.lottery import lottery
from  controller.person import person
from  controller.register import register
from  controller.logout import logout
#from views.Board import Board


app = Flask(__name__)
app.register_blueprint(direct)
app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(title)
app.register_blueprint(lottery)
app.register_blueprint(person)
app.register_blueprint(register)
app.register_blueprint(logout)
@app.route('/')
def router():
    return render_template('index.html')


if __name__ == '__main__':
	app.secret_key = 'some secret key'
	app.run(debug=True)
