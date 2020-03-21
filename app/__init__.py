from flask import Flask
from configure import ProductionConfig, DevelopmentConfig

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


def create_app(config_name):
    print("**** FLASK APP INITIATED ****")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    from .extract import extract as extract_blueprint
    app.register_blueprint(extract_blueprint)

    return app
