from flask import Flask, render_template, request
<<<<<<< HEAD
from controller.home import home
from controller.store import store
from controller.login import login
=======
from  controller.home import home
from  controller.store import store
from  controller.login import login
from  controller.title import title
>>>>>>> ef537b63531fbd6a36ef21ac14aa83d5160becbb
#from views.Board import Board


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(store)
app.register_blueprint(login)
app.register_blueprint(title)
@app.route('/')
def router():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
