from flask import Flask, render_template
from flask import request

#from views.Board import Board


app = Flask(__name__)


@app.route('/')
def router():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
