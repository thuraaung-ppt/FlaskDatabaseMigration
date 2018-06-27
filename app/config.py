
import os 

class Configuration: 

	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	DEBUG = True 
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/test.db' % APPLICATION_DIR
	SQLALCHEMY_TRACK_MODIFICATIONS = 'Testing database'
	SECRET_KEY = 'This is my secret key'

	