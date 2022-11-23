class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "1235asdzxqer34asd31sdf"
    MAIL_SERVER = 'mail.ehelpingbusiness.com'
    MAIL_PORT= 587
    MAIL_USERNAME = 'hrm@ehelpingbusiness.com'
    MAIL_PASSWORD = 'pass@hrm.com'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False