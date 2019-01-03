from model.model import model

class Post(model):

    def __init__(self, title, description, author, board, username):
        self.title = title
        self.description = description
        self.author = author
        self.board = board
        self.username = username