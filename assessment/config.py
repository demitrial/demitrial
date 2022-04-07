class Config(object):
    DEBUG = False
    TESTING = False
    SQLAlCHEMY_DATABASE_URI = 'mysql://root:password@localhost/assessment'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/assessment'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/assessment'
