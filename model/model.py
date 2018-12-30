#from models.pg_model import pg_model
from model.postgreSQL import postgreSQL

class model():
	dao = postgreSQL()
	# dao = pg_model()
	def create(self):
		model.dao.create(type(self).__name__, self.__dict__)