from flask import Flask, render_template, request
from views.home import home
#from views.Board import Board


app = Flask(__name__)

app.register_blueprint(home)

@app.route('/')
def router():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
