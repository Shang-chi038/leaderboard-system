class Config:

    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass

config_dict = {
    "default" : DevelopmentConfig,
    "development" : DevelopmentConfig	
}