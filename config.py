import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True
 
class ProductionConfig(Config):
    DEBUG = False
       
config = {
'development': DevelopmentConfig,
'production': ProductionConfig,
'default' : DevelopmentConfig
}