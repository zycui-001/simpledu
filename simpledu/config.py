class BaseConfig(object):
	SECRET_KEY = 'makesure to set a very secret key'
	INDEX_PER_PAGE = 9
	ADMIN_PER_PAGE = 15

class DevlopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
	pass

configs = {
	'development': DevlopmentConfig,
	'production': ProductionConfig
}